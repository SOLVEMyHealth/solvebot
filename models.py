from app import db 
from sqlalchemy import Column , Integer , String 

class User(db.Model):
    __tablename_= "users"
    id= db.Column(db.Integer, primary_key= True)
    whatsapp_number = db.Column(db.String(15), unique= True , nullable=False)
    chat_history = db.relationship('ChatHistory', backref='user',lazy=True)


class ChatHistory(db.Model):
    __tablename__= 'chathistory'
    id = db.Column(db.Integer, primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    message= db.Column(db.Text, nullable = False)
    response = db.Column(db.Text, nullable= False)


