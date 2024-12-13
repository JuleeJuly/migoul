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
    match choix:
        case 0:
            exit()
        case 1:
            creation_personnage()
            affichage_menu()
        case 2:
            suppression_personnage()
            affichage_menu()
        case 3:
            liste_personnage()
            affichage_menu()
        case 4:
            ajout_objet_inventaire()
            affichage_menu()
        case 5:
            attaquer()
            affichage_menu()
        case 6:
            utilisation_potion()
            affichage_menu()
        case 7:
            afficher_personnage()
            affichage_menu()
        case _:
            exit()

def creation_personnage():
    global list_personnage
    personnage = {}
    list_inv =  []
    inv = {}
    print("== AJOUTER UN PERSONNAGE ==")
    personnage["nom"] = input("Nom : ")
    personnage["classe"] = input("Classe : ")
    personnage["niveau"] = 1
    personnage["pdv"] = 30
    personnage["max_pdv"] = 30
    personnage["inventaire"] = list_inv
    inv["nom"] = "Potion"
    inv["quantite"] = 3
    list_inv.append(inv)
    list_personnage.append(personnage)
    print("Le personnnage est ajouté ! ")


def suppression_personnage():
    print("== SUPPRIMER PERSONNAGE ==")
    liste_personnage()
    presence = 0
    while presence == 0:
        if len(list_personnage) == 0:
            print("Il n'y a pas de personnage ! ")
            break
        nb = int(input("Quelle personnage voulez vous supprimer ? : "))-1
        for i in list_personnage:
            if nb == list_personnage.index(i):
                presence = 1
                list_personnage.pop(nb)
                print("Le personnage est supprimé ! ")


def liste_personnage():
    global list_personnage
    print("== VOIR LES PERSONNAGES ==")
    for i in list_personnage:
        print("Perso n°",list_personnage.index(i)+1," - Nom : ",i["nom"])

def afficher_personnage():
    global list_personnage
    print("== VOIR LES DETAILS D'UN PERSONNAGE ==")
    result = int(input("Afficher les détails de quel personnage ? "))-1
    for i in list_personnage:
        if result == list_personnage.index(i):
            afficher_details_personnage(i)

def afficher_details_personnage(personnage):
    print(" Nom : ",personnage["nom"]," / Classe : ",personnage["classe"]," / Niveau : ",personnage["niveau"]," / Pdv : ",personnage["pdv"])
    print("    Inventaire")
    for j in personnage["inventaire"]:
        print("        Objet n°",personnage["inventaire"].index(j)+1," ",j["nom"]," Quantité : ",j["quantite"])

def modifier_stats(index_personnage):
    list_personnage[index_personnage]["niveau"] += 1
    list_personnage[index_personnage]["max_pdv"] += 20
    list_personnage[index_personnage]["pdv"] += 20
def attaquer():
    print("== ATTAQUER ==")
    liste_personnage()
    presence = 0
    while presence == 0:
        if len(list_personnage) >= 2:
            attaquant = int(input("Quel personnage attaque ? : "))-1
            victime = int(input("Quel personnage est victime de l'attaque ? : "))-1
            for i in list_personnage:
                if attaquant == list_personnage.index(i):
                    presence += 1
                if victime == list_personnage.index(i):
                    presence += 1
            if presence == 2:
                degats = 10*int(list_personnage[attaquant]["niveau"])
                list_personnage[victime]["pdv"] -= degats
                if list_personnage[victime]["pdv"] <= 0:
                    for objet_inventaire in list_personnage[victime]["inventaire"]:
                        for objet_inventaire_attaquant in list_personnage[attaquant]["inventaire"]:
                            if objet_inventaire["nom"] == objet_inventaire_attaquant["nom"]:
                                objet_inventaire_attaquant["quantite"] += objet_inventaire["quantite"]
                            else:
                                list_personnage[attaquant]["inventaire"].append(objet_inventaire)
                    list_personnage.pop(victime)
                    modifier_stats(attaquant)
            else:
                print("Personnage inexistant ")
                break   
        else :
            print("Il n'y a pas assez de personnage ! ")
            break

def ajout_objet_inventaire():
    print("== AJOUT OBJET INVENTAIRE ==")
    liste_personnage()
    presence = 0
    while presence == 0:
        if len(list_personnage) == 0:
            print("Il n'y a pas de personnage ! ")
            break
        nb = int(input("Ajouter objet pour quel personnage ? : "))-1
        for i in list_personnage:
            if nb == list_personnage.index(i):
                presence = 1
                inv = {}
                inv["nom"] = input("Nom : ")
                inv["quantite"] = int(input("Quantité : "))
                i["inventaire"].append(inv)
                print("L'objet est ajouté ! ")
def utilisation_potion():
    print("== UTILISATION POTION ==")
    liste_personnage()
    presence = 0
    while presence == 0:
        if len(list_personnage) == 0:
            print("Il n'y a pas de personnage ! ")
            break
        nb = int(input("utiliser potion pour quel personnage ? : "))-1
        for i in list_personnage:
            if nb == list_personnage.index(i):
                presence = 1
                for j in i["inventaire"]:
                    if j["nom"] == "Potion" and j["quantite"] > 0:
                        pdv_plus = random.randint(1,50)
                        if i["pdv"]+pdv_plus <= i["max_pdv"]:
                            i["pdv"] += pdv_plus
                        else :
                            i["pdv"] = i["max_pdv"]
                        j["quantite"] -= 1
                    if j["quantite"] == 0:
                        i["inventaire"].pop(i["inventaire"].index(j))
affichage_menu()