from Commande import Commande
from Facture import Facture
from Historique import Historique
from Produit import Produit


def menu():
    while True:
        print("\n--- Menu Gestion de Stock ---")
        print("1. Gestion des produits")
        print("2. Gestion des commandes")
        print("3. Gérer les factures")
        print("4. Afficher l'historique")
        print("5. Quitter")
        choix = input("Choisissez une option: ")
        if choix == "1":
            print("\n--- Gestion des Produits ---")
            print("1. Ajouter un produit")
            print("2. Afficher les produits")
            print("3. Supprimer un produit")
            choix_prod = input("Choisissez une option: ")
            if choix_prod == "1":
                code_prod = int(input("Code du produit: "))
                nom_prod = input("Nom du produit: ")
                description = input("Description: ")
                quantite = int(input("Quantité: "))
                prix_unit = float(input("Prix unitaire: "))
                Produit.ajouter(code_prod, nom_prod, description, quantite, prix_unit)
            elif choix_prod == "2":
                Produit.afficher()
            elif choix_prod == "3":
                code_prod = int(input("Code du produit à supprimer: "))
                Produit.supprimer(code_prod)
            else:
                print("Option invalide.")
        elif choix == "2":
            print("\n--- Gestion des Commandes ---")
            print("1. Ajouter une commande")
            print("2. Afficher les statistiques")
            choix_cmd = input("Choisissez une option: ")
            if choix_cmd == "1":
                code_cmd = int(input("Code de la commande: "))
                code_prod = int(input("Code du produit: "))
                quantite_cmd = int(input("Quantité commandée: "))
                commande = Commande(code_cmd, code_prod, quantite_cmd)
                Commande.ajouter(code_cmd, code_prod, quantite_cmd)
                Historique.ajouter_commande(commande)
            elif choix_cmd == "2":
                Commande.afficher_statistiques()
            else:
                print("Option invalide.")
        elif choix == "3":
            print("\n--- Gestion des Factures ---")
            code_facture = int(input("Code de la facture: "))
            code_cmd = int(input("Code de la commande: "))
            montant_total = float(input("Montant total: "))
            facture = Facture(code_facture, code_cmd, montant_total)
            Facture.creer_facture(code_facture, code_cmd, montant_total)
            Historique.ajouter_facture(facture)
        elif choix == "4":
            Historique.afficher_historique()
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Option invalide.")


if __name__ == "__main__":
    menu()
