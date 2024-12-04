class Produit:
    produits = []

    def __init__(self, code_prod: int, nom_prod: str, description: str, quantite: int, prix_unit: float):
        self.code_prod = code_prod
        self.nom_prod = nom_prod
        self.description = description
        self.quantite = quantite
        self.prix_unit = prix_unit

    @classmethod
    def ajouter(cls, code_prod: int, nom_prod: str, description: str, quantite: int, prix_unit: float):
        produit = Produit(code_prod, nom_prod, description, quantite, prix_unit)
        cls.produits.append(produit)
        print("Produit ajouté avec succès.")

    @classmethod
    def afficher(cls):
        if not cls.produits:
            print("Aucun produit disponible.")
            return
        print("Liste des produits (triés par nom) :")
        for produit in sorted(cls.produits, key=lambda p: p.nom_prod):
            print(produit)

    @classmethod
    def supprimer(cls, code_prod: int):
        cls.produits = [p for p in cls.produits if p.code_prod != code_prod]
        print(f"Produit avec code {code_prod} supprimé.")

    def __repr__(self):
        return f"Produit({self.code_prod}, {self.nom_prod}, {self.quantite}, {self.prix_unit})"
