from flask_login import login_user, login_manager, logout_user, LoginManager
from flask_jwt_extended import create_access_token, jwt_required, JWTManager
from .exercise import getExercises
from .user import create_user
from App.database import init_db, db
from App.models import User

def jwt_authenticate(username, password):
  user = User.query.filter_by(username=username).first()
  if user and user.check_password(password):
    return create_access_token(identity=username)
  return None

def login(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None

def setup_flask_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    return login_manager

def setup_jwt(app):
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        user = User.query.filter_by(username=identity).one_or_none()
        if user:
            return user.id
        return None

    @jwt.user_lookup_loader
    def user_lookup_callback( _jwt_header, jwt_data):
        identity = jwt_data["sub"]
        return User.query.get(identity)

    return jwt

def initialize():

    # try:
    # # Start a transaction
    #     with session.begin():
    #     # Perform database operations here
    db.drop_all()
    db.create_all()
    user=User('rob23', 'robpass','rob345@email.com')
    # db.session.add(user)
    # getExercises()
    
    # print(rob.name)
    #     # If an error occurs, raise an exception
    # raise Exception("An error occurred during the transaction")

    # # If no exception is raised, commit the transaction
    #         session.commit()
    # except Exception as e:
    # # If an exception is raised, roll back the transaction
    #     session.rollback()
    # print("Transaction rolled back due to error:", e)
    # finally:
    # # Close the session
    #     session.close()
   
