from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with the API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to generate alternative beliefs based on the user's input
def ask_question(question):
    try:
        # Define the initial prompt for the chatbot to act as a CBT therapist
        initial_prompt = f"""You are an experienced Cognitive Behavioral Therapy (CBT) therapist. 
        A client has shared the following belief: "{question}". 
        Offer 5 alternative, healthier beliefs that challenge this original belief. 
        After providing the 5 alternatives, ask the client to select which alternative belief they resonate with the most."""
        
        # Send the prompt to the GPT-4 model
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": initial_prompt}],
            max_tokens=300
        )
        
        # Extract the bot's response
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main logic for interacting with the chatbot
if __name__ == "__main__":
    # Get the user's belief as input
    belief = input("Please enter the belief you want to challenge: ")
    
    if belief:
        # Call the function to get alternative beliefs
        answer = ask_question(belief)
        print("Therapist Response:", answer)
    else:
        print("Please provide a valid belief.")
