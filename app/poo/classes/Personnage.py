from classes.Objet import Objet
import random

class Personnage():
    def __init__(self,nom,classe,niveau,pdv,max_pdv,inventaire):
        self.nom = nom
        self.classe = classe
        self.niveau = niveau
        self.pdv = pdv
        self.max_pdv = max_pdv
        self.list_objet = []
        potion = Objet("Potion",3)
        self.list_objet.append(potion)

    def to_string(self):
        print("Nom : ",self.nom,", Classe : ",self.classe,", Niveau : ",self.niveau,", Points de vie : ",self.pdv,", Maximum de PDV : ",self.max_pdv)

    def modifier_stats(self):
        self.niveau += 1
        self.max_pdv += 20
        self.pdv += 20
    
    def ajouter_objet_inventaire(self,nom,quantite):
        objet = Objet(nom,quantite)
        for element in self.list_objet:
            if element.nom == nom:
                element.quantite += quantite
                return
            self.list_objet.append(objet)

    def afficher_details(self):
        self.to_string()
        for element in self.list_objet:
            element.to_string()

    def utiliser_potion(self):
        print("== UTILISATION POTION ==")
        for objet in self.list_objet:
            if objet.nom == "Potion" and objet.quantite > 0:
                pdv_plus = random.randint(1,50)
                if self.pdv+pdv_plus <= self.max_pdv:
                    self.pdv += pdv_plus
                else :
                    self.pdv = self.max_pdv
                objet.quantite -= 1
            if objet.quantite == 0:
                self.list_objet.remove(objet)
                # personnage["inventaire"].pop(personnage["inventaire"].index(objet))
    
    def combattre(self,victime):
        print("== ATTAQUER ==")
        degats = 10* self.niveau
        victime.pdv -= degats
        if victime.pdv <= 0:
            for objet_inventaire in victime.list_objet:
                self.ajouter_objet_inventaire(objet_inventaire.nom,objet_inventaire.quantite)
            self.modifier_stats()
            return True
        return False