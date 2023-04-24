from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

from App.database import db
from App.models.exercise import Exercise
from App.models.routine import Routine



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email =  db.Column(db.String, nullable=False, unique=True)
    routine = db.relationship('Routine', backref='user')

    def __init__(self, username, password,email):
        self.username = username
        self.set_password(password)
        self.email=email
        self.id=id

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def addExercise(self,exerciseID):
        ex=Exercise.query.get(exerciseID)
        if(ex):
            try:
                exer=Routine(self.id,exerciseID,ex.name)
                db.session.add(exer)
                db.session.commit()
                return exer
            except Exception:
                db.session.rollback()
            return None
        return None

    def editUserName(self,username):
        # user=User.query.get(userID)
        self.username=username
        db.session.commit()
        return True


    def editEmail(self,email):
        self.email=email
        db.session.commit()
        return True;

    def editPassword(self,password):
        self.set_password(password);
        db.session.commit()

    def removeRoutine(user_exercise_id):
        rout=Routine.query.get(user_exercise_id)
        if rout.user==rout.user_id:
            db.session.delete(rout)
            db.session.commit()
            return True
        return None




