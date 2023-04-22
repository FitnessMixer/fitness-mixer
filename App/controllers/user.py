from App.models.user import User
from App.database import db

def create_user(username,password,email):
    newuser = User(username=username, password=password,email=email,no_routines=0)
    db.session.add(newuser);
    db.session.commit()
    return newuser;

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username,self):
# user = get_user(id)
    # if user:
    self.username = username
    return True;
    
def editUserName(self, userID,username):
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

def deleteAccount(self,userID):
    # data=request.json();
    # User del_user;
    # del_user=User.query.filter_by(userID=data["userID"])
    db.session.delete(self)
    db.session.commit()
    return True
    return None

def signUP(self):
    # user=User(username,password,phoneNumber,email,workoutLevel)
    db.session.add(self)
    db.session.commit()
    return True;

def check_password(self, password):
    """Check hashed password."""
    return self.check_password_hash(self.password, password)
