from App.models.exercise import Exercise
from App.database import db
import requests,json


def add_exercise(userID,routine_id,exercise_id):
    # user_routine=user_routine(exercise_id=exercise_id,routine_id=routine_id);
    exercise.routine.append(routine)
    db.session.add();
    db.session.commit()
    return True
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
