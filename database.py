from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://smoldex:Theo!032020@35.203.83.145:5432/medex-database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    privacy_data = db.Column(db.Text, nullable=True)  # Added a new column for privacy data

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

def init_db():
    with app.app_context():
        db.create_all()

def get_privacy_data_from_db(user_id):
    with app.app_context():
        user = User.query.get(user_id)
        if user:
            return user.privacy_data
        else:
            return None