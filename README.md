# 🧭 AI Job Layoff Risk Predictor

A machine learning web app that predicts whether a job role is at **Low**, **Medium**, or **High** risk of being affected by AI and automation — based on role details, industry, and how much AI is already used in that job.

Built with **Streamlit** and a **Random Forest Classifier**.

---

## 🚀 Features

- Simple, guided form to enter role details (age, education, experience, industry, job role, etc.)
- AI exposure inputs — routine task %, automation %, AI adoption level, AI tools used, and more
- Instant prediction with a clear Low / Medium / High risk result
- Clean, responsive UI built entirely with Streamlit — no extra frontend code needed

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** — web app framework
- **scikit-learn** — Random Forest model
- **pandas** — data handling
- **joblib** — model loading

---

## 📦 Project Structure

```
AI-job-layoff-risk-predictor-System/
├── app.py                     # Main Streamlit app
├── layoff_Risk model.pkl      # Trained Random Forest model
├── .streamlit/
│   └── config.toml            # App theme (colors, fonts)
├── requirements.txt           # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/iqrabb/AI-job-layoff-risk-predictor-System.git
   cd AI-job-layoff-risk-predictor-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```

4. Open the local URL shown in your terminal (usually `http://localhost:8501`).

---

## 📋 How It Works

1. Enter details about the role — age, education level, experience, company size, industry, and job title.
2. Enter how exposed the role already is to AI — routine task percentage, automation level, number of AI tools used, and more.
3. Click **Predict Layoff Risk** to get an instant Low / Medium / High risk result.

---

## 🙋 Author

**Iqra  ❤️**
AI & Machine Learning Learner

---