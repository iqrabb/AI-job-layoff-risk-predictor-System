import streamlit as st
import pandas as pd
import joblib

# ===============================
# Page Configuration
# ===============================
st.set_page_config(
    page_title="AI Job Layoff Risk Predictor System",
    page_icon="🧭",
    layout="centered"
)

# ===============================
# Load Model
# ===============================
model = joblib.load("AI_Impact_on_Jobs_Prediction_System.pkl")

# ===============================
# Small readability fixes (captions + card borders) + forced brand color
# ===============================
st.markdown("""
<style>
/* Captions / subtext — darker and bolder everywhere (header intro + footer) */
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] * {
    color: #2E3A55 !important;
    font-weight: 600 !important;
    font-size: 14.5px !important;
}

/* Card borders */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border: 1px solid #B2DFDB !important;
    box-shadow: 0 2px 10px rgba(31, 71, 188, 0.08);
}

/* Force navy blue on sliders (track fill + thumb), regardless of theme file */
div[data-testid="stSlider"] div[role="slider"] {
    background-color: #004D40 !important;
    border-color: #004D40 !important;
}
div[data-testid="stSlider"] > div > div > div > div {
    background-color: #004D40 !important;
}

/* Force navy blue on the primary button */
button[kind="primary"], button[kind="primaryFormSubmit"] {
    background-color: #004D40 !important;
    border-color: #004D40 !important;
}
button[kind="primary"]:hover, button[kind="primaryFormSubmit"]:hover {
    background-color: #00332B !important;
    border-color: #00332B !important;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# Header
# ===============================
st.markdown("""
<div style="
    background: linear-gradient(90deg, #004D40, #00897B);
    padding: 30px 34px;
    border-radius: 16px;
    margin-bottom: 26px;
    box-shadow: 0 6px 18px rgba(31, 71, 188, 0.25);
">
    <h1 style="color:#FFFFFF; margin:0; font-size:28px; font-weight:800;">🧭 AI Job Layoff Risk Predictor</h1>
    <p style="color:#E4EBFB; margin-top:8px; margin-bottom:0; font-size:15px; font-weight:600;">
        Enter details about any job role below, and this tool predicts whether that role's risk of
        being affected by AI and automation is Low, Medium, or High.
    </p>
</div>
""", unsafe_allow_html=True)

# ===============================
# Section 1: Role Profile
# ===============================
profile_section = st.container(border=True)
with profile_section:
    st.markdown("""
    <div style="border-left:4px solid #004D40; padding-left:12px; margin-bottom:2px;">
        <span style="background:#E0F2F1; padding:6px 9px; border-radius:8px; font-size:16px;">🧑‍💼</span>
        <span style="color:#004D40; font-weight:700; font-size:19px; margin-left:6px;">Role Profile</span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Basic details about the person and the company.")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 18, 65, 30)
        education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])
        experience = st.slider("Years of Experience", 0, 40, 5)
        job_level = st.selectbox("Job Level", ["Entry", "Mid", "Senior"])

    with col2:
        company_size = st.slider("Company Size (employees)", 10, 10000, 500)
        industry = st.selectbox(
            "Industry",
            ["Education", "Finance", "Healthcare", "IT", "Logistics", "Manufacturing", "Retail", "Telecom"]
        )
        job_role = st.selectbox(
            "Job Role",
            [
                "Academic Coordinator", "Accountant", "Auditor", "Data Analyst", "Dispatcher",
                "Financial Analyst", "Health Analyst", "Inventory Analyst", "ML Engineer",
                "Medical Assistant", "Network Engineer", "Nurse", "Operations Analyst", "Operator",
                "Production Supervisor", "Quality Engineer", "Research Assistant", "Sales Associate",
                "Software Engineer", "Store Manager", "Supply Chain Analyst", "Support Specialist",
                "Teacher", "Warehouse Manager"
            ]
        )

st.write("")

