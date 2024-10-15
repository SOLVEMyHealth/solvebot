from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, UserProfile, HealthAssessment, ConsultationRecord

class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def add_user(self, name, age, height, weight, gender, contact_info):
        session = self.get_session()
        new_user = UserProfile(name=name, age=age, height=height, weight=weight, gender=gender, contact_info=contact_info)
        session.add(new_user)
        session.commit()
        user_id = new_user.user_id
        session.close()
        return user_id

    def get_user(self, user_id):
        session = self.get_session()
        user = session.query(UserProfile).filter_by(user_id=user_id).first()
        session.close()
        return user