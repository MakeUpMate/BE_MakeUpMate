from flask import Flask, make_response, request, jsonify, render_template, abort
import os
from flask_cors import CORS, cross_origin
from utils.utils import decodeImage
from predict import predict
from execption import InvalidDocomentId
import firebase_admin
from firebase_admin import credentials, auth, firestore

cred = credentials.Certificate("serviceAccounts.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
# app.debug = True
CORS(app)

#@cross_origin()
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = predict(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

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


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    clApp = ClientApp()
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=5000)
