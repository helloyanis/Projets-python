from inspect import stack
import json
import os
import random

def list_duplicates_of(seq,item):
    start_at = -1
    locs = []
    while True:
        try:
            loc = seq.index(item,start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs



players = []


class Game:

    def __init__(self):
        global game
        self.setNbPlayer()
        self.setCardByPlayer()
        self.setListPlayer()
        for player in self.players:
            self.generateDeck(player)
        print("Ok! Voilà la configuration!")
        tour=1
        win=False
        while(not win):
            print("")
            print("--TOUR "+str(tour)+"--")
            for player in self.players:
                print(player.name+" - "+str(player.deck.getSize())+" cartes dans le deck!")
            Round(self)
            if(self.winCondition()):
                win=True
            else:
                tour+=1
        print(self.winCondition().name+" a récupéré toutes les cartes et a gagné! La partie a duré "+str(tour)+" tours!")
        


    def setPokedex():
        pokemonID = json.load(open("pokemonID.json"))
        for pokemon in pokemonID:
            print(pokemon+" - "+pokemonID[pokemon])
        # Va chercher les fichiers json (pokemonid.json et pokestats.json)

    def setListPlayer(self):
        # Modifie la liste des joueurs
        self.players=[]
        for i in range(self.nbPlayer):
            self.players.append(Player(self))
        return self.players
            
            
    def setNbPlayer(self):
        # Modifie le nombre de joueurs
        try:
            self.nbPlayer = int(input("Nombre de joueurs : "))
        except:
            print("Format de réponse incorrecte, veuillez entrer un nombre!")
            return self.setNbPlayer()
        if(self.nbPlayer<2 or self.nbPlayer>10):
            print("Le nombre de joueurs est incorrect, il faut entre 2 et 10 joueurs!")
            return self.setNbPlayer()
        else:
            return self.nbPlayer

    def setCardByPlayer(self):
        global pokemonID
        # Modifie le nombre de cartes par joueurs
        try:
            self.cardByPlayer = int(input("Nombre de cartes par joueur : "))
        except:
            print("Format de réponse incorrecte, veuillez entrer un nombre!")
            return self.setCardByPlayer()
        if(self.cardByPlayer*self.nbPlayer>len(pokemonID)):
            print("Le nombre de cartes est trop grand, il n'y a pas assez de cartes pour tout le monde! Max : "+str(len(pokemonID)/self.nbPlayer))
            return self.setCardByPlayer()
        else:
            return self.cardByPlayer
        
    def winCondition(self):
        # Condition de victoire (le joueur avec le plus de cartes = winner )
        global pokemonIn
        deckat0=0
        for player in self.players:
            if player.deck.stack.size()==len(pokemonIn):
                return player
            elif player.deck.stack.size()==0:
                deckat0+=1
        if deckat0==len(self.players):
            return True #Partie fini personne gagne
        else:
            return False #Partie pas gagnée
        

    def endGame():
        # If winCondition == True alors il arrête le partie et affiche les stats et demande si la partie doit être relancer
        pass

    def generateDeck(self,player):
        # Génère le deck d'un joueur
        player.deck=Deck(self)
        return player.deck.stack



class Player:
#Besoin name et deck

    def __init__(self,game):
        self.setName(game)
            

    def getDeck(self):
        # Obtiens le deck
        return self.deck

    def getName(self):
        # Donne les noms des joueurs
        return self.name

    def setName(self,game):
        # Set le nom du joueur
        name = ((str(input("Veuillez donner le nom du joueur "+str(len(game.players)+1)+" : "))))
        for player in game.players:#ok ca marche ca
            if player.name==name:
                print("Ce joueur existe déjà! Choisir un autre nom SVP!")
                return self.setName(game)
        self.name=name
                


class Deck:

    def __init__(self,game):
        self.stack=Stack()
        for i in range(game.cardByPlayer):
            randomcard=Card()
            self.stack.push(randomcard)
            

    def getSize(self):
        # Retourne la taille du deck en int
        return self.stack.size()

    def addCardAtBottom(self,liste,deck):
        liste=[x for xs in liste for x in xs]#Permet d'avoir les liste non-nestées
        #print(liste)
        #liste=[Card("isdummy"),Card("isdummy")]test suppr dummy
        # Recup la liste des cartes gagnées pour la mélanger(shuffleList) et l'ajouter au deck
        gotlist=0
        while gotlist<len(liste):#dégage les dummy
            if liste[gotlist].id==0:
                liste.pop(gotlist)
            else:
                gotlist+=1
        #print(liste)
        random.shuffle(liste)
        deck.stack_reverse()
        for i in range(len(liste)):
            deck.push(liste[i])
        deck.stack_reverse()
        return deck

    def getTopCard():
        # Recup et supprime la première carte
        pass

    def helpPokemon():
        # Le joueur à 30% de chances de piocher 2 cartes
        pass


class Card:
    def __init__(self,isdummy=None):
        if isdummy!="isdummy":
            global pokemonID, pokemonIn, pokemonLeft
            # print(list(pokemonID.values())[int(random.choice(list(pokemonID.keys())))])
            pokemonleftid=random.choice(list(pokemonLeft.keys()))
            stats = self.setAttribut(pokemonleftid)
            pokemonLeft.pop(str(stats["id"]))
            pokemonIn.update({str(stats["id"]):str(stats["name"])})
            # for pokemon in pokemonID:
            #   print(pokemon+" - "+pokemonID[pokemon])
            # Va chercher les fichiers json (pokemonid.json et pokestats.json)

        else:
            self.id=0
            self.attack=0
            self.name="dummy"
            

    # Attribut en string
    def setAttribut(self, idpoké):
        # Retourne la stat de l'attribut choisis en string
            global pokemonID
            global pokemonStat
            self.id = idpoké
            self.attack = pokemonStat[str(idpoké)]["attack"]
            self.name = pokemonID[idpoké]
            return {"id": self.id, "attack": self.attack, "name": pokemonID[idpoké]}


class Stats:
    # [{}] Un dico pour chaque parties dans la liste, k: nom joueur v: bool true si c'est le gagnant
    liste = []  # Initialise une liste des statistiques de la partie

    def __init__():
        pass

    def getNbRound():
        # Donne le nombre de tour
        pass

    def getWinner():
        # Retourne le gagnant final
        pass

    def getStats():
        # Affiche les stats de la partie
        pass


class Round:

    def __init__(self,game):
        self.cardsplayed=[]
        self.pickCards(game)
    
    def pickCards(self,game):
        #Pioche les cartes (et éventuellement un helper)
        for player in game.players:
            if player.getDeck().stack.size() != 0:
                self.cardsplayed.append([player.getDeck().stack.pop()])
                if(random.choice([1,2,3])==3 and player.deck.stack.size()>1):
                    self.cardsplayed[-1].append(player.getDeck().stack.pop())
            else:
                self.cardsplayed.append([Card("isdummy")])
        self.printRound(game)
        winner=self.getWinner(game)
        if winner!=True:
            print(winner+" a gagné et remporte toutes les cartes en jeu!")
            for player in game.players:
                if player.name==winner:
                    player.deck.addCardAtBottom(self.cardsplayed,player.deck.stack)
        else:
            print("Hein! Ca c'est rare, il y a une égalité et personne ne peut contrer car le deck de toutes les personnes avec égalité sont vide!")
    
    def printRound(self,game):
        #Affiche les infos du round
        i=0
        envoieliste=["envoie un","lance","attaque avec","utilise","envoie sa pokéball, et il en sort un"]
        introcri=["qui hurle","qui crie","qui lance son cri de guerre :","et il casse les oreilles de tout le monde en disant ","et il hurle"]
        cri1=["svp me tuez pas","JE VAIS TE TUER","PIKATCHOUM MEILLEUR POKEMON","Tremblez devant ma puissance!","Je suis le meilleur!!","J'adore manger des donuts!"]
        cri2=["Je vais t'aider!","Je suis ton plus grand fan!","Laisse moi t'aider à le tuer ce sale mioche","J'adore tes chaussures!"]
        for player in game.players:
            playercard=self.cardsplayed[i]
            if(len(playercard)==1):
                card=playercard[0]
                if(card.id==0):
                    #dummy handle
                    print(player.name+" regarde sans rien faire car son deck est vide!")
                else:
                    print(player.name+" "+random.choice(envoieliste)+" "+str(card.name)+" - Attaque "+str(card.attack)+" "+random.choice(introcri)+" \""+random.choice(cri1)+"\"")
            elif len(playercard)==2:
                card1=playercard[0]
                card2=playercard[1]
                print(player.name+" "+random.choice(envoieliste)+" "+str(card1.name)+" - Attaque "+str(card1.attack)+" "+random.choice(introcri)+" \""+random.choice(cri1)+"\" qui se fait aider par "+str(card2.name)+" - Attaque "+str(card2.attack)+" "+random.choice(introcri)+" \""+random.choice(cri2)+"\" pour une puissance totale de "+str(int(card1.attack+card2.attack))+"!")

            i+=1

    def getWinner(self,game):
        # Renvoie le gagnant du round
        i=0
        atkvalue={}
        for player in game.players:
            card=self.cardsplayed[i]
            if(len(card)==1):
                atkvalue[player.name]=card[0].attack
            elif len(card)==2:
                atkvalue[player.name]=card[0].attack+card[1].attack
            else:
                #dummy!!!
                continue
            i+=1
        #atkvalue={"a":5,"b":5,"c":5,"d":5}
        if list(atkvalue.values()).count(max(atkvalue.values()))==1:
            #Pas d'éga
            return list(atkvalue.keys())[list(atkvalue.values()).index(max(atkvalue.values()))]
        else:
            #Ega donc on remet un tour
            return self.handleTie(game,atkvalue)
    
    def handleTie(self,game,atkvalue):
        tied = [k for k, v in atkvalue.items() if v == max(atkvalue.values())]
        print("Des joueurs sont a égalité! ",end="")
        for player in game.players:
            if player.name in tied:
                print(player.name,end=" ")
        print()
        totalTie=True
        for player in game.players:
            if player.name in tied:
                #Piocher une carte en plus
                newcard=self.cardOver(game,player,tied,atkvalue)
                if newcard:
                    totalTie=False
                    print(player.name+" contre avec "+newcard.name+" avec une attaque de "+str(newcard.attack)+", pour une puissance totale de "+str(atkvalue[player.name]))
                else:
                    tied.remove(player.name)
                    print(player.name+" ne peut pas contrer car il n'y a pas de carte dans son deck!")
        if totalTie:
            return True
        else:
            tied=[]
            return self.checkWinAfterTie(atkvalue,game)
            
    
    def checkWinAfterTie(self,atkvalue,game):
        #atkvalue={"a":5,"b":5,"c":5,"d":4}
        if list(atkvalue.values()).count(max(atkvalue.values()))==1:
            #Pas d'éga
            return list(atkvalue.keys())[list(atkvalue.values()).index(max(atkvalue.values()))]
        else:
            #Ega donc on remet un tour
            return self.handleTie(game,atkvalue)
    
    def cardOver(self,game,player,tied,atkvalue):
        #Remet une carte au dessus
        try:
            newcard=player.getDeck().stack.pop()
            self.cardsplayed.append([newcard])
            atkvalue[player.name]+=newcard.attack
            return newcard
        except:
            
            return False#Plus de carte dans le deck!

    def powerPokemon():
        # Fonction qui s'active seulement lorsqu'un pokemon aide et additionne la puissance des 2 cartes
        pass


class Stack:
    def __init__(self):
        self.elements = []

    def push(self, data):
        self.elements.append(data)
        return data

    def pop(self):
        return self.elements.pop()

    def top(self):
        return self.elements[-1]

    def is_empty(self):
        return len(self.elements) == 0

    def size(self):
        return len(self.elements)

    def print(mystack):
        pass

    def stack_reverse(self):
        return self.elements.reverse()

    # Remplace l'élement au top par "newvalue" et return la stack
    def stack_top_replace(my_stack, newvalue):
        pass

    # Remplace l'élement au bottom par "newvalue" et return la stack
    def stack_bottom_replace(my_stack, newvalue):
        pass

    # Return True si la première stack est similaire à la seconde
    def stack_is_same(my_stack1, my_stack2):
        pass

    # push dans mystack les élements de liste
    def multipush(mystack, liste):
        pass

    # Remove the max
    def removeTheMax(mystack):
        pass

    # Remove the min
    def removeTheMin(mystack):
        pass

    # verifie la bonne syntaxe des parenthèses, crochets et accolades
    #PARAM : String
    # RETURN : True si le parenthésage est OK.
    #         False sinon
    test1 = "{}"  # True
    test2 = "[]"  # True
    test3 = "()"  # True
    test4 = "[({})]"  # True
    test5 = "[[[()()]]]"  # True
    test6 = "[(())]{"  # False
    test7 = "[()]{()}"  # True
    test8 = "]()()()["  # False
    test9 = ""  # True
    test10 = "[(})]"  # False
    test11 = "[[((())]]"

    def goodsyntax(s):
        pass


pokemonID = json.load(open("pokemonID.json"))
pokemonStat = json.load(open("pokemonStat.json"))
pokemonLeft=json.load(open("pokemonID.json"))
pokemonIn={}

class Main:
    def __init__(self):
        # Début de la partie
        #print("./music/"+random.choice(os.listdir("./music")))
        #os.startfile(".\\music\\"+random.choice(os.listdir("./music")))
        Game()
        while(str(input("Voulez-vous rejouer? (O/N)"))).lower()!="n":
            global pokemonLeft,pokemonIn
            pokemonLeft=json.load(open("pokemonID.json"))
            pokemonIn={}
            Game()
        return print("A plus tard!")
        

    def StartStats(stats):
        # Initialise les stats
        pass

    
Main()
