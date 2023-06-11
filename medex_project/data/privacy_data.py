from sqlalchemy import Column, Integer, String, ForeignKey
from database import db

class PrivacyData(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    sensitive_data = Column(String)

    def __init__(self, user_id, sensitive_data):
        self.user_id = user_id
        self.sensitive_data = sensitive_data

    def __repr__(self):
        return f"<PrivacyData(user_id={self.user_id}, sensitive_data={self.sensitive_data})>"