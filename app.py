import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('fraud_model.pkl')

FRAUD_SAMPLE = {
    'Time': 406.0, 'V1': -2.312227, 'V2': 1.951992,
    'V3': -1.609851, 'V4': 3.997906, 'V5': -0.522188,
    'V6': -1.426545, 'V7': -2.537387, 'V8': 1.391657,
    'V9': -2.770089, 'V10': -2.772272, 'V11': 3.202033,
    'V12': -2.899907, 'V13': -0.595222, 'V14': -4.289254,
    'V15': 0.389724, 'V16': -1.140747, 'V17': -2.830056,
    'V18': -0.016822, 'V19': 0.416956, 'V20': 0.126911,
    'V21': 0.517232, 'V22': -0.035049, 'V23': -0.465211,
    'V24': 0.320198, 'V25': 0.044519, 'V26': 0.177840,
    'V27': 0.261145, 'V28': -0.143276, 'Amount': 0.0
}

NORMAL_SAMPLE = {
    'Time': 0.0, 'V1': -1.359807, 'V2': -0.072781,
    'V3': 2.536347, 'V4': 1.378155, 'V5': -0.338321,
    'V6': 0.462388, 'V7': 0.239599, 'V8': 0.098698,
    'V9': 0.363787, 'V10': 0.090794, 'V11': -0.551600,
    'V12': -0.617801, 'V13': -0.991390, 'V14': -0.311169,
    'V15': 1.468177, 'V16': -0.470401, 'V17': 0.207971,
    'V18': 0.025791, 'V19': 0.403993, 'V20': 0.251412,
    'V21': -0.018307, 'V22': 0.277838, 'V23': -0.110474,
    'V24': 0.066928, 'V25': 0.128539, 'V26': -0.189115,
    'V27': 0.133558, 'V28': -0.021053, 'Amount': 149.62
}

# Page config
st.set_page_config(
    page_title="Fraud Detection System",
    page_icon="💳",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { padding: 2rem; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
    }
    .metric-card {
        background-color: #1e1e2e;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    .header-text {
        font-size: 14px;
        color: #888;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("💳 Credit Card Fraud Detection System")
st.markdown("##### Enterprise-grade real-time fraud detection powered by Machine Learning & Explainable AI")
st.markdown("---")

# Stats bar
c1, c2, c3, c4 = st.columns(4)
c1.metric("Model", "Random Forest")
c2.metric("Recall Score", "83%")
c3.metric("Dataset Size", "284,807")
c4.metric("Fraud Rate", "0.17%")

st.markdown("---")

# ================================
# SECTION 1 — Single Transaction
# ================================
st.header("🔍 Single Transaction Analysis")
st.markdown("Test individual transactions using pre-loaded samples or custom values.")

col1, col2 = st.columns(2)
if col1.button("⚠️ Load Fraud Transaction Sample"):
    st.session_state.sample = FRAUD_SAMPLE
if col2.button("✅ Load Normal Transaction Sample"):
    st.session_state.sample = NORMAL_SAMPLE

sample = st.session_state.get('sample', NORMAL_SAMPLE)

with st.expander("⚙️ View & Edit Transaction Details"):
    ec1, ec2 = st.columns(2)
    amount = ec1.number_input("Transaction Amount ($)", value=float(sample['Amount']))
    time = ec2.number_input("Transaction Time (seconds)", value=float(sample['Time']))

    v_features = {}
    cols = st.columns(4)
    for i in range(1, 29):
        v_features[f'V{i}'] = cols[(i-1) % 4].number_input(
            f"V{i}", value=float(sample[f'V{i}']), format="%.4f"
        )

if st.button("🔍 Analyze Transaction", type="primary"):
    columns = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
    input_data = {'Time': time, 'Amount': amount}
    input_data.update(v_features)
    input_df = pd.DataFrame([input_data])[columns]

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    st.markdown("#### Analysis Result")
    if probability[1] >= 0.7:
        st.error("🚨 HIGH RISK — FRAUDULENT TRANSACTION DETECTED")
    elif probability[1] >= 0.3:
        st.warning("⚠️ MEDIUM RISK — SUSPICIOUS TRANSACTION")
    else:
        st.success("✅ LOW RISK — LEGITIMATE TRANSACTION")

    r1, r2, r3 = st.columns(3)
    r1.metric("Normal Probability", f"{probability[0]*100:.2f}%")
    r2.metric("Fraud Probability", f"{probability[1]*100:.2f}%")
    r3.metric("Risk Level",
              "High 🔴" if probability[1] >= 0.7
              else "Medium 🟡" if probability[1] >= 0.3
              else "Low 🟢")

st.markdown("---")

# ================================
# SECTION 2 — Bulk CSV Upload
# ================================
st.header("📂 Batch Transaction Analysis")
st.markdown("Upload a CSV file to analyze multiple transactions simultaneously.")

uploaded_file = st.file_uploader("Upload Transactions CSV", type=['csv'])

if uploaded_file is not None:
    df_upload = pd.read_csv(uploaded_file)

    if 'Class' in df_upload.columns:
        df_upload = df_upload.drop('Class', axis=1)

    columns = ['Time'] + [f'V{i}' for i in range(1, 29)] + ['Amount']
    input_df = df_upload[columns]

    predictions = model.predict(input_df)
    probabilities = model.predict_proba(input_df)

    df_upload['Result'] = pd.Series(predictions).map({
        0: '✅ Legitimate',
        1: '🚨 Fraudulent'
    })
    df_upload['Fraud Probability %'] = (probabilities[:, 1] * 100).round(2)

    df_upload['Risk Level'] = df_upload['Fraud Probability %'].apply(
        lambda x: '🔴 High' if x >= 70
        else ('🟡 Medium' if x >= 30
              else ('🟢 Low' if x > 0
                    else '⚪ Safe'))
    )

    st.markdown("### 📊 Analysis Summary")
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Total Transactions", len(df_upload))
    s2.metric("Fraudulent", int(predictions.sum()))
    s3.metric("Legitimate", int(len(predictions) - predictions.sum()))
    s4.metric("Fraud Rate", f"{(predictions.sum()/len(predictions)*100):.2f}%")

    st.markdown("### 📋 Detailed Results")
    st.dataframe(
        df_upload[['Amount', 'Result', 'Fraud Probability %', 'Risk Level']],
        use_container_width=True
    )

    csv = df_upload.to_csv(index=False)
    st.download_button(
        "⬇️ Download Full Report",
        csv,
        "fraud_detection_report.csv",
        "text/csv",
        type="primary"
    )

st.markdown("---")
st.markdown(
    "Developed by **Vidhya Majee** | "
    "[GitHub](https://github.com/Vidhya-Majee) | "
    "[LinkedIn](https://linkedin.com/in/vidhya-majee-7807b9321)"
)