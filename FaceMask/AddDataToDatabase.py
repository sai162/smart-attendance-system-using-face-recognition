import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://faceattendancerealtime-a7ee7-default-rtdb.firebaseio.com/'
    })

ref = db.reference('Students')
data = {
        "1234":{
        "name":"sai_charan",
        "major":"CSE",
        "starting_year":2020,
        "total_attendence":6,
        "standing":"A",
        "year":3,
        "last_attendance_time":"2022-12-11 0:54:34"
    },
"3214":{
        "name":"rohit",
        "major":"CSE",
    "starting_year": 2020,
        "total_attendence":6,
        "standing":"B",
        "year":3,
        "last_attendance_time":"2022-12-11 0:54:34"
    }
    }
for key, value in data.items():
    ref.child(key).set(value)