# app.py
import streamlit as st
from prompts import build_prompt
from question_engine import generate_response  # Uses static fallback

st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")
st.markdown("<h1>TalentScout Hiring Assistant</h1>", unsafe_allow_html=True)

if st.sidebar.button("Reset App"):
    st.session_state.clear()
    st.experimental_rerun()


if "stage" not in st.session_state:
    st.session_state.stage = "form"
if "questions" not in st.session_state:
    st.session_state.questions = {}


if st.session_state.stage == "form":
    with st.form("candidate_form"):
        name = st.text_input("Full Name", key="name_input")
        email = st.text_input("Email ID", key="email_input")
        phone = st.text_input("Phone Number", key="phone_input")
        experience = st.number_input("Years of Experience", min_value=0, max_value=50, key="exp_input")
        position = st.text_input("Desired Position(s)", key="position_input")
        location = st.text_input("Current Location", key="location_input")
        tech_stack = st.text_input("Tech Stack (comma-separated)", key="tech_stack_input")
        submitted = st.form_submit_button("Continue")

    if submitted:
        st.session_state.name = name
        st.session_state.email = email
        st.session_state.phone = phone
        st.session_state.experience = experience
        st.session_state.position = position
        st.session_state.location = location
        st.session_state.tech_stack = tech_stack
        st.session_state.stage = "questions"
        st.rerun()


elif st.session_state.stage == "questions":
    st.write(f"Hi {st.session_state.name}, here are your technical questions:")
    st.header("Generated Questions")

    tech_list = [tech.strip() for tech in st.session_state.tech_stack.split(",") if tech.strip()]

    if not st.session_state.questions:
        for tech in tech_list:
            prompt = f"{st.session_state.position} interview questions for {tech}"
            questions = generate_response(prompt)
            st.session_state.questions[tech] = f"Questions for {tech}:\n\n{questions}"

    for tech, questions in st.session_state.questions.items():
        st.subheader(tech)
        st.code(questions, language="markdown")

    if st.button("Finish"):
        st.success("Thank you! Your response has been recorded.")
        st.session_state.stage = "done"


elif st.session_state.stage == "done":
    if st.button("Start Over"):
        st.session_state.clear()
        st.experimental_rerun()
