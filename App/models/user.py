from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

from App.database import db
from App.models import exercise , routine



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    email =  db.Column(db.String, nullable=False, unique=True)
    no_routines=db.Column(db.Integer,nullable=True,default=0);
    routine = db.relationship('Routine', backref='user')

    def __init__(self, username, password,email, no_routines):
        self.username = username
        self.set_password(password)
        self.email=email
        self.no_routines=no_routines
        self.id=id(self)

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

    def addExercise(self,exerciseID,name):
        ex=Exercise.query.get(id=exerciseID)
        if(ex):
            try:
                exer=Routine(user_id=self.id,exerciseID=exerciseID,name=ex.name)
                db.session.add(exer)
                db.session.commit()
                return exer
            except Exception:
                db.session.rollback()
        return None

