# import json
# import pyrebase

# with open('config.json') as json_file:
#     config = json.load(json_file)

# # cred = credentials.Certificate("serviceAccounts.json")
# firebase = pyrebase.initialize_app(config)

# auth = firebase.auth()
# db = firebase.database()

email = "317damar@gmail.com"
password = "123456"

# # # user = auth.create_user_with_email_and_password(email,password)
# user = auth.sign_in_with_email_and_password(email,password)

# id_token = user["idToken"]

# recomendations = db.child("recommendations").get().val()
# print(recomendations) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}

# # decoded_token = auth.verify_id_token(id_token)
# # uid = decoded_token['uid']

# # print(uid)

import firebase_admin
from firebase_admin import credentials, auth
import pyrebase
import json
import time

with open('config.json') as json_file:
    config = json.load(json_file)

cred = credentials.Certificate("serviceAccounts.json")
fb = firebase_admin.initialize_app(cred)
firebase = pyrebase.initialize_app(config)

auth_client = firebase.auth()

# user = auth.get_user_by_email(email)
# print('Successfully fetched user data: {0}'.format(user.uid))
user = auth_client.sign_in_with_email_and_password(email,password)
id_token = user["idToken"]
print(id_token)
# time.sleep(2)

# try:
#     decoded_token = auth.verify_id_token(id_token)
#     uid = decoded_token['uid']
#     print(decoded_token)
#     print(uid)
# except Exception as error:
#     print(error)