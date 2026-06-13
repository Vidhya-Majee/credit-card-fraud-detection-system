# 💳 Credit Card Fraud Detection System

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)

> Enterprise-grade real-time fraud detection system built with Machine Learning & Explainable AI (SHAP), deployed on Streamlit Cloud.

## 🔗 Live Demo
👉 **[Click here to try the app]()** ← Streamlit link baad mein add karna

---

## 📌 Problem Statement
Credit card fraud costs the global economy **$32 billion annually**.
Traditional rule-based systems fail to detect complex fraud patterns.
This ML system detects fraudulent transactions with **96.54% detection rate**
using Random Forest + SHAP Explainability.

---

## 🎯 Key Results

| Metric | Score |
|--------|-------|
| Fraud Detection Rate | **96.54%** |
| Recall | **83%** |
| Precision | **83%** |
| F1-Score | **83%** |
| Dataset Size | 2,84,807 transactions |
| Fraud Rate | 0.17% (highly imbalanced) |

---

## 📊 Complete Model Performance Report

### Dataset Overview
| Property | Value |
|----------|-------|
| Total Transactions | 2,84,807 |
| Normal Transactions | 2,84,315 (99.83%) |
| Fraud Transactions | 492 (0.17%) |
| Train Set | 2,27,845 (80%) |
| Test Set | 56,962 (20%) |

### ⚖️ SMOTE — Class Imbalance Handling
| | Before SMOTE | After SMOTE |
|--|-------------|------------|
| Normal | 2,27,451 | 2,27,451 |
| Fraud | 394 | 2,27,451 ✅ |
| Total | 2,27,845 | 4,54,902 |

### 🏆 Model Comparison

| Model | Precision | Recall | F1-Score | Selected |
|-------|-----------|--------|----------|----------|
| Logistic Regression | 12% | 90% | 20% | ❌ |
| **Random Forest** | **83%** | **83%** | **83%** | ✅ |
| XGBoost | 79% | 85% | 82% | ❌ |

### 🧪 Final Testing Results
| Test | Value |
|------|-------|
| Total Fraud in Dataset | 492 |
| Fraud Detected | 475 |
| **Detection Rate** | **96.54%** 🔥 |

---

## 🖼️ Screenshots

### SHAP Summary Plot
![SHAP Summary](shap_summary.png)

### SHAP Feature Importance
![SHAP Bar](shap_bar.png)

### Class Imbalance
![Class Imbalance](class_imbalance.png)

---

## ⚙️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.8+ |
| ML Models | Random Forest, XGBoost, Logistic Regression |
| Imbalance Handling | SMOTE |
| Explainability | SHAP |
| Web App | Streamlit |
| Deployment | Streamlit Cloud |

---

## 🏗️ Project Structure
credit-fraud-detector/

│

├── 01_EDA.ipynb          # Exploratory Data Analysis

├── 02_model.ipynb        # Model Training & Evaluation

├── 03_shap.ipynb         # SHAP Explainability

├── app.py                # Streamlit Dashboard

├── requirements.txt      # Dependencies

└── README.md             # Documentation

---

## 🔍 SHAP Insights

| Rank | Feature | Insight |
|------|---------|---------|
| 1 | V14 | Low V14 = Strong fraud signal 🚨 |
| 2 | V4 | Low V4 = Fraud indicator |
| 3 | V12 | Low V12 = Fraud indicator |
| 4 | V11 | High V11 = Fraud indicator |

---

## 🚀 Run Locally

```bash
# Clone repo
git clone https://github.com/Vidhya-Majee/credit-fraud-detector.git
cd credit-fraud-detector

# Install dependencies
pip install -r requirements.txt

# Download dataset from Kaggle
# Place creditcard.csv in project folder

# Run notebooks in order
# 01_EDA.ipynb → 02_model.ipynb → 03_shap.ipynb

# Run app
streamlit run app.py
```

---

## 📂 Dataset
- **Source:** [Kaggle — Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- **Size:** 2,84,807 transactions
- **Note:** Dataset not included — download from Kaggle

---

## 👩‍💻 About Me

**Vidhya Majee** — BCA Student | Data Science & Full Stack Developer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/vidhya-majee-7807b9321)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=for-the-badge&logo=github)](https://github.com/Vidhya-Majee)

---
⭐ If you found this helpful, please star this repo!