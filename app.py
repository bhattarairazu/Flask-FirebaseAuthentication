import firebase_admin
import pyrebase
import json


from firebase_admin import credentials, auth
from flask import Flask, request
from functools import wraps

app = Flask(__name__)

#conect to firebase
cred = credentials.Certificate('fbAdminConfig.json')
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.load(open('fbconfig.json')))

users = [{'uid':1,'name':'Noah Sarahar'}]

#middle ware for validatin tkken
def check_token(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if not request.headers.get('authorization'):
            return {'message':'No token provide'},400
        try:
            user = auth.verify_id_token(request.headers['authorization'])
            request.user = user
        except:
            return {'message':'Invalid token provide'},400
        return f(*args,**kwargs)
    return wrap


@app.route('/api/userinfo')
@check_token
def userinfo():
    print(request.user)
    return {'data':users}, 200

@app.route('/api/signup',methods=['POST'])
def signup():
    email = request.get_json()['email']
    password = request.get_json()['password']

    if email is None or password is None:
        return {'message':'Error missing email or password'},400
    try:
        user = auth.create_user(
            email=email,password=password
        )
        return {'message':f'Successfully created user {user.uid}'},200
    except:
        return {'message':'Error createing user'},400

#signup to new user
@app.route('/api/token',methods=['POST'])
def token():
    email = request.get_json()['email']
    password = request.get_json()['password']

    try:
        user = pb.auth().sign_in_with_email_and_password(email,password)
        jwt = user['idToken']
        return {'token':jwt}, 200
    except:
        return {'message':'There was an error loggin in'}, 400



if __name__=="__main__":
    app.run(debug=True)