# ===============================
# Section 2: AI Exposure
# ===============================
ai_section = st.container(border=True)
with ai_section:
    st.markdown("""
    <div style="border-left:4px solid #004D40; padding-left:12px; margin-bottom:2px;">
        <span style="background:#E0F2F1; padding:6px 9px; border-radius:8px; font-size:16px;">⚙️</span>
        <span style="color:#004D40; font-weight:700; font-size:19px; margin-left:6px;">AI Exposure</span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("How much AI and automation are already part of this role.")

    col3, col4 = st.columns(2)

    with col3:
        routine = st.slider("Routine Task Percentage", 0, 100, 50)
        creativity = st.slider("Creativity Requirement", 0, 100, 50)
        interaction = st.slider("Human Interaction Level", 0, 100, 50)
        ai_adoption = st.slider("AI Adoption Level", 0, 100, 50)

    with col4:
        ai_tools = st.slider("Number of AI Tools Used", 0, 20, 5)
        ai_usage = st.slider("AI Usage Hours Per Week", 0, 80, 20)
        automated = st.slider("Tasks Automated Percentage", 0, 100, 50)
        training = st.slider("AI Training Hours", 0, 500, 50)

st.write("")

# ===============================
# Encode + Predict
# ===============================
education_map = {"High School": 0, "Bachelor's": 1, "Master's": 2, "PhD": 3}
job_level_map = {"Entry": 0, "Mid": 1, "Senior": 2}

if st.button("🔍 Predict Layoff Risk", use_container_width=True, type="primary"):

    input_data = {
        "Age": age,
        "Education_Level": education_map[education],
        "Years_of_Experience": experience,
        "Company_Size": company_size,
        "Job_Level": job_level_map[job_level],
        "Routine_Task_Percentage": routine,
        "Creativity_Requirement": creativity,
        "Human_Interaction_Level": interaction,
        "AI_Adoption_Level": ai_adoption,
        "Number_of_AI_Tools_Used": ai_tools,
        "AI_Usage_Hours_Per_Week": ai_usage,
        "Tasks_Automated_Percentage": automated,
        "AI_Training_Hours": training,

        "Industry_Finance": 0, "Industry_Healthcare": 0, "Industry_IT": 0,
        "Industry_Logistics": 0, "Industry_Manufacturing": 0,
        "Industry_Retail": 0, "Industry_Telecom": 0,

        "Job_Role_Accountant": 0, "Job_Role_Auditor": 0, "Job_Role_Data Analyst": 0,
        "Job_Role_Dispatcher": 0, "Job_Role_Financial Analyst": 0, "Job_Role_Health Analyst": 0,
        "Job_Role_Inventory Analyst": 0, "Job_Role_ML Engineer": 0, "Job_Role_Medical Assistant": 0,
        "Job_Role_Network Engineer": 0, "Job_Role_Nurse": 0, "Job_Role_Operations Analyst": 0,
        "Job_Role_Operator": 0, "Job_Role_Production Supervisor": 0, "Job_Role_Quality Engineer": 0,
        "Job_Role_Research Assistant": 0, "Job_Role_Sales Associate": 0, "Job_Role_Software Engineer": 0,
        "Job_Role_Store Manager": 0, "Job_Role_Supply Chain Analyst": 0, "Job_Role_Support Specialist": 0,
        "Job_Role_Teacher": 0, "Job_Role_Warehouse Manager": 0
    }

    if industry != "Education":
        input_data[f"Industry_{industry}"] = 1

    if job_role != "Academic Coordinator":
        input_data[f"Job_Role_{job_role}"] = 1

    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    result_section = st.container(border=True)
    with result_section:
        st.markdown("""
        <div style="border-left:4px solid #004D40; padding-left:12px; margin-bottom:10px;">
            <span style="background:#E0F2F1; padding:6px 9px; border-radius:8px; font-size:16px;">📊</span>
            <span style="color:#004D40; font-weight:700; font-size:19px; margin-left:6px;">Result</span>
        </div>
        """, unsafe_allow_html=True)

        if prediction == 0:
            st.success("🟢 **Low Risk** — This role is fairly safe for now. Keep learning new tools as they come up.")
        elif prediction == 1:
            st.warning("🟡 **Medium Risk** — Some tasks in this role could get automated. A bit of upskilling will help.")
        else:
            st.error("🔴 **High Risk** — Most tasks in this role overlap with what AI can already do. Building AI-related skills is worth prioritizing.")

# ===============================
# Footer
# ===============================
st.write("")
st.markdown("""
<div style="
    background:#00332B;
    padding:20px;
    border-radius:16px;
    text-align:center;
    margin-top:10px;
">
    <p style="color:#FFFFFF; margin:0; font-weight:700; font-size:15px;">Developed by Iqra ❤️</p>
    <p style="color:#C7D4F0; margin:2px 0 0 0; font-size:13px; font-weight:600;">AI & Machine Learning Learner | Turning Data into Real-World Solutions.</p>
</div>
""", unsafe_allow_html=True)
