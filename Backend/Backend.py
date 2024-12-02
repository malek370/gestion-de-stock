#to test 

from flask import Flask,request,jsonify,render_template,redirect ,url_for ,session
from flask_cors import CORS
import pickle 
import pymongo
import datetime
import json
from bson import ObjectId
import math

def tr(value):
    factor = 10 ** 2  # Two decimal places
    truncated_value = math.trunc(value * factor)
    return truncated_value
def json_util(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    elif isinstance(obj, list):
        return [json_util(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: json_util(value) for key, value in obj.items()}
    else:
        return obj
    
app=Flask(__name__)
CORS(app)

app.secret_key = 'your-secret-key'
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['GestionStockage']

"""@app.route('/home')
def home():
    if not 'user_id' in session:
            return redirect(url_for('login_page'))
    if session.get('role')=='1':
        return render_template('indexad.html')
    return render_template('index.html')
@app.route('/')
def login_page():
    if not 'user_id' in session:
            return render_template('login.html')
    return redirect(url_for('home'))
    """
@app.route('/register',methods=['POST'])
def create_user():
    user = request.json['user']
    pwd = request.json['pwd']
    try:
        rech=db.users.find_one({'username':user})
        if not rech==None:
            return jsonify({'message':'utilisateur deja exisite'})
        else:
            db.users.insert_one({'username':user,'password':pwd,'isadmin':'0'})
            return jsonify({'message':'utilisateur cree avec succee'})
    except pymongo.errors.PyMongoError as e:
        return jsonify({'message':'erreur !'})

@app.route('/login',methods=['POST'])
def login():
     user = request.json['user']
     pwd = request.json['pwd']
     res=db.users.find_one({'username':user,'password':pwd})
     if(not res==None):
         session['user_id'] = user 
         session['role']=res['role']
         return jsonify({'status':'1','message':'utilisateur trouve'})
     else :
         return jsonify({'status':'0','message':'utilisateur introuvable'})

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('role', None)

@app.route('/produit',methods=['POST'])
def ajoutProduit():
     if not 'user_id' in session:
            return jsonify({'status':'0','message':'login please'})
     user = request.json['user']
     pwd = request.json['pwd']
     res=db.users.find_one({'username':user,'password':pwd})
     if(not res==None):
         session['user_id'] = user 
         session['role']=res['role']
         return jsonify({'status':'1','message':'utilisateur trouve'})
     else :
         return jsonify({'status':'0','message':'utilisateur introuvable'})
     
@app.route('/produit',methods=['GET'])
def getAllProduit():
     if not 'user_id' in session:
            return jsonify({'status':'0','message':'login please'})
     user = request.json['user']
     pwd = request.json['pwd']
     res=db.users.find_one({'username':user,'password':pwd})
     if(not res==None):
         session['user_id'] = user 
         session['role']=res['role']
         return jsonify({'status':'1','message':'utilisateur trouve'})
     else :
         return jsonify({'status':'0','message':'utilisateur introuvable'})
     


@app.route('/produi/<doc>',methods=['GET'])
def getProduit(doc):
    try:
        pass
    except pymongo.errors.PyMongoError as e:
        return jsonify({'message':'erreur !'})
    
@app.route('/produi/<doc>',methods=['DELETE'])
def getProduit(doc):
    try:
        pass
    except pymongo.errors.PyMongoError as e:
        return jsonify({'message':'erreur !'})

@app.route('/produi/<doc>',methods=['PUT'])
def getProduit(doc):
    try:
        pass
    except pymongo.errors.PyMongoError as e:
        return jsonify({'message':'erreur !'})

     
@app.route('/history')
def history():
    if not 'user_id' in session:
            return redirect(url_for('login_page'))
    if session.get('role')=='1':
        return render_template('historyad.html')
    return render_template('history.html')

@app.route('/history/recent')
def history_data_recent():
    if session.get('role')=='1':
        predictions = list(db.predictions.find().sort('_id',-1))
    else:
        predictions = list(db.predictions.find({'username':session.get('user_id')}).sort('_id',-1))
    prediction_data_json = json.loads(json.dumps(json_util(predictions)))
    return prediction_data_json

@app.route('/history/data')
def history_data_encient():
    predictions = list(db.predictions.find({'username':session.get('user_id')}).sort('_id',1))
    prediction_data_json = json.loads(json.dumps(json_util(predictions)))
    return prediction_data_json

@app.route('/history/defaut')
def history_data_defaut():
    if session.get('role')=='1':
        predictions = list(db.predictions.find().sort([('proba',-1),('_id',-1)]))
    else:
        predictions = list(db.predictions.find({'username':session.get('user_id')}).sort([('proba',-1),('_id',-1)]))
    prediction_data_json = json.loads(json.dumps(json_util(predictions)))
    return prediction_data_json

@app.route('/history/nondefaut')
def history_data_nondefaut():
    if session.get('role')=='1':
        predictions = list(db.predictions.find().sort([('proba',1),('_id',-1)]))
    else:
        predictions = list(db.predictions.find({'username':session.get('user_id')}).sort([('proba',1),('_id',-1)]))
    prediction_data_json = json.loads(json.dumps(json_util(predictions)))
    return prediction_data_json

@app.route('/history/delete/<doc>',methods=['DELETE'])
def delete_doc(doc):
    try:
        result = db.predictions.delete_one({'_id': ObjectId(doc)})
        return jsonify({'message': 'enregistrement supprime avec succee'})
    except pymongo.errors.PyMongoError as e:
        return jsonify({'message':'erreur !'})
    
@app.route('/users/get')
def get_users():
    users = list(db.users.find({"isadmin":'0'}))
    prediction_data_json = json.loads(json.dumps(json_util(users)))
    return prediction_data_json

@app.route('/users')
def users_page():
    if not 'user_id' in session:
            return redirect(url_for('login_page'))
    if session.get('role')=='1':
        return render_template('users.html')
    return redirect(url_for('home'))

@app.route('/users/delete/<doc>',methods=['DELETE'])
def delete_doc_user(doc):
    try:
        db.users.delete_one({'_id': ObjectId(doc)})
        return jsonify({'message': 'enregistrement supprime avec succee'})
    except pymongo.errors.PyMongoError as e:
        return jsonify({'message':'erreur !'})


    
if __name__=='__main__':
    app.run(port=3002)
