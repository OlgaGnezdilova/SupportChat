from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
import os
from dotenv import load_dotenv

load_dotenv()

def ask_question(question):
    try:
        response = client.chat.completions.create(model="gpt-4o-mini",
        messages=[{"role": "user", "content": question}],
        max_tokens=100)
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == "__main__":
    question = input("Please enter your question: ")
    if question:
        answer = ask_question(question)
        print("Answer:", answer)
    else:
        print("Please provide a valid question.")