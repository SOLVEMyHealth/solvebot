from fastapi import FastAPI, Request
from app.bot.chatbot import SolveMyHealthBot
from app.database.db_manager import DatabaseManager
from app.services.whatsapp_service import send_whatsapp_message

app = FastAPI()
db_manager = DatabaseManager()
bot = SolveMyHealthBot(db_manager)

@app.on_event("startup")
async def startup():
    await db_manager.connect()

@app.on_event("shutdown")
async def shutdown():
    await db_manager.disconnect()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    sender = data['entry'][0]['changes'][0]['value']['messages'][0]['from']
    message = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

    bot_response = await bot.handle_user_input(message)
    await send_whatsapp_message(sender, bot_response)

    return {"status": "success"}

@app.get("/")
async def root():
    return {"message": "SolveMyHealth Bot is running!"}
