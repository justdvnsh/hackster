import json
import firebase_admin
from firebase_admin import db, credentials

cred = credentials.Certificate('hackster-justdvnsh-firebase-adminsdk-tzcaf-396fd300d1.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hackster-justdvnsh.firebaseio.com'
})

database = db.reference('competitions')

with open('competitions_kaggle.json', 'r') as fl:
    data_kaggle = fl.read()
    final_data_kaggle = json.loads(data_kaggle)

#print(final_data)

with open('competitions_analytics_vidya.json', 'r') as fl:
    data_av = fl.read()
    final_data_av = json.loads(data_av)

for dat in final_data_av:
    database.push(dat)

print(database.get())