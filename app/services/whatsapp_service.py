import requests
from config.config import Config

WHATSAPP_API_URL = f"https://graph.facebook.com/v13.0/{Config.WHATSAPP_PHONE_NUMBER_ID}/messages"

def send_whatsapp_message(recipient, message):
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient,
        "type": "text",
        "text": {"body": message}
    }
    headers = {
        "Authorization": f"Bearer {Config.WHATSAPP_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    response = requests.post(WHATSAPP_API_URL, json=payload, headers=headers)
    return response.json()