class Commande:
    commandes = []

    def __init__(self, code_cmd: int, code_prod: int, quantite_cmd: int):
        self.code_cmd = code_cmd
        self.code_prod = code_prod
        self.quantite_cmd = quantite_cmd

    @classmethod
    def ajouter(cls, code_cmd: int, code_prod: int, quantite_cmd: int):
        commande = Commande(code_cmd, code_prod, quantite_cmd)
        cls.commandes.append(commande)
        print("Commande ajoutée avec succès.")

    @classmethod
    def afficher_statistiques(cls):
        if not cls.commandes:
            print("Aucune commande enregistrée.")
            return
        stats = {}
        for commande in cls.commandes:
            stats[commande.code_prod] = stats.get(commande.code_prod, 0) + commande.quantite_cmd
        produits_ordonnes = sorted(stats.items(), key=lambda x: x[1], reverse=True)
        print("Produits les plus commandés :")
        for code_prod, quantite in produits_ordonnes:
            print(f"Produit {code_prod} : {quantite} commandes")

    def __repr__(self):
        return f"Commande({self.code_cmd}, {self.code_prod}, {self.quantite_cmd})"
