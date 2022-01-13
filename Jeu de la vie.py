import copy
import os
import random
import time
clear = lambda: os.system('cls') #Pour effacer la console


def voisin(tabl, x, y):
    if x == 0:
        leftedge = True
    else:
        leftedge = False
    if x == len(tabl[y]) - 1:
        rightedge = True
    else:
        rightedge = False
    if y == 0:
        topedge = True
    else:
        topedge = False
    if y == len(tabl) - 1:
        bottomedge = True
    else:
        bottomedge = False

    #

    voisins = 0

    if not leftedge:
        # Voisin a gauche
        if tabl[y][x - 1]:
            voisins += 1
        if not topedge:
            # Voisin en haut a gauche
            if tabl[y - 1][x - 1]:
                voisins += 1
        if not bottomedge:
            # Voisin en bas a gauche
            if tabl[y + 1][x - 1]:
                voisins += 1
    if not rightedge:
        # Voisin a droite
        if tabl[y][x + 1]:
            voisins += 1
        if not topedge:
            # Voisin en haut a droite
            if tabl[y - 1][x + 1]:
                voisins += 1
        if not bottomedge:
            # Voisin en bas a droite
            if tabl[y + 1][x + 1]:
                voisins += 1
    if not topedge:
        # Voisin en haut
        if tabl[y - 1][x]:
            voisins += 1
    if not bottomedge:
        # Voisin en bas
        if tabl[y + 1][x]:
            voisins += 1
    return voisins


def step(tabl,steps=False):
    
    if steps:
        steps-=1
    editing = copy.deepcopy(tabl)
    for y in range(len(tabl)):
        for x in range(len(tabl[y])):
            if tabl[y][x]:
                if voisin(tabl, x, y) <= 1 or voisin(tabl, x, y) >= 4:
                    editing[y][x] = False
                    print(" ", end=" ")
                else:
                    print("■", end=" ")
            else:
                if voisin(tabl, x, y) == 3:
                    editing[y][x] = True
                    print("■", end=" ")
                else:
                    print(" ", end=" ")
        print()
    time.sleep(0.2)
    if not steps:
        """
        Enlever le # sur la ligne 85 pour que le programme s'arrête une fois une seul étape finie ou bien une fois que le nombre d'étapes défini dans la fonction est passé
        (pour vérifier le temps
        """
        #return
        if editing==tabl:
            print("Votre tableau de jeu ne va plus changer, donc vous pouvez arrêter maintenant si vous voulez.")
            return
        #
        else:
            clear()
            return editing
        #
        input("Entrée pour l'étape suivante...")
        clear()
        return editing
    else:
        print("--Etape suivante (reste "+str(steps)+")--")
        return [editing,steps]


clear()
h=int(input("Pour générer un tableau de jeu aléatoire, il me faut le nombre de lignes... "))
v=int(input("Et maintenant, le nombre de colonnes... "))
print("Ok, je suis en train de créer ça, un peu de patience...")
liste=[[random.choice([True,False]) for j in range(0,v)] for i in range(0,h)]
#step([[False, False, False, False, False],[False, True, True, True, False],[False, False, False, False, False]],5)
clear()

while True:
    liste=step(liste)


"""
La fonction step() qui fait une étape du jeu de la vie prend 2 arguments (1 optionel) : 
La liste qui est le tableau du jeu, et le nombre d'étapes à faire d'emblée (optionel) qui effectue un certain nombre d'étapes automatiquement.
Pour un tableau de 3x3 avec une ligne de carrés au milieu le format de la liste est :
[[False,False,False],
 [True,True,True],
 [False,False,False]]
 où True est un carré allumé et False est un carré éteint.
Cela permet de faire un fichier un chouïa plus léger en disant "if not a" au lieu de "if a==(valeur)" pour vérifier si a est false par exemple.

La fonction voisin() peût sûrement être optimisée mais vu que j'avais un peu de mal avec je l'ai divisée en 2 parties
La première partie vérifie si le carré dont on cherche les voisins est sur un bord. Cela évite un out of range si le nombre est au bord du tableau
La deuxième partie prend en compte les résultats de la première partie pour vérifier les voisins.
Cette partie est assez optimisée car il vérifie uniquement les voisins des diagonales si le carré est déjà au bord
Par exemple si le carré est sur le bord gauche, on sait qu'il n'aura pas de voisin en ↙, ️⬅ et ️↖️, donc on passe outre ces vérifications pour gagner du temps.
"""