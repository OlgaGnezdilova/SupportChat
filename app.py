import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

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
        Please provide 5 alternative, healthier beliefs in a confident, affirmative form, each one written as a statement, not a question. 
        Respond in the same language as the question and avoid using question marks."""


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
st.markdown("<h3 style='text-align: center;'>Enter your belief here</h3>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Feel free to use your native language</h3>", unsafe_allow_html=True)

question = st.text_input("Enter your belief here", label_visibility="collapsed", placeholder="")

if st.button("Get support"):
    if question:
        answer = ask_question(question)
        st.subheader("")
        st.subheader("Here are some alternative thoughts:")
        st.write(answer)
        st.subheader("")
        st.markdown("<h3 style='text-align: center;'>Which of these alternative thoughts supports you more on your journey?</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>Repeate it one more time to support yourself!</h3>", unsafe_allow_html=True)
    else:
        st.write("Please enter a valid belief")

   


