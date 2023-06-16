from flask import Flask, make_response, request, jsonify, render_template, abort
import os
from flask_cors import CORS, cross_origin
from requests import HTTPError
from utils.utils import decodeImage
from predict import predict
from execption import InvalidDocomentId
import firebase_admin
from firebase_admin import credentials, auth, firestore
from dotenv import load_dotenv
import json
import pyrebase

load_dotenv()

cred = credentials.Certificate("serviceAccounts.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

with open('config.json') as json_file:
    config = json.load(json_file)

firebase = pyrebase.initialize_app(config)

auth_client = firebase.auth()

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
# app.debug = True
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = predict(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/api-doc", methods=['GET'])
@cross_origin()
def api():
    return render_template('api.html')

@app.route("/our-team", methods=['GET'])
@cross_origin()
def team():
    return render_template('team.html')

@app.route("/api/login", methods=['POST'])
@cross_origin()
def login():
    email = request.json["email"]
    password = request.json["password"]
    try:
        user = auth_client.sign_in_with_email_and_password(email,password)
        id_token = user["idToken"]
    except HTTPError as e:
        error_response = e.args[1]
        error_data = json.loads(error_response)
        error_message = error_data["error"]["message"]
        error_code = error_data["error"]["code"]
        abort(make_response(jsonify(error_code=error_code, message=error_message), error_code))
    res = {"token" : id_token}
    return jsonify(res)

def getData(collectionName, docId):
    stringId = str(docId)
    doc_ref = db.collection(collectionName).document(stringId)
    doc = doc_ref.get()
    if (doc.to_dict() != None):
        return doc.to_dict()
    else:
        raise InvalidDocomentId
    
@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try:
        token = request.headers['token']
        auth.verify_id_token(token)
    except:
        abort(make_response(jsonify(message="Unauthorized User"), 401))
    
    image = request.json['image']
    decodeImage(image, clApp.filename)
    try:
        pred = clApp.classifier.skinClassifier()
        res = getData("recommendations",pred)
        return jsonify(res)
    except InvalidDocomentId:
        abort(make_response(jsonify(message="Error when getting data"), 500))
    except Exception as e:
        print(str(e))
        abort(make_response(jsonify(message="Error when predicting data", errorType=str(e)), 500))

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    clApp = ClientApp()
    app.run(host='0.0.0.0', port=port)
    # app.run(host='0.0.0.0', port=5000)
