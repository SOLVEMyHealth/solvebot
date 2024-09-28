import os 
from flask import Flask ,  request , render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv 


load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS','False').lower() == 'true'

db = SQLAlchemy(app)


from models import User , ChatHistory
# routes 


@app.route("/")
def home():
    return render_template("index.html")    


@app.route("/whatsapp_webhook", methods= ['POST'])
def whatsapp_webhook():
    data = request.json   # Whatsapp should send the payload
    incoming_msg = data['messages'][0]['text']
    sender = data['messages'][0].get('from','')

    # Creating a dbession
    db_session = db.session

    user = db_session.query(User).filter(User.whatsapp_number == sender ).first() 
    if not user: 
        user = User(whatsapp_number = sender)
        db_session.add(user)
        db_session.commit()

    response_message = " open ai integration later"

    # save the chat history 

    chat = ChatHistory(user_id = user.id, message = incoming_msg , response= response_message )
    db_session.add(chat)
    db_session.commit()


    # send the response back to the whatsapp
    return "OK" , 200


# main function

if __name__ == "__main__":
    app.run(debug= True, port= 5000)