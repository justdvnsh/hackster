import json
import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate('hackster-justdvnsh-firebase-adminsdk-tzcaf-396fd300d1.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hackster-justdvnsh.firebaseio.com'
})

database = db.reference('competitions')

with open('competitions.json', 'r') as fl:
    data = fl.read()
    final_data = json.loads(data)

#print(final_data)

for dat in final_data:
    database.push(dat)

print(database.get())