from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


class Excercise(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False, unique=True)
    muscle=  db.Column(db.String, nullable=False)
    category =  db.Column(db.String, nullable=False)
    difficulty =  db.Column(db.String, nullable=False)
    force= db.Column(db.String, nullable=False)

    def __init__(self,name,muscle,category,difficulty,force):
        self.name=name
        self.muscle=muscle
        self.category=category
        self.difficulty=difficulty
        self.force=force
        pass


