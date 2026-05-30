import joblib
import numpy as np
from flask import Flask, render_template, request, jsonify
import os
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the model and supporting objects
model_path = os.path.join(os.path.dirname(__file__), 'loan_scoring_model.pkl')
try:
    loaded_data = joblib.load(model_path)
    # Handle case where file contains a dictionary
    if isinstance(loaded_data, dict):
        model = loaded_data.get('model')
        scaler = loaded_data.get('scaler')
        label_encoder_employment = loaded_data.get('label_encoder_employment')
        feature_cols = loaded_data.get('feature_cols', [])
        print(f"Model loaded from dictionary")
        print(f"Features expected: {feature_cols}")
    else:
        model = loaded_data
        scaler = None
        label_encoder_employment = None
        feature_cols = []
    
    print(f"Model type: {type(model)}")
    print(f"Scaler type: {type(scaler)}")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None
    scaler = None
    label_encoder_employment = None
    feature_cols = []

def get_decision(score):
    """Get decision based on score"""
    if score >= 700:
        return {
            'decision': 'Зөвшөөрөх',
            'status': 'approved',
            'message': 'Таны өргөдөл зөвшөөрөгдсөн байна!'
        }
    elif score >= 450:
        return {
            'decision': 'Гар шалгалт',
            'status': 'manual',
            'message': 'Таны өргөдөл гараар шалгагдах хэрэгтэй байна.'
        }
    else:
        return {
            'decision': 'Татгалзах',
            'status': 'rejected',
            'message': 'Уучлаарай, таны өргөдөл авч хүлээмшүүлэх боломжгүй байна.'
        }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return jsonify({
                'success': False,
                'error': 'Модель ачаалагдаагүй байна. Сервер алдаа.'
            }), 400
        
        data = request.json
        
        # Extract basic features from input
        monthly_income = float(data.get('monthly_salary', 0))
        employment_type_raw = int(data.get('employment_type', 0))
        employment_years = float(data.get('years_worked', 0))
        requested_amount = float(data.get('desired_amount', 0))
        
        # Validate inputs
        if monthly_income <= 0 or requested_amount <= 0 or employment_years < 0:
            return jsonify({
                'success': False,
                'error': 'Оруулсан утгууд буруу байна. Эерэг утга оруулна уу.'
            }), 400
        
        # Calculate derived features
        amount_to_income_ratio = requested_amount / (monthly_income * 12)
        
        # annual_dti: Assuming we use requested_amount as annual obligation divided by income
        annual_dti = requested_amount / (monthly_income * 12)
        
        # Log transformations
        log_income = np.log(monthly_income) if monthly_income > 0 else 0
        log_amount = np.log(requested_amount) if requested_amount > 0 else 0
        
        # Encode employment type - it's already an integer (0-3)
        employment_type_encoded = employment_type_raw
        
        # Prepare feature array in the expected order:
        # ['monthly_income', 'employment_years', 'requested_amount', 
        #  'amount_to_income_ratio', 'annual_dti', 'log_income', 'log_amount', 
        #  'employment_type_encoded']
        features_raw = np.array([[
            monthly_income,
            employment_years,
            requested_amount,
            amount_to_income_ratio,
            annual_dti,
            log_income,
            log_amount,
            employment_type_encoded
        ]])
        
        # Apply scaler if available
        if scaler is not None:
            features_scaled = scaler.transform(features_raw)
        else:
            features_scaled = features_raw
        
        # Make prediction
        if not hasattr(model, 'predict'):
            return jsonify({
                'success': False,
                'error': 'Модельд predict арга байхгүй байна. Загварын файл эвдэрсэн байж магадгүй.'
            }), 400
        
        # Get prediction probability
        if hasattr(model, 'predict_proba'):
            # Get probability of positive class (class 1)
            probabilities = model.predict_proba(features_scaled)[0]
            # Use probability of the positive class (last class)
            probability = probabilities[-1]
            score = max(0, min(1000, probability * 1000))
        else:
            # Fallback to direct prediction
            prediction = model.predict(features_scaled)[0]
            # Normalize to 0-1000 range
            score = max(0, min(1000, prediction * 1000))
        
        # Get decision
        decision_info = get_decision(score)
        
        return jsonify({
            'success': True,
            'score': round(score, 0),
            'decision': decision_info['decision'],
            'status': decision_info['status'],
            'message': decision_info['message']
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
