import aiohttp
from config.config import Config

WHATSAPP_API_URL = f"https://graph.facebook.com/v13.0/{Config.WHATSAPP_PHONE_NUMBER_ID}/messages"

async def send_whatsapp_message(recipient, message):
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
    async with aiohttp.ClientSession() as session:
        async with session.post(WHATSAPP_API_URL, json=payload, headers=headers) as response:
            return await response.json()
