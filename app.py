from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse, Start
import os, openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
TWILIO_WHATSAPP = os.getenv("TWILIO_WHATSAPP_NUMBER")

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming = request.values.get("Body", "")
    # simple echo reply for now
    resp = MessagingResponse()
    resp.message(f"You said: {incoming}")
    return str(resp)

@app.route("/voice", methods=["POST"])
def voice():
    resp = VoiceResponse()
    resp.say("Hello! I’m your AI assistant. How can I help you?")
    return str(resp)

if __name__ == "__main__":
    app.run(port=5000)
