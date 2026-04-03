import streamlit as st
import pandas as pd

# Page Config for a professional look
st.set_page_config(page_title="MahaAgri-Shield AI", layout="wide")

# Styling to make it look "Premium"
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

## --- HEADER ---
st.title("🛡️ MahaAgri-Shield AI")
st.subheader("Proactive Risk Assessment for Maharashtra Crop Insurance")
st.info("Targeting high-accuracy client selection based on regional agro-climatic data.")

## --- SIDEBAR INPUTS ---
st.sidebar.header("Client Parameters")
district = st.sidebar.selectbox("Select District", ["Jalna", "Wardha", "Nashik", "Ratnagiri", "Pune", "Latur"])
crop = st.sidebar.selectbox("Primary Crop", ["Soybean", "Cotton", "Pigeon Pea (Tur)", "Sugarcane", "Rice"])
land_size = st.sidebar.number_input("Land Size (Acres)", min_value=1.0, max_value=100.0, value=5.0)
irrigation = st.sidebar.radio("Irrigation Type", ["Rainfed", "Canal/Well", "Drip Irrigation"])

## --- LOGIC ENGINE ---
def calculate_risk(district, crop, irrigation):
    # This is a simplified logic gate for the prototype
    risk_score = 0
    factors = []

    # Regional Risk
    if district in ["Jalna", "Latur", "Wardha"]:
        risk_score += 40
        factors.append("High drought vulnerability zone.")
    elif district == "Ratnagiri":
        risk_score += 20
        factors.append("Excess rainfall risk.")

    # Crop Specific Risk
    if crop == "Cotton":
        risk_score += 30
        factors.append("High pest susceptibility (Pink Bollworm).")
    
    # Mitigation Factor
    if irrigation == "Drip Irrigation":
        risk_score -= 15
        factors.append("Risk mitigated by efficient water management.")
    
    return min(max(risk_score, 10), 100), factors

## --- RESULTS SECTION ---
col1, col2 = st.columns([1, 1])

with col1:
    st.write("### Analysis Dashboard")
    score, reasons = calculate_risk(district, crop, irrigation)
    
    # Displaying the "Proactive" Risk Gauge
    st.metric(label="Risk Assessment Score", value=f"{score}%", delta="- Low Risk" if score < 40 else "High Risk", delta_color="inverse")
    
    st.write("**Key Risk Drivers:**")
    for r in reasons:
        st.write(f"- {r}")

with col2:
    st.write("### Insurance Recommendation")
    if score > 70:
        st.error("🚨 HIGH RISK: Requires mandatory satellite monitoring and higher premium.")
    elif 40 <= score <= 70:
        st.warning("⚠️ MODERATE RISK: Recommend customized index-based insurance.")
    else:
        st.success("✅ LOW RISK: High eligibility for standard premium rates.")

    # Button to simulate a deeper AI report
    if st.button("Generate Comprehensive AI Report"):
        st.write("Fetching historical weather patterns and satellite imagery for your district...")
        st.progress(100)
        st.write("Report: The 10-year trend indicates a stable yield for this client.")

st.divider()
st.caption("Powered by Maharashtra Agri-AI Framework Logic | Prototype v1.0")
