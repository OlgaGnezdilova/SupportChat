from flask import Flask, request, jsonify, render_template
import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

# Route to serve the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle chatbot interactions
@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    belief = data['question']

    # GPT prompt for CBT therapist
    prompt = f"""You are an experienced Cognitive Behavioral Therapy (CBT) therapist. 
    A client has shared the following belief: "{belief}". 
    Offer 5 alternative, healthier beliefs that challenge this original belief. 
    After providing the 5 alternatives, ask the client to select which alternative belief they resonate with the most."""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": prompt}],
            max_tokens=300
        )

        # Extract the content from the response
        answer = response['choices'][0]['message']['content'].strip()
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
