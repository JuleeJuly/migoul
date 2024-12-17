from classes.Combattant import Combattant
from classes.Personnage import Personnage

def creation_personnage():
    nom = input("Nom : ")
    classe = input("Classe : ")
    personnage = Personnage(nom,classe,1,30,30)
    return personnage

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
    choix = input("Votre choix : ")
    if choix in "01234567" and len(choix) == 1:
        match choix:
            case "0":
                exit()
            case "1":
                combattant.ajout_personnage(creation_personnage())
                affichage_menu()
            case "2":
                combattant.visualiser_personnage()
                nb = int(input("Numéro du personnage à supprimer : "))-1
                combattant.suppression_personnage(nb)
                affichage_menu()
            case "3":
                combattant.visualiser_personnage()
                affichage_menu()
            case "4":
                combattant.visualiser_personnage()
                nb = int(input("Pour quel personnage ? : "))-1
                nom = input("Nom de l'objet : ")
                quantite = int(input("Quantité : "))
                personnage = combattant.recuperer_personnage(nb)
                personnage.ajouter_objet_inventaire(nom,quantite)
                affichage_menu()
            case "5":
                combattant.visualiser_personnage()
                att = int(input("Qui attaque ? : "))-1
                defense = int(input("Qui défend ? : "))-1
                attaquant = combattant.recuperer_personnage(att)
                victime = combattant.recuperer_personnage(defense)
                combattant.organiser_combat(attaquant,victime)
                affichage_menu()
            case "6":
                combattant.visualiser_personnage()
                nb = int(input("Pour quel personnage ? : "))-1
                personnage = combattant.recuperer_personnage(nb)
                personnage.utiliser_potion()
                affichage_menu()
            case "7":
                combattant.visualiser_personnage()
                nb = int(input("Pour quel personnage ? : "))-1
                personnage = combattant.recuperer_personnage(nb)
                personnage.afficher_details()
                affichage_menu()
            case _:
                exit()
    else:
        print("Erreur, réessayez")

combattant = Combattant()
perso1 = Personnage("Jean","Mage",12,180,210)
perso2 = Personnage("Albert","Barbare",10,220,250)
perso1.ajouter_objet_inventaire("Tasse",1)
perso1.ajouter_objet_inventaire("Baguette",2)
perso1.ajouter_objet_inventaire("Tente",1)
perso1.ajouter_objet_inventaire("Livre",5)
perso2.ajouter_objet_inventaire("Chaussette",3)
perso2.ajouter_objet_inventaire("Pomme",2)
perso2.ajouter_objet_inventaire("Poulet",1)
perso2.ajouter_objet_inventaire("Sel",5)
combattant.ajout_personnage(perso1)
combattant.ajout_personnage(perso2)
affichage_menu()