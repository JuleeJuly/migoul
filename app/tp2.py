inventaire = [
    {"nom": "Boules de Noël", "quantite": 50, "prix": 1.5},
    {"nom": "Guirlandes", "quantite": 30, "prix": 3.0},
    {"nom": "Sapin de Noël", "quantite": 10, "prix": 25.0}]

def affichage_menu():
    print("== MENU PRINCIPAL ==")
    print("1. Afficher inventaire")
    print("2. Ajouter un produit")
    print("3. Supprimer un produit")
    print("4. Modifier la quantité d'un produit")
    print("5. Rechercher un produit")
    print("6. Valeur totale inventaire")
    print("7. Quitter le programme")
    choix_menu()

def choix_menu():
    choix = int(input("Votre choix : "))
    produit = {}
    match choix:
        case 1:
            afficher_inventaire()
            affichage_menu()
        case 2:
            nom = str(input("Nom : "))
            quantite = int(input("Quantité : "))
            prix = float(input("Prix : "))
            ajouter_produit(nom,quantite,prix)
            affichage_menu()
        case 3:
            print("== SUPPRIMER UN PRODUIT ==")
            produit = selection_produit()
            supprimer_produit(produit)
            affichage_menu()
        case 4:
            afficher_inventaire()
            print("== MODIFIER UN PRODUIT ==")
            produit = selection_produit()
            quantite = int(input("Quantité : "))
            modifier_quantite(produit,quantite)
            affichage_menu()
        case 5:
            nom_produit = input("Nom du produit : ")
            recherche(nom_produit)
            affichage_menu()
        case 6:
            valeur_totale()
            affichage_menu()
        case _:
            exit()


def selection_produit():
    afficher_inventaire()
    nb = int(input("Quelle produit ? : "))-1
    return inventaire[nb]

def afficher_inventaire():
    print("== VOIR L INVENTAIRE ==")
    for i in inventaire:
        print("Produit n°",inventaire.index(i)+1," - Nom : ",i["nom"]," - Quantité : ",i["quantite"]," - Prix : ",i["prix"])

def ajouter_produit(nom,quantite,prix):
    print("== AJOUTER UN PRODUIT ==")
    for item in inventaire:
        if item["nom"] == nom:
            item["quantite"] = quantite
            return
    inventaire.append({"nom":nom,"quantite":quantite,"prix":prix})    

def supprimer_produit(produit):
    inventaire.remove(produit)
    print("Le produit est supprimé ! ")

def modifier_quantite(produit,quantite):
    produit["quantite"] = quantite 

def recherche(nom_produit):
    for i in inventaire:
        if i["nom"] == nom_produit:
            print("Numero de produit : ",inventaire.index(i)," Nom : ",i["nom"]," Quantité : ",i["quantite"]," Prix : ",i["prix"])
            return
    print("Le produit n'existe pas !")

def valeur_totale():
    total = 0
    for i in inventaire:
        total += i["quantite"]*i["prix"]
    print("Valeur totale de l'inventaire : ",total)
affichage_menu()