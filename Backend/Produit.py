import uuid
import pymongo
import pymongo.database

class Produit:

    def __init__(self, nom_prod: str, description: str, quantite: int, prix_unit: float):
        self.code_prod = uuid.uuid4().hex
        self.nom_prod = nom_prod
        self.description = description
        self.quantite = quantite
        self.prix_unit = prix_unit

    def getOne(code_prod:str,db):
        res=db.produits.find_one({"code_prod":code_prod})
        if res==None: return None
        p = Produit(res["nom_prod"],res["description"],res["quantite"],res["prix_unit"])
        p.code_prod=res["code_prod"]
        return p


    def ajouter(self,db):
        db.produits.insert_one(self.__dict__)
    

    def supprimer(self,db):
        db.produits.delete_one({"code_prod":self.code_prod})

    def get(db):
        return list(db.produits.find({},{"_id":0}))
    
    def modifier(self,nouveauProduit,db):
        print("news : ",nouveauProduit)
        db.produits.update_one({"code_prod":self.code_prod},{ '$set' : 
        nouveauProduit
        })
        return Produit.getOne(self.code_prod,db)

  