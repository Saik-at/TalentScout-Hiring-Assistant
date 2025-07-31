import streamlit as st
from prompts import generate_prompt
from question_engine import generate_response

st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")

if "stage" not in st.session_state:
    st.session_state.stage = "form"

st.title("TalentScout Hiring Assistant")

if st.session_state.stage == "form":
    with st.form("candidate_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.slider("Years of Experience", 0, 30, 1)
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_input("List your tech stack (comma-separated):")
        submitted = st.form_submit_button("Generate Questions")

        if submitted and all([full_name, email, phone, position, location, tech_stack]):
            st.session_state.full_name = full_name
            st.session_state.email = email
            st.session_state.phone = phone
            st.session_state.experience = experience
            st.session_state.position = position
            st.session_state.location = location
            st.session_state.tech_stack = tech_stack
            st.session_state.stage = "questions"
            st.rerun()

elif st.session_state.stage == "questions":
    st.subheader(f"Hello {st.session_state.full_name}, here are your questions:")
    techs = [tech.strip() for tech in st.session_state.tech_stack.split(",")]

    for tech in techs:
        prompt = generate_prompt(tech)
        response = generate_response(prompt)
        if response:
            st.markdown(f"**Questions for {tech}:**\n\n{response}")
        else:
            st.markdown(f"**Questions for {tech}:**\n\nSorry, I couldn't generate any questions for this topic.")

    if "conversation_history" not in st.session_state:
        st.session_state.conversation_history = []

    user_input = st.text_input("You may ask follow-up questions or type 'exit' to stop:")

    if any(word in user_input.lower() for word in ["exit", "quit", "bye"]):
        st.session_state.stage = "done"
        st.rerun()
    elif user_input:
        last_tech = techs[-1] if techs else "general tech"
        follow_up_prompt = f"Provide a follow-up technical question or clarification for {last_tech} based on: {user_input}"
        response = generate_response(follow_up_prompt)
        if response:
            st.session_state.conversation_history.append((user_input, response))
            st.markdown(f"**Follow-up Response:**\n\n{response}")
        else:
            st.markdown("Sorry, I couldn't generate a response.")

    if st.session_state.conversation_history:
        st.subheader("Conversation History")
        for q, a in st.session_state.conversation_history:
            st.markdown(f"**You:** {q}")
            st.markdown(f"**Bot:** {a}")

elif st.session_state.stage == "done":
    st.success("Thank you for your time. The interview session has been closed.")
    if st.button("Start Over"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
