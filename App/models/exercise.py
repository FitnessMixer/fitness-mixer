from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db


user_routines = db.Table('user_routines',
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercise.id'), primary_key=True),
    db.Column('routine_id', db.Integer, db.ForeignKey('routine.id'), primary_key=True)
)

class Exercise(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=True,unique=False)
    muscle=  db.Column(db.String, nullable=True,default=None)
    equipment=db.Column(db.String, nullable=True,default=None)
    category =  db.Column(db.String, nullable=True,default=None)
    difficulty =  db.Column(db.String, nullable=True,default=None)
    instructions=db.Column(db.String, nullable=True,default=None)


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
class Routine(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    userID=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    name =  db.Column(db.String, nullable=False, unique=True)
    target= db.Column(db.String,nullable=False)
    difficulty =  db.Column(db.String, nullable=False)
    reps=db.Column(db.Integer,nullable=False)
    sets=db.Column(db.Integer,nullable=False)

    def __init__(self,user_id,name,target,difficulty,sets,reps):
        self.name=name
        self.difficulty=difficulty
        self.userID=user_id
        self.name=name
        self.target=target
        self.sets=sets
        self.reps=reps
        pass


