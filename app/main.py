from flask import Flask , request , jsonify
from app.bot.chatbot import SolveMyHealthBot
from app.database.db_manager import DatabaseManager 
from app.services.whatsapp_service import send_whatsapp_message 
from config.config import Config 

app = Flask(__name__)
app.config.from_object(Config)

db_manager = DatabaseManager(app.config['SQL_ALCHEMY_DATABASE_URI'])
bot = SolveMyHealthBot(db_manager)

@app.route("/webhook", methods=['POST'])
def webhook():
    incoming_msg = request.json
    sender = incoming_msg['entry'][0]['changes'][0]['value']['messages'][0]['from']
    message = incoming_msg['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']

    bot_response = bot.handle_user_input(message)
    send_whatsapp_message(sender, bot_response)

    return jsonify({"status","message"}),200


if __name_=="__main__":
    app.run(debug=True)
