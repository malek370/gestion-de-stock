import uuid
from ProduitCommande import ProduitCommande
from Produit import Produit
class Commande:

    def __init__(self,titre:str,description:str):

        self.code_cmd = uuid.uuid4().hex
        self.titre = titre
        self.description=description
        self.items = []

    def getOne(code_cmd:str,db):
        res=db.commandes.find_one({"code_cmd":code_cmd})
        if res==None: return None
        c = Commande("","")
        c.code_cmd=res["code_cmd"]
        c.description=res["description"]
        c.titre=res["titre"]
        c.items=list(res["items"])
        return c

    def ajouterProduit(self,produit:Produit,quantite:int,db):
        if produit.quantite<quantite :
            return False
        print("enter modif with :",self.__dict__)
        produit.modifier({"quantite":produit.quantite-quantite},db)
        self.items.append(ProduitCommande(produit.code_prod,produit.nom_prod,quantite).__dict__)
        db.commandes.update_one({"code_cmd":self.code_cmd},{ '$set' : 
        self.__dict__
        })
        return True

    def ajouter(self,db):
        db.commandes.insert_one(self.__dict__)
        print("Commande ajoutée avec succès.")

    def supprimer(self,db):
        db.commandes.delete_one({"code_cmd":self.code_cmd})

    # @classmethod
    # def afficher_statistiques(cls):
    #     if not cls.commandes:
    #         print("Aucune commande enregistrée.")
    #         return
    #     stats = {}
    #     for commande in cls.commandes:
    #         stats[commande.code_prod] = stats.get(commande.code_prod, 0) + commande.quantite_cmd
    #     produits_ordonnes = sorted(stats.items(), key=lambda x: x[1], reverse=True)
    #     print("Produits les plus commandés :")
    #     for code_prod, quantite in produits_ordonnes:
    #         print(f"Produit {code_prod} : {quantite} commandes")

    def get(db):
        return list(db.commandes.find({},{"_id":0}))

    def modifier(self,nouvCmd,db):
        db.commandes.update_one({"code_cmd":self.code_cmd},{ '$set' : 
        nouvCmd
        })
        return True

    def __repr__(self):
        return f"Commande({self.code_cmd}, {self.code_prod}, {self.quantite_cmd})"
