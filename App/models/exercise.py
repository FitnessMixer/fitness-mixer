from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


user_routines = db.Table('user_routines',
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), primary_key=True),
    db.Column('routine_id', db.Integer, db.ForeignKey('routine.id'), primary_key=True)
)

class Excercise(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False, unique=True)
    muscle=  db.Column(db.String, nullable=False)
    category =  db.Column(db.String, nullable=False)
    difficulty =  db.Column(db.String, nullable=False)
    force= db.Column(db.String, nullable=True)
    routines=db.relationship('Routine',secondary=user_routines,backref='exercises')


    def __init__(self,name,muscle,category,difficulty,force):
        self.name=name
        self.muscle=muscle
        self.category=category
        self.difficulty=difficulty
        self.force=force
        pass

# a rotuines has many exercises in it and an exercise can be present in many routines
class Routine(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    userID=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    name =  db.Column(db.String, nullable=False, unique=True)
    muscle1=  db.Column(db.String, nullable=False)#what's it targeting
    muscle2=  db.Column(db.String, nullable=True)
    muscle3=  db.Column(db.String, nullable=True)
    difficulty =  db.Column(db.String, nullable=False)
    time=db.Column(db.Integer,nullable=False)

    def __init__(self,name,muscle1,muscle2,muscle3,difficulty):
        self.name=name
        self.muscle1=muscle1
        self.muscle2=muscle2
        self.muscle3=muscle3
        self.difficulty=difficulty
        pass


