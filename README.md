# 🏦 Зээлийн үнэлгээ системүүд (Loan Scoring System)

Энэхүү Flask вэб апп нь машин сургалтын регрессион моделийг ашигладаг орчин үеийн зээлийн үнэлгээ системүүд юм. Машин сургалт ашигласан GradientBoostingClassifier моделийг ашиглаж, зээл өргөдлийг үнэлж, 0-1000 оноогоор үнэлгээ өгнө.

## ✨ Онцлог

- 💜 Гоо сайхан, адаптив дизайн (мобайл + десктоп)
- 🤖 Machine Learning дээр суурилсан үнэлгээ
- 📊 Оноо ба шийдвэрийн дүрслэл
- ⚡ Хурдан API хариу
- 🔒 Өгөгдлийн нормалжуулалт (StandardScaler)

## 📋 Шаардлага

- Python 3.8+
- Flask 3.0+
- scikit-learn 1.5+
- numpy 1.26+

## 🚀 Суснуулалт & Ажиллуулалт

### 1. Репозиториороо клон хийх
```bash
git clone https://github.com/YOUR_USERNAME/loan-scoring-system.git
cd "loan scoring"
```

### 2. Virtual Environment үүсгэх
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Хэрэгцээтэй сацуудлуудыг суснуулах
```bash
pip install -r requirements.txt
```

### 4. Апп ажиллуулах
```bash
python app.py
```

Дараа нь браузерээр орно:
```
http://localhost:5000
```

## 📝 Функц

### Оруулах үзүүлэлтүүд
- **Сарын цалин** (₮): Хэрэглэгчийн сарын орлого
- **Ажил эрхлэлтийн төрөл**: 
  - Байнгын ажилтан
  - Гэрээтэй ажилтан
  - Өөрийн сал эрхэлэгч
  - Оршин суугч
- **Ажилласан жил**: Нөхцөл байдлын жил
- **Хүссэн зээлийн дүн** (₮): Хүссэн зээлийн хэмжээ

### Гаралт

Модель 0-1000 хүртэлх оноо өгнө:

| Оноо | Шийдвэр | Дүрслэл |
|------|---------|---------|
| **700+** | ✅ **Зөвшөөрөх** | Зээл зөвшөөрөгдсөн |
| **450-700** | ⚠️ **Гар шалгалт** | Нэмэлт шалгалт шаардлагатай |
| **<450** | ❌ **Татгалзах** | Өргөдөл авч хүлээмшүүлэхгүй |

## 🔧 Техникийн детайл

### Model Pipeline
1. **Feature Engineering**: Сурсан үзүүлэлтүүдээс 8 шинэ параметр үүсгэнэ
2. **Feature Scaling**: StandardScaler ашигалан нормалжуулна
3. **Prediction**: GradientBoostingClassifier моделийн predict_proba() ашиглан магадлал тооцно
4. **Scoring**: Магадлалыг 0-1000 хүрээтэй оноо болгон хувиргана

### Үүсдэг параметрүүд
```
['monthly_income', 'employment_years', 'requested_amount', 
 'amount_to_income_ratio', 'annual_dti', 'log_income', 
 'log_amount', 'employment_type_encoded']
```

## 📁 Файл бүтэц

```
loan scoring/
├── app.py                    # Flask апп сервер
├── requirements.txt          # Python сацуудлуудын жагсаалт
├── loan_scoring_model.pkl    # Machine Learning модель + scaler
├── templates/
│   └── index.html           # Үндсэн HTML хуудас
├── README.md                # Энэ файл
├── .gitignore              # Git ignore rules
└── inspect_model.py         # Модель шалгах скрипт
```

## 🛠️ API Endpoints

### GET /
Үндсэн HTML хуудас буцаана

### POST /predict
Зээлийн үнэлгээ тооцнэ

**Request:**
```json
{
    "monthly_salary": 2000000,
    "employment_type": 0,
    "years_worked": 5,
    "desired_amount": 10000000
}
```

**Response:**
```json
{
    "success": true,
    "score": 750,
    "decision": "Зөвшөөрөх",
    "status": "approved",
    "message": "Таны өргөдөл зөвшөөрөгдсөн байна!"
}
```

## 🐛 Troubleshooting

### "Модель ачаалагдаагүй" алдаа
- loan_scoring_model.pkl файл байгаа эсэхийг шалгана
- app.py файл болон loan_scoring_model.pkl файлуудыг нэг фолдер дээр байлгаана

### "X has 4 features" алдаа
- Feature engineering орц алдаа (app.py-д засчихсан)
- Сервер рестарт хийнэ: `python app.py`

## 👨‍💻 GitHub-руу push хийх

```bash
# 1. GitHub-т шинэ репо үүсгэх (https://github.com/new)

# 2. Local git init хийх
git init
git add .
git commit -m "Initial commit: Loan scoring system"

# 3. Remote үүсгэх
git remote add origin https://github.com/YOUR_USERNAME/loan-scoring-system.git

# 4. Push хийх
git branch -M main
git push -u origin main
```

## 📄 Лиценз

MIT License

## 👤 Зохиолч

Created with ❤️

## 📞 Support

Асуулт эсвэл асуудал байвал GitHub Issues дээр нээ.

