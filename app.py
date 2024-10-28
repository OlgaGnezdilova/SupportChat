import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

if "show_buttons" not in st.session_state:
    st.session_state["show_buttons"] = False

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

try:
    with open("style.css") as css_file:
        st.markdown(f"<style>{css_file.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.warning("The style.css file was not found. Ensure it exists in the correct path.")

def ask_question(question):
    try:
        initial_prompt = f"""You are an experienced Cognitive Behavioral Therapy (CBT) therapist. 
        A client has shared the following belief: "{question}". 
        Offer 5 alternative, healthier beliefs that challenge this original belief."""

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": initial_prompt}],
            max_tokens=300
        )

        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        return f"An error occurred: {str(e)}"

st.markdown("<h1 style='text-align: center;'>Dark thought? Share it with me!</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: left;'>This app functions as an experienced Cognitive Behavioral Therapyst. Just share your troubles with it and enjoy alternative perspectives</h4>", unsafe_allow_html=True)
st.subheader("Enter your belief here:")

question = st.text_input("")

if st.button("Get support"):
    if question:
        answer = ask_question(question)
        st.subheader("")
        st.subheader("Here are some alternative thoughts:")
        st.write(answer)
        st.subheader("")
        st.subheader("Which of these alternative thoughts supports you more on your journey?")
    else:
        st.write("Please enter a valid belief")

    if st.session_state["show_buttons"]:
        col1, col2, col3, col4, col5 = st.columns(5)
        if col1.button("1"):
            st.markdown("<h4 style='text-align: center;'>Repeat the alternative one more time and good luck!</h4>", unsafe_allow_html=True)
        elif col2.button("2"):
            st.markdown("<h4 style='text-align: center;'>Repeat the alternative one more time and good luck!</h4>", unsafe_allow_html=True)
        elif col3.button("3"):
            st.markdown("<h4 style='text-align: center;'>Repeat the alternative one more time and good luck!</h4>", unsafe_allow_html=True)
        elif col4.button("4"):
            st.markdown("<h4 style='text-align: center;'>Repeat the alternative one more time and good luck!</h4>", unsafe_allow_html=True)
        elif col5.button("5"):
            st.markdown("<h4 style='text-align: center;'>Repeat the alternative one more time and good luck!</h4>", unsafe_allow_html=True)




