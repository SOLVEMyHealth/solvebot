from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserProfile(Base):
    __tablename__ = 'user_profiles'

    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    gender = Column(String)
    contact_info = Column(String)

    assessments = relationship('HealthAssessment', back_populates='user')
    consultations = relationship('ConsultationRecord', back_populates='user')

class HealthAssessment(Base):
    __tablename__ = 'health_assessments'

    assessment_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_profiles.user_id'))
    assessment_date = Column(DateTime)
    score = Column(Float)
    notes = Column(String)

    user = relationship('UserProfile', back_populates='assessments')

class ConsultationRecord(Base):
    __tablename__ = 'consultation_records'

    record_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_profiles.user_id'))
    consultation_date = Column(DateTime)
    doctor = Column(String)
    notes = Column(String)

    user = relationship('UserProfile', back_populates='consultations')