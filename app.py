import streamlit as st
import pickle
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Placement Prediction Dashboard",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
/* Overall Font */
html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
    font-size: 18px;
}

/* Subheaders */
h1 {
    font-size: 45px !important;
}

h2 {
    font-size: 34px !important;
}

h3 {
    font-size: 28px !important;
}

/* Normal text */
p, li, span, div {
    font-size: 18px !important;
}

/* Sidebar */
section[data-testid="stSidebar"] * {
    font-size: 18px !important;
}

/* Number input labels */
div[data-testid="stNumberInput"] label {
    font-size: 18px !important;
    font-weight: 700 !important;
}

/* Number input values */
div[data-testid="stNumberInput"] input {
    font-size: 18px !important;
}

/* Button */
div[data-testid="stButton"] > button {
    font-size: 20px !important;
}

/* Main background */
.stApp{
    background: linear-gradient(135deg,#EEF4FF,#FFFFFF);
}

/* Hide Streamlit menu & footer */
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* Title */
.main-title{
    font-size:100px;
    font-weight:800;
    text-align:center;
    color:#1E3A8A;
    margin-top:10px;
}

.sub-title{
    text-align:center;
    color:#64748B;
    font-size:22px;
    margin-bottom:30px;
}

/* Input boxes */
.stNumberInput, .stSelectbox{
    background:white;
    border-radius:10px;
    padding:6px;
}

/* Button */
div[data-testid="stButton"] > button{
    width:100%;
    height:55px;
    background:linear-gradient(to right,#2563EB,#7C3AED);
    color:white;
    font-size:20px;
    font-weight:bold;
    border:none;
    border-radius:10px;
}

div[data-testid="stButton"] > button:hover{
    background:linear-gradient(to right,#1D4ED8,#6D28D9);
    transform:scale(1.02);
    transition:0.3s;
}
html, body, [class*="css"]{
    font-family:'Segoe UI',sans-serif;
    font-size:18px;
}
label{
    color:#1E293B !important;
    font-size:18px !important;
    font-weight:700 !important;
}
input{
    font-size:18px !important;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class='main-title'>
🎓 Placement Prediction Dashboard
</div>

<div class='sub-title'>
Predict whether a student is likely to be placed using Machine Learning
</div>
""", unsafe_allow_html=True)
# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.title("🎓 Placement Predictor")

    st.markdown("---")

    st.info("""
### 📌 About

This application predicts whether a student is likely to be placed based on:

- 🎯 CGPA
- 💼 Internships
- 📂 Projects
- 💻 Coding Skills
- 🗣 Communication Skills
- 📝 Aptitude Score
- 🤝 Soft Skills
- 📜 Certifications
- ⚠️ Backlogs
""")

    st.markdown("---")

    st.markdown("---")

    st.caption("Developed using  Python, Streamlit & Scikit-Learn")

# -----------------------------
# LOAD PICKLE MODEL
# -----------------------------
with open("placement_model.pkl", "rb") as file:
    model = pickle.load(file)


# -----------------------------
# USER INPUTS
# -----------------------------

# ---------------- INPUT SECTION ---------------- #

st.subheader("📋 Enter Student Details")

col1, col2 = st.columns(2)

with col1:

    cgpa = st.number_input(
        "🎓 CGPA",
        min_value=0.0,
        max_value=10.0,
        value=0.0,
        step=0.01
    )

    internships = st.number_input(
        "💼 Internships",
        min_value=0,
        value=0
    )

    projects = st.number_input(
        "📂 Projects",
        min_value=0,
        value=0
    )

    coding = st.number_input(
        "💻 Coding Skills",
        min_value=0,
        max_value=100,
        value=0
    )

    communication = st.number_input(
        "🗣 Communication Skills",
        min_value=0,
        max_value=100,
        value=0
    )

with col2:

    aptitude = st.number_input(
        "📝 Aptitude Test Score",
        min_value=0,
        max_value=100,
        value=0
    )

    soft = st.number_input(
        "🤝 Soft Skills Rating",
        min_value=1,
        max_value=10,
        value=1
    )

    certifications = st.number_input(
        "📜 Certifications",
        min_value=0,
        value=0
    )

    backlogs = st.number_input(
        "⚠️ Backlogs",
        min_value=0,
        value=0
    )

# -----------------------------
# PREDICTION
# -----------------------------

if st.button("🚀 Predict Placement"):

    input_data = pd.DataFrame({
        "CGPA":[cgpa],
        "Internships":[internships],
        "Projects":[projects],
        "Coding_Skills":[coding],
        "Communication_Skills":[communication],
        "Aptitude_Test_Score":[aptitude],
        "Soft_Skills_Rating":[soft],
        "Certifications":[certifications],
        "Backlogs":[backlogs]
    }) 
    prediction = model.predict(input_data)[0]

    st.markdown("---")

    if prediction == 1:
        st.success("🎉 Congratulations! You are likely to get placed")

        st.markdown("""
### ✅ Placement Prediction

The student has a **HIGH chance of getting placed.**

Keep up the excellent performance!
""")

    else:

        st.error("You are not likely to placed")

        st.markdown("""
### Improvement Required

The student currently has a **LOW chance of placement.**

📌 Focus on:
- 💻 Coding Skills
- 📝 Aptitude
- 🗣 Communication
- 📂 Projects
""")