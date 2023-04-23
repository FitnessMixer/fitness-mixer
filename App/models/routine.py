from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from App.models import user, exercise
class Routine(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    userID=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    exerciseID=db.Column(db.Integer,db.ForeignKey('exercise.id'),nullable=False)
    exercise=db.relationship('Exercise')
    name = db.Column(db.String, nullable=False, unique=True)

    #target= db.Column(db.String,nullable=False)
    #difficulty =  db.Column(db.String, nullable=False)
    #reps=db.Column(db.Integer,nullable=False)
    #sets=db.Column(db.Integer,nullable=False)

    def __init__(self,user_id,exerciseID,name):
        self.name=name
        self.exerciseID=exerciseID
        self.userID=user_id    
        #self.id=id(self)
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
