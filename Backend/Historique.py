class Historique:
    commandes = []
    factures = []

    @classmethod
    def ajouter_commande(cls, commande):
        cls.commandes.append(commande)

    @classmethod
    def ajouter_facture(cls, facture):
        cls.factures.append(facture)

    @classmethod
    def afficher_historique(cls):
        print("\n--- Historique des Commandes ---")
        for commande in cls.commandes:
            print(commande)
        print("\n--- Historique des Factures ---")
        for facture in cls.factures:
            print(facture)
