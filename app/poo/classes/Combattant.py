class Combattant():
    def __init__(self):
        self.list_personnages = []

    def visualiser_personnage(self):
        print("== VOIR LES PERSONNAGES ==")
        for personnage in self.list_personnages:
            print(self.list_personnages.index(personnage)+1,end=" :")
            personnage.to_string()
    
    def ajout_personnage(self, personnage):
        self.list_personnages.append(personnage)
    
    def suppression_personnage(self,index):
        self.list_personnages.pop(index)

    def recuperer_personnage(self,nb) :
          for personnage in self.list_personnages:
              if self.list_personnages.index(personnage) == nb:
                  return personnage
    def organiser_combat(self,attaquant,victime):
        result_attaque = attaquant.combattre(victime)
        if result_attaque == True:
            self.list_personnages.remove(victime)            
