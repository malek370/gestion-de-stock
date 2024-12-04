class Facture:
    factures = []

    def __init__(self, code_facture: int, code_cmd: int, montant_total: float):
        self.code_facture = code_facture
        self.code_cmd = code_cmd
        self.montant_total = montant_total

    @classmethod
    def creer_facture(cls, code_facture: int, code_cmd: int, montant_total: float):
        facture = Facture(code_facture, code_cmd, montant_total)
        cls.factures.append(facture)
        print("Facture créée avec succès.")

    @classmethod
    def afficher_factures(cls):
        if not cls.factures:
            print("Aucune facture disponible.")
            return
        print("Liste des factures:")
        for facture in cls.factures:
            print(facture)

    def __repr__(self):
        return f"Facture({self.code_facture}, {self.code_cmd}, {self.montant_total})"
