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
    match choix:
        case 1:
            afficher_inventaire()
            affichage_menu()
        case 2:
            ajouter_produit()
            affichage_menu()
        case 3:
            supprimer_produit()
            affichage_menu()
        case 4:
            afficher_inventaire()
            nb_index = int(input("Quel produit voulez vous modifier ? "))
            quantite = int(input("Quantité : "))
            modifier_quantite(nb_index,quantite)
            affichage_menu()
        case 5:
            recherche()
            affichage_menu()
        case 6:
            valeur_totale()
            affichage_menu()
        case _:
            exit()
def afficher_inventaire():
    global inventaire
    print("== VOIR L INVENTAIRE ==")
    for i in inventaire:
        print("Produit n°",inventaire.index(i)," - Nom : ",i["nom"]," - Quantité : ",i["quantite"]," - Prix : ",i["prix"])

def ajouter_produit():
    global inventaire
    produit = {}
    print("== AJOUTER UN PRODUIT ==")
    produit["nom"] = str(input("Nom : "))
    produit["quantite"] = int(input("Quantité : "))
    produit["prix"] = float(input("Prix : "))
    exist = 0
    for i in inventaire:
        # index = inventaire.index(i)
        if i["nom"] == produit["nom"]:
            i["quantite"] = produit["quantite"]
            exist = 1
            print("Le produit est mis à jour ! ")
    if exist == 0:
        inventaire.append(produit)
        print("Le produit est ajouté ! ")

def supprimer_produit():
    global inventaire
    print("== SUPPRIMER UN PRODUIT ==")
    afficher_inventaire()
    nb = int(input("Quel produit voulez vous supprimer ? "))
    for i in inventaire:
        if nb == inventaire.index(i):
            print(inventaire.index(i))
            inventaire.pop(nb)
            print("Le produit est supprimé ! ")

def modifier_quantite(nb_index,quantite):
    global inventaire
    print("== MODIFIER UN PRODUIT ==")
    exist = 0
    # inventaire[nb_index]["quantite"]
    for i in inventaire:
        if nb_index == inventaire.index(i):
            i["quantite"] = quantite
            exist = 1
    if exist == 0:
        print("ERREUR ! ")

def recherche():
    global inventaire
    nom_produit = input("Quel est le produit à chercher ? ")
    exist = 0
    print(nom_produit)
    for i in inventaire:
        if i["nom"] == nom_produit:
            exist = 1
            print("Numero de produit : ",inventaire.index(i)," Nom : ",i["nom"]," Quantité : ",i["quantite"]," Prix : ",i["prix"])
    if exist == 0:
        print("ERREUR ! ")

def valeur_totale():
    global inventaire
    total = 0
    for i in inventaire:
        total += i["quantite"]*i["prix"]
    print("Valeur totale de l'inventaire : ",total)
affichage_menu()