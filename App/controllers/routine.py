from App.models import Routine
from App.database import db


# def get_all_userRoutines(user):





# def get_all_users_json():
#     users = User.query.all()
#     if not users:
#         return []
#     users = [user.get_json() for user in users]
#     return users

# def update_user(id, username,self):
# # user = get_user(id)
#     # if user:
#     self.username = username
#     return True;
    
# def editUserName(self, userID,username,email,phoneNumber):
#     # user=User.query.get(userID)
#     self.username=username
#     self.phoneNumber=phoneNumber
#     self.email=email
#     return True

# def editphoneNumber(self,phoneNumber,email):
#     # user=User.query.get(userID)
#     # user.username=username
#     self.phoneNumber=phoneNumber;
#     self.email=email;
#     return True;

# def editEmail(self,email):
#     # user=User.query.get(userID)
#     self.email=email
#     return True;

# def deleteAccount(self,userID):
#     # data=request.json();
#     # User del_user;
#     # del_user=User.query.filter_by(userID=data["userID"])
#     db.session.delete(self)
#     db.session.commit()
#     return True
#     return None

# def signUP(self):
#     # user=User(username,password,phoneNumber,email,workoutLevel)
#     db.session.add(self)
#     db.session.commit()
#     return True;