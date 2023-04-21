import openai
from twilio.rest import Client

# Set up OpenAI API key and model
openai.api_key = "YOUR_API_KEY"
model_engine = "davinci"

# Set up Twilio account details
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
client = Client(account_sid, auth_token)

# Define a function to generate OpenAI response
def generate_response(text):
    prompt = f"Conversation with OpenAI:\n\nUser: {text}\nAI:"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Define a function to handle incoming WhatsApp messages
def handle_message(message):
    response_text = generate_response(message.body)
    message.reply(response_text)

# Set up Twilio webhook to listen for incoming messages
from flask import Flask, request
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="Thanks for your message! Our chatbot will get back to you soon.",
        to=message.from_
    )
    handle_message(request.form["Body"])
    return ""

if __name__ == "__main__":
    app.run(debug=True)
