import os
from flask import Flask
from flask_login import LoginManager, current_user
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta

from App.database import init_db
from App.config import config

from App.controllers import (
    setup_jwt,
    setup_flask_login
)

from App.views import views

def add_views(app):
    for view in views:
        app.register_blueprint(view)

def configure_app(app, config, overrides):
    for key, value in config.items():
        if key in overrides:
            app.config[key] = overrides[key]
        else:
            app.config[key] = config[key]

def create_app(config_overrides={}):
    app = Flask(__name__, static_url_path='/static')
    configure_app(app, config, config_overrides)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEVER_NAME'] = '0.0.0.0'
    app.config['PREFERRED_URL_SCHEME'] = 'https'
    app.config['UPLOADED_PHOTOS_DEST'] = "App/uploads"
    CORS(app)
    photos = UploadSet('photos', TEXT + DOCUMENTS + IMAGES)
    configure_uploads(app, photos)
    add_views(app)
    init_db(app)
    setup_jwt(app)
    setup_flask_login(app)
    app.app_context().push()
    return app

@app.route("/", methods=['GET'])
def login():
   return redirect(url_for('home_page'))


@app.route('/signup',methods=['POST'])
def signup_user_view():
  data = request.json
  
  if not all(key in data for key in ['username','email','password']):
    return jsonify({'Error': 'Missing required fields'}),400

  user = User.query.filter_by(username=data['username']).first()
  email= User.query.filter_by(email=data['email']).first()
  
  if email or user:
    return jsonify(error='username or email already exists'),400
  
  newuser = User(username=data['username'], email=data['email'], password=data['password'])

  db.session.add(newuser)
  db.session.commit()
  return jsonify(message=f'{newuser.username} created' ), 201


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
