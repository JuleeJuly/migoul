import random
list_personnage = []

def affichage_menu():
    print("== MENU PRINCIPAL ==")
    print("1. Création personnage")
    print("2. Suppression personnage")
    print("3. Afficher liste personnage")
    print("4. Ajouter un objet")
    print("5. Attaquer")
    print("6. Utiliser potion")
    print("7. Afficher details personnage")
    print("0. Quitter le programme")
    choix_menu()

def choix_menu():
    choix = int(input("Votre choix : "))
    personnage = {}
    match choix:
        case 0:
            exit()
        case 1:
            creation_personnage()
            affichage_menu()
        case 2:
            personnage = selection_personnage()
            suppression_personnage(personnage)
            affichage_menu()
        case 3:
            liste_personnage()
            affichage_menu()
        case 4:
            personnage = selection_personnage()
            nom = input("Nom de l'objet : ")
            quantite = int(input("Quantité : "))
            ajout_objet_inventaire(personnage,nom,quantite)
            affichage_menu()
        case 5:
            attaquant = selection_personnage()
            victime = selection_personnage()
            attaquer(attaquant,victime)
            affichage_menu()
        case 6:
            personnage = selection_personnage()
            utilisation_potion(personnage)
            affichage_menu()
        case 7:
            personnage = selection_personnage()
            afficher_details_personnage(personnage)
            affichage_menu()
        case _:
            exit()

def selection_personnage():
    liste_personnage()
    nb = int(input("Quelle personnage ? : "))-1
    return list_personnage[nb]

def creation_personnage():
    global list_personnage
    print("== AJOUTER UN PERSONNAGE ==")
    list_personnage.append({"nom":input("Nom : "),"classe":input("Classe : "),"niveau":1,"pdv":30,"max_pdv":30,"inventaire":[{"nom":"Potion","quantite":3}]})
    print("Le personnnage est ajouté ! ")

def suppression_personnage(personnage):
    print("== SUPPRIMER PERSONNAGE ==")
    list_personnage.remove(personnage)
    print("Le personnage est supprimé ! ")

def liste_personnage():
    global list_personnage
    print("== VOIR LES PERSONNAGES ==")
    for i in list_personnage:
        print("Perso n°",list_personnage.index(i)+1," - Nom : ",i["nom"])

def afficher_details_personnage(personnage):
    print(" Nom : ",personnage["nom"]," / Classe : ",personnage["classe"]," / Niveau : ",personnage["niveau"]," / Pdv : ",personnage["pdv"])
    print("    Inventaire")
    for j in personnage["inventaire"]:
        print("        Objet n°",personnage["inventaire"].index(j)+1," ",j["nom"]," Quantité : ",j["quantite"])

def modifier_stats(personnage):
    personnage["niveau"] += 1
    personnage["max_pdv"] += 20
    personnage["pdv"] += 20

def attaquer(attaquant,victime):
    print("== ATTAQUER ==")
    degats = 10* attaquant["niveau"]
    victime["pdv"] -= degats
    if victime["pdv"] <= 0:
        for objet_inventaire in victime["inventaire"]:
            ajout_objet_inventaire(attaquant,objet_inventaire["nom"],objet_inventaire["quantite"])
        list_personnage.remove(victime)
        modifier_stats(attaquant)

def ajout_objet_inventaire(personnage,nom,quantite):
    print("== AJOUT OBJET INVENTAIRE ==")
    for item in personnage["inventaire"]:
        if item["nom"] == nom:
            item["quantite"] += quantite
            return
    personnage["inventaire"].append({"nom":nom,"quantite":quantite})    
    print("L'objet est ajouté ! ")
                
def utilisation_potion(personnage):
    print("== UTILISATION POTION ==")
    for objet in personnage["inventaire"]:
        if objet["nom"] == "Potion" and objet["quantite"] > 0:
            pdv_plus = random.randint(1,50)
            if personnage["pdv"]+pdv_plus <= personnage["max_pdv"]:
                personnage["pdv"] += pdv_plus
            else :
                personnage["pdv"] = personnage["max_pdv"]
            objet["quantite"] -= 1
        if objet["quantite"] == 0:
            personnage["inventaire"].pop(personnage["inventaire"].index(objet))

affichage_menu()