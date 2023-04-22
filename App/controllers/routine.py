from App.models import Routine
from App.database import db


def create_routine(user_id,name,e1,e2,e3,e4,e5,target,difficulty,sets,reps):
    newroutine = Routine(user_id=user_id,name=name,e1=e1,e2=e2,e3=e3,e4=e4,e5=e5,target=target,difficulty=difficulty,sets=sets,reps=reps)
    db.session.add(newuser);
    db.session.commit()
    return newuser;

def get_routine_by_name(name):
    return Routine.query.filter_by(name=name).first()

def get_all_users():
    return Routine.query.all()

def get_all_user_routines_json(user):
    routines = Routines.query.filter_by(user_id=user.id).all()
    if not routines:
        return []
    routines = [routines.get_json() for routine in routines]
    return routines


