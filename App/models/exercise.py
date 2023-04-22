from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


class Exercise(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=True,unique=False)
    muscle=  db.Column(db.String, nullable=True,default=None)
    equipment=db.Column(db.String, nullable=True,default=None)
    category =  db.Column(db.String, nullable=True,default=None)
    difficulty =  db.Column(db.String, nullable=True,default=None)
    instructions=db.Column(db.String, nullable=True,default=None)
    routine = db.relationship('Routine', backref='exercise', lazy=True, cascade="all, delete-orphan")



    def __init__(self,name,muscle,category,equipment,difficulty,instructions):
        self.name=name
        self.muscle=muscle
        self.category=category
        self.difficulty=difficulty
        self.instructions=instructions
        self.equipment=equipment
        pass


    # def __init__(self):
    #     self.id=id(self);
    #     pass
# a rotuines has many exercises in it and an exercise can be present in many routines
