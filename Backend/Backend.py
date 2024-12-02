#to test 

from functools import wraps
from flask import Flask,request,jsonify,render_template,redirect ,url_for ,session,Response
from flask_cors import CORS
import pickle 
import jwt
import pymongo
from datetime import datetime, timedelta, date
import json
from bson import ObjectId
import math
from User import User
from  werkzeug.security import generate_password_hash, check_password_hash
from Appsettings import SecretKey
app=Flask(__name__)
CORS(app)

app.secret_key = SecretKey
app.config['SECRET_KEY'] = SecretKey
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['GestionStockage']

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            current_user = db.users.find_one({ "PublicId" : data['public_id'] })
        except:
            #return jsonify({"message":"Token Invalide"}), 401
            return jsonify({"message","Token Invalide"}), 401
        # returns the current logged in users context to the routes
        return  f(current_user, *args, **kwargs)
  
    return decorated

@app.route('/register',methods=['POST'])
def create_user():
    if request.json['username']==None or request.json['password']==None:
        return {"message":"Invalid Inputs"},401
    user=User(username=request.json['username'],password=generate_password_hash(request.json['password']),role="user")
    try:
        rech=db.users.find_one({'username':user.username})
        if not rech==None:
            return {'message':'utilisateur deja exisite'},400
        else:
            app.logger.info(user.__dict__)
            db.users.insert_one(user.dict())
            return {'message':'utilisateur cree avec succee'},201
    except Exception as e:
        return e,500

@app.route('/login',methods=['POST'])
def login():
     user = request.json['username']
     pwd = request.json['password']
     res=db.users.find_one({'username':user})
     if(res==None):
         return {'message':'utilisateur non trouve'},401
     if check_password_hash(res["password"], pwd):
        # generates the JWT Token
        expDate=datetime.now() + timedelta(days=30)
        token = jwt.encode({
            'public_id': str(res["PublicId"]),
            'exp' : int(expDate.timestamp())
        }, app.config['SECRET_KEY'],algorithm="HS256")
        return {'token' : token},201
     else:
        return {"message":"wrong password"},403



@app.route('/produit',methods=['GET'])
@token_required
def ajoutProduit(current_user):
     return {"message success":"success"},200
     
 
     


# # @app.route('/produi/<doc>',methods=['GET'])
# # def getProduit(doc):
# #    pass
    
# # @app.route('/produi/<doc>',methods=['DELETE'])
# # def getProduit(doc):
# #     pass
# # @app.route('/produi/<doc>',methods=['PUT'])
# # def getProduit(doc):
# #     pass
if __name__=='__main__':
    app.run(debug=True)
  