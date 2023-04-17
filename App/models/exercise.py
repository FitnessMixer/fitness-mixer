from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


class Excercise(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False, unique=True)
    muscle=  db.Column(db.String, nullable=False)
    workoutLevel =  db.Column(db.String, nullable=False)

