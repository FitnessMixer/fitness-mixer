import os
import csv

from flask import Flask
from flask_login import LoginManager, current_user
from flask_uploads import DOCUMENTS, IMAGES, TEXT, UploadSet, configure_uploads
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from datetime import timedelta
from App.controllers import ( create_user, get_all_users_json, get_all_users,getExercises )
from App.models import User,Exercise

from App.database import init_db,db
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
    with app.app_context():
        db.drop_all()
        db.create_all()
        user=User(username='bob', password='bobpass',email='bob@email.com')
        db.session.add(user)
        getExercises()
    return app

