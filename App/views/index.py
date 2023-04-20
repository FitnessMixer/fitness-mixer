from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash
from App.models import User, db
from App.controllers import create_user

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('signup.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

@index_views.route('/users', methods=['GET'])
def displaySignup():
    return render_template('users.html')

@index_views.route('/signup', methods=['POST'])
def signup():
    data=request.form
    newuser= User(username=data["username"],password=data["password"],email=data["email"]);
    
      
    try:
      newuser.create_user();
      login_user(newuser)  # login the user
      flash('Account Created!')  # send message
      render_template('users.html')  # redirect to homepage
    except Exception:  # attempted to insert a duplicate user
      db.session.rollback()
      flash("username or email already exists")  # error message
      return redirect("/login")



@index_views.route('/', methods=['GET'])
@index_views.route('/login', methods=['GET'])
def login_page():
  return render_template('login.html')


@index_views.route('/login', methods=['POST'])
def login_action():
  data = request.form
  user = User.query.filter_by(username=data['username']).first()
  if user and user.check_password(data['password']):  # check credentials
    flash('Logged in successfully.')  # send message to next page
    login_user(user)  # login the user
    return redirect('/users')  # redirect to main page if login successful
  else:
    flash('Invalid username or password')  # send message to next page
  return redirect('/login')


  
#API STUFF

# import requests

# url = "https://calories-burned-by-api-ninjas.p.rapidapi.com/v1/caloriesburned"

# querystring = {"activity":"skiing"}

# headers = {
# 	"X-RapidAPI-Key": "abf5c13524mshc9214300313f611p1be4e0jsnfb6846048bd3",
# 	"X-RapidAPI-Host": "calories-burned-by-api-ninjas.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# #print(response.text)



# url2 = "https://musclewiki.p.rapidapi.com/exercises/1"

# headers = {
# 	"X-RapidAPI-Key": "abf5c13524mshc9214300313f611p1be4e0jsnfb6846048bd3",
# 	"X-RapidAPI-Host": "musclewiki.p.rapidapi.com"
# }

# response = requests.request("GET", url2, headers=headers)

#print(response.text)