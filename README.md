# AI Job Layoff Risk Predictor System

A machine learning web application that predicts whether a job role is at Low, Medium, or High risk of being affected by AI and automation based on employee, industry, and AI adoption-related factors.

Built with Streamlit and a LightGBM Classifier.

## 🚀 Features

* Simple and user-friendly interface for entering job and employee details.
* Predicts AI-driven layoff risk as Low, Medium, or High.
* Supports inputs such as:

  * Age
  * Education Level
  * Years of Experience
  * Industry
  * Company Size
  * Job Level
  * Routine Task Percentage
  * Creativity Requirement
  * Human Interaction Level
  * AI Adoption Level
  * Number of AI Tools Used
  * AI Usage Hours per Week
  * Tasks Automated Percentage
  * AI Training Hours
* Instant predictions powered by a trained LightGBM model.
* Clean and responsive UI built entirely with Streamlit.

## 🛠️ Tech Stack

* Python
* Streamlit – Web application framework
* LightGBM – Machine Learning Classification Model
* scikit-learn – Data preprocessing and model evaluation
* pandas – Data handling and preprocessing
* joblib – Model serialization and loading

## 📊 Model Performance

* Model: LightGBM Classifier
* Accuracy: 93.92%
* Multi-Class Classification:

  * Low Layoff Risk
  * Medium Layoff Risk
  * High Layoff Risk
* Evaluated using:

  * Accuracy Score
  * Precision
  * Recall
  * F1-Score
  * Confusion Matrix

## 📦 Project Structure

```
AI-job-layoff-risk-predictor-System/
├── app.py                           # Main Streamlit application
├── ai_layoff_risk_model.pkl         # Trained LightGBM model
├── .streamlit/
│   └── config.toml                  # Streamlit theme configuration
├── requirements.txt                 # Project dependencies
└── README.md
```

## ⚙️ Installation & Setup

### Clone the Repository

```bash
git clone https://github.com/iqrabb/AI-job-layoff-risk-predictor-System.git
cd AI-job-layoff-risk-predictor-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

Open the local URL shown in your terminal (usually http://localhost:8501).

## 📋 How It Works

1. Enter job and employee-related information.
2. Provide AI adoption and automation-related details.
3. Click the **Predict Layoff Risk** button.
4. The model analyzes the inputs and predicts whether the role is at:

   * Low Risk
   * Medium Risk
   * High Risk
5. Receive an instant AI-driven layoff risk prediction.

## 🎯 Use Cases

* Workforce risk assessment.
* AI adoption impact analysis.
* Educational and portfolio projects.
* Demonstrating machine learning deployment using Streamlit and LightGBM.
* Exploring the future impact of AI on jobs and industries.

## 🙋 Author

**Iqra BiBi**
AI & Machine Learning Learner | Data Science Student | Building Real-World ML Projects

## About

AI Job Layoff Risk Predictor is a machine learning web application that predicts the likelihood of job roles being affected by AI and automation using a LightGBM Classifier. The model has been trained on a dataset of 20,000 records and optimized for high predictive performance and deployment efficiency.
