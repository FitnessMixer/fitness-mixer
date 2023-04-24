import click, pytest, sys, requests, json
from App.models import Exercise
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from App.database import db, get_migrate
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users )

# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)




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



# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_user(username='bob', password='bobpass',email='bob@email.com')
    getExercises()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)