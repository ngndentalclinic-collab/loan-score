import joblib
import warnings
warnings.filterwarnings('ignore')

# Load the model
data = joblib.load('loan_scoring_model.pkl')

print("=" * 50)
print("MODEL INSPECTION")
print("=" * 50)

print(f"\nLoaded object type: {type(data)}")

if isinstance(data, dict):
    print(f"Dictionary keys: {list(data.keys())}")
    
    # Try to find the classifier
    for key in ['classifier', 'model', 'clf', 'estimator']:
        if key in data:
            clf = data[key]
            print(f"\nFound '{key}':")
            print(f"  Type: {type(clf)}")
            if hasattr(clf, 'n_features_in_'):
                print(f"  Expected features: {clf.n_features_in_}")
            if hasattr(clf, 'feature_importances_'):
                print(f"  Feature importances: {clf.feature_importances_}")
            break
    
    # Also check for scalers
    for key in ['scaler', 'preprocessor', 'encoder']:
        if key in data:
            print(f"\nFound '{key}': {type(data[key])}")
else:
    print(f"\nDirect model type: {type(data)}")
    if hasattr(data, 'n_features_in_'):
        print(f"Expected features: {data.n_features_in_}")
