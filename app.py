import os
from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify
from .models import User, db
from flask_login import LoginManager, current_user, login_user, login_required, logout_user

login_manager = LoginManager()

def create_app():
  app = Flask(__name__, static_url_path='/static')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  app.config['TEMPLATES_AUTO_RELOAD'] = True
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
  app.config['DEBUG'] = True
  app.config['SECRET_KEY'] = 'MySecretKey'
  app.config['PREFERRED_URL_SCHEME'] = 'https'
  db.init_app(app)
  login_manager.init_app(app)
  login_manager.login_view = "login_page"
  app.app_context().push()
  return app

app = create_app()
app.app_context().push()
