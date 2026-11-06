# AI Job Impact & Layoff Risk Predictor

A Streamlit portfolio application that explores how job characteristics and reported AI/automation exposure relate to a model-generated Low, Medium, or High risk category.

The app collects role, company, experience, task, and AI-adoption inputs, then passes the encoded features to a saved machine-learning estimator.

> **Important:** This is an experimental educational project. Its output is not a forecast of actual layoffs, a reliable assessment of an individual's job security, or a basis for employment decisions.

## Features

- Streamlit interface for entering role and workplace characteristics.
- Inputs for education, experience, job level, company size, industry, and job role.
- Inputs for routine tasks, creativity, human interaction, AI adoption, AI-tool usage, automation, and AI training.
- Encodes categorical inputs and sends the resulting feature row to the saved model.
- Displays one of three model output categories: Low, Medium, or High.

## Technology

- Python
- Streamlit
- Pandas
- Joblib for loading the saved estimator
- scikit-learn, LightGBM, and NumPy are listed in the project dependencies

The app code loads a serialized estimator from `AI_Impact_on_Jobs_Prediction_System.pkl`. The exact estimator class and its training configuration are not established by the application code alone, so this README does not make an unverified algorithm claim.

## How it works

1. The user enters role and AI-exposure details in the Streamlit interface.
2. Education and job-level values are mapped to numeric categories.
3. Industry and job-role values are converted into one-hot-style feature columns.
4. The app creates a single-row Pandas DataFrame.
5. The saved estimator predicts a class.
6. The app maps class `0` to Low Risk, `1` to Medium Risk, and other outputs to High Risk.

## Run locally

### 1. Clone the repository

```bash
git clone https://github.com/iqrabb/AI-job-layoff-risk-predictor-System.git
cd AI-job-layoff-risk-predictor-System
```

### 2. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the application

```bash
streamlit run app.py
```

Open the local URL printed by Streamlit (usually http://localhost:8501).

The app expects `AI_Impact_on_Jobs_Prediction_System.pkl` in the repository root. Do not load pickle/joblib artifacts from untrusted sources; deserialization can execute arbitrary code.

## Input categories

| Area | Inputs |
|---|---|
| Role profile | Age, education, years of experience, job level, company size |
| Work context | Industry, job role |
| Task characteristics | Routine task percentage, creativity requirement, human interaction level |
| AI exposure | AI adoption level, number of AI tools, AI usage hours, tasks automated percentage, AI training hours |

## Repository contents

- `app.py` — Streamlit interface, feature encoding, and prediction logic.
- `AI_Impact_on_Jobs_Prediction_System.pkl` — serialized estimator loaded by the app.
- `requirements.txt` — Python dependencies.
- `README.md` — project documentation.

## Evaluation and reproducibility

The repository currently does not include the training dataset or a training/evaluation script. The accuracy figure and training-data-size claims from the previous README have therefore been removed because they cannot be independently verified from the committed files.

To make this project reproducible, add the dataset source and license, a training pipeline, the exact feature schema, a documented split strategy, and held-out evaluation results (including per-class precision, recall, F1-score, and a confusion matrix).

## Limitations and responsible interpretation

- The model output reflects patterns learned from its training data; it does not establish that a particular job will or will not be eliminated.
- AI adoption, task automation, and employment outcomes vary by organization, region, time, and many factors not represented by this interface.
- The repository does not provide evidence of calibration, external validation, or real-world predictive performance.
- Do not use this application for hiring, firing, promotion, compensation, or other consequential employment decisions.

---

Developed as an educational demonstration of tabular feature engineering and machine-learning inference with Streamlit.
