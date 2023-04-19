import os
from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify
from  .models import  Exercise,User, db
from flask_login import LoginManager, current_user, login_user, login_required, logout_user


login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)

@login_manager.unauthorized_handler
def unauthorized():
    flash('Unauthorized!')
    return redirect(url_for('login_page'))

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

# Page Routes

#To update
@app.route("/", methods=['GET'])
def login():
   return redirect(url_for('home_page'))

@app.route("/app", methods=['GET'])
@app.route("/app/<int:pokemon_id>", methods=['GET'])
# add @login_required decorator to require login
def home_page(pokemon_id=1):
    #pass relevant data to template
    return render_template("home.html")



@app.route('/signup', methods=['GET'])
def signup_page():
  return render_template('signup.html')

# Form Action Routes




if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
