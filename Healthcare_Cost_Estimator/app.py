import streamlit as st
import pandas as pd
import joblib

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Healthcare Cost Estimator",
    page_icon="🏥",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("healthcare_cost_model.pkl")

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background-color: #F8FAFC;
}

/* Remove Streamlit Header Background */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Main Title */
.main-title {
    font-size: 48px;
    font-weight: 800;
    color: #1E3A8A;
    margin-bottom: 0;
}

.sub-title {
    font-size: 20px;
    color: #475569;
}

/* Metric Cards */
[data-testid="metric-container"] {
    background-color: white;
    border: 1px solid #E2E8F0;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

/* Prediction Card */
.prediction-box {
    background: linear-gradient(
        135deg,
        #0891B2,
        #14B8A6
    );

    padding: 40px;
    border-radius: 20px;

    text-align: center;

    color: white;

    font-size: 34px;
    font-weight: bold;

    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
}

/* Driver Cards */
.driver-card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    border: 1px solid #E2E8F0;
    color: #1E293B;
    font-size: 20px;
    font-weight: 600;
}

/* Insight Card */
.insight-card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    border: 1px solid #E2E8F0;
    color: #1E293B;
    font-size: 18px;
    line-height: 1.8;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #020617,
        #0F172A
    );
}

[data-testid="stSidebar"] * {
    color: white;
}

.section-heading {
    color: #1E3A8A;
    font-size: 30px;
    font-weight: 700;
    margin-top: 15px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/2966/2966486.png",
    width=120
)

st.sidebar.markdown("## Patient Information")

age = st.sidebar.slider("Age", 18, 100, 30)

bmi = st.sidebar.slider("BMI", 15.0, 50.0, 25.0)

children = st.sidebar.slider("Children", 0, 5, 0)

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

smoker = st.sidebar.selectbox(
    "Smoker",
    ["No", "Yes"]
)

region = st.sidebar.selectbox(
    "Region",
    ["northeast", "northwest", "southeast", "southwest"]
)

# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<p class="main-title">🏥 Healthcare Cost Estimator</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="sub-title">AI-Powered Insurance Cost Prediction System</p>',
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================
# DASHBOARD METRICS
# ==========================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Model Accuracy",
        "90.26%"
    )

with col2:
    st.metric(
        "Best Algorithm",
        "Gradient Boosting"
    )

with col3:
    st.metric(
        "Prediction Type",
        "Regression"
    )

st.markdown("---")

# ==========================================
# INPUT PREPARATION
# ==========================================

sex_male = 1 if gender == "Male" else 0

smoker_yes = 1 if smoker == "Yes" else 0

region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

input_data = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "children": [children],
    "sex_male": [sex_male],
    "smoker_yes": [smoker_yes],
    "region_northwest": [region_northwest],
    "region_southeast": [region_southeast],
    "region_southwest": [region_southwest]
})

# ==========================================
# PREDICTION
# ==========================================

if st.button(
    "Predict Healthcare Cost",
    use_container_width=True
):

    prediction = model.predict(input_data)[0]

    st.markdown(
        f"""
        <div class="prediction-box">
        Estimated Annual Healthcare Cost
        <br><br>
        ${prediction:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

# ==========================================
# MAJOR COST DRIVERS
# ==========================================

st.markdown("---")

st.markdown(
    '<div class="section-heading">Major Cost Drivers</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="driver-card">
        🚬 <br><br>
        Smoking Status
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="driver-card">
        ⚖️ <br><br>
        BMI
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="driver-card">
        🎂 <br><br>
        Age
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# KEY FINDINGS
# ==========================================

st.markdown("---")

st.markdown(
    '<div class="section-heading">Key Findings</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="insight-card">

<b>Top Factors Affecting Healthcare Costs:</b>

<ul>
<li><b>Smoking Status</b> has the highest impact on insurance charges.</li>

<li><b>BMI</b> is strongly associated with higher healthcare expenses.</li>

<li><b>Age</b> significantly influences annual medical costs.</li>

<li><b>Children, Gender and Region</b> have comparatively lower impact on predictions.</li>

</ul>

</div>
""", unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Developed by Het Patel | AI/ML Internship Project | Gradient Boosting Regressor | Explainable AI"
)