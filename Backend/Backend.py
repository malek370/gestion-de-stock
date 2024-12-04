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
from Commande import Commande
from Produit import Produit
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
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],algorithms=["HS256"])
            current_user = db.users.find_one({ "PublicId" : data['public_id']})
        except Exception:
            return jsonify({"message","Token Invalide"}), 401
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

#PRODUITS +++++++++++++++++++

@app.route('/produit',methods=['GET'])
def GetAllProduit():
    produits=Produit.get(db)
    return produits

@app.route('/produit/<doc>',methods=['GET'])
def GetProduit(doc):
    produit=Produit.getOne(doc,db)
    if produit==None: return {"message":"Produit introuvable"},404
    return produit.__dict__,200

@app.route('/produit',methods=['POST'])
def CreerProduit():
    produit=Produit(request.json["nom_prod"],request.json["description"],int((request.json["quantite"] )),float(request.json["prix_unit"]))
    produit.ajouter(db)
    return {"message":"created successfully"} ,201

@app.route('/produit/<doc>',methods=['PUT'])
def UpdateProduit(doc):
    nouveauProduit={
    "nom_prod": request.json["nom_prod"],
    "description": request.json["description"],
    "quantite":int(request.json["quantite"] ),
    "prix_unit":float(request.json["prix_unit"])
    }
    produit=Produit.getOne(doc,db)
    if produit==None: return {"message":"Produit introuvable"},404
    produit.modifier(nouveauProduit,db)
    return {"message":"updated successfully"} ,204

@app.route('/produit/<doc>',methods=['DELETE'])
def supprimerProduit(doc):
    produit=Produit.getOne(doc,db)
    if produit==None: return {"message":"Produit introuvable"},404
    produit.supprimer(db)   
    return {"message":"deleted successfully"},204    


#commandes ============================================


@app.route('/commande',methods=['GET'])
def getAllCommandes():
    return Commande.get(db)

@app.route('/commande/<doc>',methods=['GET'])
def GetCommande(doc):
    commande=Commande.getOne(doc,db)
    if commande==None: return {"message":"commande introuvable"},404
    return commande.__dict__,200


@app.route('/commande',methods=['POST'])
def CreerCommande():
    commande=Commande()
    commande.ajouter(db)
    return {"message":commande.code_cmd} ,201

@app.route('/commande/<doc>',methods=['PUT'])
def AjouterProduitCommande(doc):
    produit=Produit.getOne(request.json["code_prod"],db)
    if produit==None: return {"message":"Produit introuvable"},404
    commande=Commande.getOne(doc,db)
    if commande==None: return {"message":"commande introuvable"},404
    commande.ajouterProduit(produit,int(request.json["nb_produit"]),db)
    return {"message":"updated successfully"} ,204

@app.route('/commande/<doc>',methods=['DELETE'])
def supprimerCommade(doc):
    commande=Commande.getOne(doc,db)
    if commande==None: return {"message":"Commande introuvable"},404
    commande.supprimer(db)   
    return {"message":"deleted successfully"},204
# def ajoutcommande():
#     return {"message":"ok"},200 
     


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
  