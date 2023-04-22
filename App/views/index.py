import requests, json
from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash
from flask_login import login_required, login_user
from App.models import User, db , Exercise
from App.controllers import create_user




def getExercises():
  muscle = 'abdominals'
  api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscle)
  response = requests.get(api_url, headers={'X-Api-Key': 'NwmKx1s20Ive3BSqoYMvmw==zbTgNEmqqVzTlGT4'})

  if response.status_code == requests.codes.ok:
   response_json = json.loads(response.text)

# Convert the JSON string to a Python list
  exercises = response_json
    
  for x in exercises:
    
      exercise=Exercise(name=x["name"],muscle=x["muscle"],category=x["type"],equipment=x['equipment'],difficulty=x["difficulty"],instructions=x["instructions"])
      db.session.add(exercise)
      db.session.commit()
      print(x["name"])
      print("Exercises added")
    # return exercises
  else:
    print("Error:", response.status_code, response.text)

  

#getExercises()




index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def login():
    return render_template('signup.html')
@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass','bob@email.com')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

@index_views.route('/users', methods=['GET'])
def displaySignup():
    return render_template('users.html')

@index_views.route('/', methods=['GET'])
@index_views.route('/signup', methods=['GET'])
def signup_page():
  return render_template('signup.html')

@index_views.route('/signup', methods=['POST'])
def signup():
    data=request.form
    try:
      newuser=create_user(username=data["username"],password=data["password"],email=data["email"])
      #db.session.add(newuser)
      #db.session.commit()  # save user
      login_user(newuser)  # login the user
      flash('Account Created!')  # send message
      return render_template('login.html') # redirect to homepage
    except Exception:  # attempted to insert a duplicate user
      db.session.rollback()
      flash("username or email already exists")  # error message
      return render_template('signup.html')

@index_views.route('/loadlist',methods=['GET'])
@login_required
def loadList():
  return render_template("home.html",exercises=getExercises())
  pass

@index_views.route('/mylist',methods=['GET'])
@login_required
def mylist():
  return render_template('home.html')
  pass

@index_views.route('/editProfile')
@login_required
def edit():
  return render_template('editProfile.html')
  pass


@index_views.route('/', methods=['GET'])
@index_views.route('/login', methods=['GET'])
def login_page():
  return render_template('login.html')

@index_views.route('/app', methods=['GET'])
@index_views.route('/home', methods=['GET'])
@login_required
def home_page():
  return render_template('home.html')

@index_views.route('/login', methods=['POST'])
def login_action():
  data = request.form
  user = User.query.filter_by(username=data['username']).first()
  if user or user.check_password(password=data['password']):  # check credentials
    flash('Logged in successfully.')  # send message to next page
    login_user(user)  # login the user
    return render_template('home.html')  # redirect to main page if login successful

  else:
    flash('Invalid username or password')  # send message to next page
    return redirect('/login')
  pass
  


#getExercises()

#API STUFF

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