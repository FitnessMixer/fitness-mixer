import requests, json
from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash,url_for
from flask_login import login_required, login_user,current_user,logout_user
from App.models import User, db , Exercise, Routine
from App.controllers.user import create_user,editEmail,check_password

#eh big dawd bruh




index_views = Blueprint('index_views', __name__, template_folder='../templates')
def getExercises():
    muscle = 'abdominals'
    i=0
    muscles=['abdominals','abductors','adductors','biceps','calves','chest','forearms','glutes','hamstrings','lats','lower_back','middle_back','neck','quadriceps','traps','triceps']
    for m in muscles:
        api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}'.format(muscles[i])
        response = requests.get(api_url, headers={'X-Api-Key': 'NwmKx1s20Ive3BSqoYMvmw==zbTgNEmqqVzTlGT4'})
        i+=1   
        if response.status_code == requests.codes.ok:
            response_json = json.loads(response.text)
            # Convert the JSON string to a Python list
            exercises = response_json
            for x in exercises:
                exercise=Exercise(name=x["name"],muscle=x["muscle"],category=x["type"],equipment=x['equipment'],difficulty=x["difficulty"],instructions=x["instructions"])
                db.session.add(exercise)
                db.session.commit()
                #print("Exercises added")
        else:
            print("Error:")


@index_views.route('/', methods=['GET'])
def initialize():
    db.drop_all()
    db.create_all()
    create_user(username='bob', password='bobpass',email='bob@email.com')
    getExercises()
    return redirect('/signup')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass','bob@email.com')
    getExercises();
    return jsonify(message='db initialized!')


@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

@index_views.route('/users', methods=['GET'])
def displayUsers():
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
      flash('Account Created!')  # send message
      login_user(newuser)  # login the user
      return redirect('/home') # redirect to homepage
    except Exception:  # attempted to insert a duplicate user
      db.session.rollback()
      flash("username or email already exists")  # error message
      return render_template('signup.html')

@index_views.route('/loadlist',methods=['GET'])
@login_required
def loadList():
  return render_template("home.html",exercises=Exercise.query.all())
  pass

@index_views.route('/mylist',methods=['GET'])
@login_required
def mylist():
  myex=current_user.routine
  return render_template('mylist.html',exercises=myex)
  pass

@index_views.route('/editProfile')
@login_required
def edit():
  return render_template('editProfile.html')
  pass

@index_views.route('/filter/<string:muscle>')
@login_required
def filterMuscle(muscle):
  return render_template('filtered.html',exercises=Exercise.query.filter_by(muscle=muscle))

@index_views.route('/filterbyDifficulty/<string:difficulty>')
@login_required
def filterByDifficulty(difficulty):
  return render_template('filtered.html',exercises=Exercise.query.filter_by(difficulty=difficulty))


@index_views.route('/addExercise/<int:exerciseID>')
@login_required
def addEXercise(exerciseID):
  userEx=current_user.addExercise(exerciseID=exerciseID)
  if (userEx):
    flash("Exercise Added")
    return redirect('/mylist')
  else:
    flash("Not added")
    return redirect('/home')
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
  if user and user.check_password(password=data['password']):  # check credentials
    flash('Logged in successfully.')  # send message to next page
    login_user(user)  # login the user
    return redirect('/home')  # redirect to main page if login successful

  else:
    flash('Invalid username or password')  # send message to next page
    return redirect('/login')
  pass

@index_views.route('/edit', methods=['GET'])
@index_views.route('/edit', methods=['GET'])
@login_required
def edit_page():
  return render_template('editProfile.html')


@index_views.route('/edit/email', methods=['POST'])
@login_required
def edit_email():
   data = request.form["new_email"]
   user = User.query.filter_by(username=current_user.username).first()
   if user:
      current_user.editEmail(data)
      flash('Email Changed Sucessfully.')  # send message to next page
   else:
      flash('Email Change Unsucessful.')  # send message to next page
   
   return redirect('/home')


@index_views.route('/edit/username', methods=['POST'])
@login_required
def edit_username():
  
   data = request.form["new_user"]
   user = User.query.filter_by(username=current_user.username).first()
   if user:
      current_user.editUserName(username=data)
      flash('Username Changed Sucessfully.')  # send message to next page
   else:
      flash('Username Change Unsucessful.')  # send message to next page
   
   return redirect('/home')


@index_views.route('/edit/password', methods=['POST'])
@login_required
def edit_password():
  
   data = request.form["new_password"]
   user = User.query.filter_by(username=current_user.username).first()
   if user:
      current_user.editPassword(password=data)
      flash('Password Changed Sucessfully.')  # send message to next page
   else:
      flash('Password Changed Unsucessful.')  # send message to next page
   
   return redirect('/home')

@index_views.route('/complete/<int:user_exercise_id>')
@login_required
def remove(user_exercise_id):
  routine=Routine.query.filter_by(id=user_exercise_id,userID=current_user.id).first()
  flash("Error here")
  if (routine):
    check=routine.release_routine()
    flash("Workout Completed")
    return redirect('/mylist')
  else:
    flash ("Workout not Removed")
  return redirect('/home')



  pass

@index_views.route('/logout', methods=['GET'])
@login_required
def logout_action():
  logout_user()
  flash('Logged Out')
  return redirect('/login')
   




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