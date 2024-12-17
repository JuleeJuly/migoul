class Objet():
    def __init__(self,nom,quantite):
        self.nom = nom
        self.quantite = quantite
    def to_string(self):
        print("Objet : ",self.nom,", Quantité : ",self.quantite)
