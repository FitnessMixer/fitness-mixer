from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from App.models import User,exercise
class Routine(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    userID=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    name = db.Column(db.String, nullable=False, unique=True)
    exercise1=db.Column(db.Integer,nullable=True)
    exericse2=db.Column(db.Integer,nullable=True)
    exericse3=db.Column(db.Integer,nullable=True)
    exercise4=db.Column(db.Integer,nullable=True)
    exercise5=db.Column(db.Integer,nullable=True)
    target= db.Column(db.String,nullable=False)
    difficulty =  db.Column(db.String, nullable=False)
    reps=db.Column(db.Integer,nullable=False)
    sets=db.Column(db.Integer,nullable=False)

    def __init__(self,user_id,name,e1,e2,e3,e4,e5,target,difficulty,sets,reps):
        self.name=name
        self.difficulty=difficulty
        self.userID=user_id
        self.exercise1=e1;
        self.exericse2=e2#these are not names but the ids of exercises save them and then look for that id in the table to display specifics
        self.exericse3=e3
        self.exercise4=e4
        self.exercise5=e5
        self.target=target
        self.sets=sets
        self.reps=reps
        self.id=id(self)
        pass

    def get_json(self):
        return{
            'exercise 1':self.exericse1,
            'exercise 2':self.exericse2,
            'exercise 2':self.exericse3,
            'exercise 2':self.exericse4,
            'exercise 2':self.exericse5,
            'Reps ':self.reps,
            'Sets':self.sets

        }
