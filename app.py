import streamlit as st
import time

from math_test import run_math_test
from stroop_test import run_stroop_test
from mental_rotation_test import run_mental_rotation_test

st.set_page_config(page_title="Cognitive Assessment Tool", layout="centered")

# =====================================================
# SESSION STATE INITIALIZATION
# =====================================================
if "current_stage" not in st.session_state:
    st.session_state.current_stage = "consent"

# =====================================================
# 1️⃣ CONSENT + DEMOGRAPHICS PAGE
# =====================================================
if st.session_state.current_stage == "consent":

    st.title("Cognitive Assessment Study")

    st.markdown("""
    ### Digital Consent

    - I confirm that I have passed 12th standard.
    - I confirm that I am computer literate.
    - I understand that the data collected will be used **only for academic purposes**.
    - My participation is voluntary and I may withdraw at any time.
    """)

    consent = st.checkbox("I agree to participate in this study")

    st.markdown("---")
    st.markdown("### Baseline & Demographic Information")

    name = st.text_input("Name")
    age = st.selectbox("Age Category", [
        "18-25", "26-35", "36-45", "46-55", "56+"
    ])
    gender = st.selectbox("Gender", [
        "Male", "Female", "Other"
    ])
    hometown = st.text_input("Home Town")
    current_city = st.text_input("Current City")
    mother_language = st.selectbox("Mother Language", [
        "Hindi", "English", "Bengali", "Tamil", "Telugu",
        "Marathi", "Gujarati", "Kannada", "Malayalam", "Other"
    ])
    academic = st.selectbox("Academic Qualification", [
        "Pursuing UG",
        "Pursuing PG",
        "Completed UG",
        "Completed PG"
    ])
    service = st.selectbox("Service Status", [
        "Employed",
        "Not Employed",
        "Retired"
    ])
    handedness = st.selectbox("Handedness", [
        "Right", "Left", "Ambidextrous"
    ])
    device = st.selectbox("Device Used", [
        "Laptop", "Desktop", "Mobile", "Tablet"
    ])
    vision = st.selectbox("Vision Status", [
        "Normal",
        "Corrected to Normal"
    ])
    prior_exposure = st.selectbox(
        "Prior exposure to any cognitive test recently?",
        ["Yes", "No"]
    )

    if st.button("Start Test"):

        if not consent:
            st.warning("You must provide consent to proceed.")
            st.stop()

        if name == "":
            st.warning("Please enter your name.")
            st.stop()

        st.session_state.demographics = {
            "name": name,
            "age": age,
            "gender": gender,
            "hometown": hometown,
            "current_city": current_city,
            "mother_language": mother_language,
            "academic": academic,
            "service": service,
            "handedness": handedness,
            "device": device,
            "vision": vision,
            "prior_exposure": prior_exposure
        }

        st.session_state.current_stage = "instructions"
        st.session_state.instruction_start = time.time()
        st.rerun()


# =====================================================
# 2️⃣ INSTRUCTION SCREEN (NON-BLOCKING 5 SECONDS)
# =====================================================
elif st.session_state.current_stage == "instructions":

    st.title("Instructions")

    st.markdown("""
    You will complete **three cognitive tasks**:

    1. **Math Speed Test**
       - Solve arithmetic questions quickly and accurately.

    2. **Stroop Test**
       - Identify the color of the word, not the word itself.

    3. **Mental Rotation Task**
       - Select the correctly rotated image.

    Please respond as quickly and accurately as possible.
    """)

    st.info("The test will begin shortly...")

    if time.time() - st.session_state.instruction_start > 5:
        st.session_state.current_stage = "math"
        del st.session_state.instruction_start
        st.rerun()


# =====================================================
# 3️⃣ MATH TEST
# =====================================================
elif st.session_state.current_stage == "math":
    run_math_test()


# =====================================================
# 4️⃣ STROOP TEST
# =====================================================
elif st.session_state.current_stage == "stroop":
    run_stroop_test()


# =====================================================
# 5️⃣ MENTAL ROTATION TEST
# =====================================================
elif st.session_state.current_stage == "mental":
    run_mental_rotation_test()


# =====================================================
# 6️⃣ FINAL THANK YOU SCREEN
# =====================================================
elif st.session_state.current_stage == "final":

    st.title("Thank You for Participating!")

    st.markdown("""
    Your participation is greatly appreciated.

    The results from each test were displayed after completion.

    This data will be used strictly for academic purposes.
    """)

    st.success("You may now close this window.")
