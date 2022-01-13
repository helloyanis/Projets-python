#Si la sortie est bloqué le héros aura tendance a l'éviter pour éviter le piège, et va finir par être bloqué
import random
import time
import os
def genmap(n, difficulty):#Génère la map
    global board,stepped,herocoords,goalcoords
    for i in range(n):#vertical
        for j in range(n):#horizontal
            if i==n-1 and j==n-1:
                print("EXIT ",end="")
                goalcoords=(j,i)
                board[j,i]="x"
                stepped[j,i]=False
            elif i==0 or j==0 or i==n-1 or j==n-1:
                print("# ",end="")
                board[j,i]="#"
                stepped[j,i]=True
            elif i==1 and j==1:
                print("S ",end="")
                board[j,i]="S"
                stepped[j,i]=True
                herocoords=(j,i)
            elif random.choice([1,2,3,5,7,9,10])%2==0:
                board[j,i]=5
                stepped[j,i]=False
                print("o ", end="")
            elif random.choice([1,2,3,5,7,9,10])%2==0:
                board[j,i]=10
                stepped[j,i]=False
                print("m ",end="")
            else:
                board[j,i]=1
                stepped[j,i]=False
                print("  ",end="")
        print()

def display():#Affiche la map
    global board
    line=0
    for i in list(board.keys()):
        if i[1]>line:
            print()
            line+=1
        if i==herocoords:
            print("H",end=" ")
        elif type(board[i])==str:
            print(board[i],end=" ")
        else:
            match (board[i]):
                case 1:
                    print(" ",end=" ")
                case 5:
                    print("O",end=" ")
                case 10:
                    print("M",end=" ")
                case _:
                    print("?",end=" ")

def avilable(j,i):#Donne les cases sur lesquelles on peut se déplacer, donc pas les limites du terrain ou les cases ou on s'est deja rendu
    global board,stepped
    avilable={}
    if type(board[j-1,i]) is int and not stepped[j-1,i]:
        avilable["LEFT"]=board[j-1,i]
    if type(board[j+1,i]) is int and not stepped[j+1,i]:
        avilable["RIGHT"]=board[j+1,i]
    if type(board[j,i-1]) is int and not stepped[j,i-1]:
        avilable["UP"]=board[j,i-1]
    if type(board[j,i+1]) is int and not stepped[j,i+1]:
        avilable["DOWN"]=board[j,i+1]
    if type(board[j-1,i+1]) is int and not stepped[j-1,i+1]:
        avilable["DL"]=board[j-1,i+1]#Down left
    if type(board[j-1,i-1]) is int and not stepped[j-1,i-1]:
        avilable["UL"] =board[j-1,i-1]#Up left
    if ((type(board[j+1,i+1]) is int) or board[j+1,i+1]=="x") and not stepped[j+1,i+1]:
        avilable["DR"]=board[j+1,i+1]
    if type(board[j+1,i-1]) is int and not stepped[j+1,i-1]:
        avilable["UR"]=board[j+1,i-1]
    
    
    return avilable
    

def step():#Fait bouger le héros
    global herocoords,board,stepped,goalcoords
    av=avilable(herocoords[0],herocoords[1])
    stepped[herocoords[0],herocoords[1]]=True
    #Vérifie si on est sur la dernière case
    if herocoords==(goalcoords[0]-1,goalcoords[1]-1):
        print("Le héros est arrivé à la fin du parcours! Bravo!")
        return True
    #Regarde si la case adjascente est la case adjascente à l'arrivée (pour ne pas qu'il évite le piège si il y en a un)
    if (herocoords[0]==goalcoords[0]-2 or herocoords[0]==goalcoords[0]-1) and (herocoords[1]==goalcoords[1]-2 or herocoords[1]==goalcoords[1]-1):
        herocoords=(goalcoords[0]-1,goalcoords[1]-1)
        return False
    #Vérifier la case ↘️
    if "DR" in av:
        if av["DR"]==1 or (not "RIGHT" in av and not "DOWN" in av and not "DL" in av and not "UR" in av and not "UP" in av and not "UL" in av and not "LEFT" in av) :
            #la case est vide
            herocoords=(herocoords[0]+1,herocoords[1]+1)#↘️
        elif av["DR"]==5:
                #la case est un mur
                if "RIGHT" in av:
                    if av["RIGHT"]==1:
                        herocoords=(herocoords[0]+1,herocoords[1])#➡️
                        return False
                if "DOWN" in av:
                    if av["DOWN"]==1:
                        herocoords=(herocoords[0],herocoords[1]+1)#⬇️
                        return False
                if "UR" in av:
                    if av["UR"]==1:
                        herocoords=(herocoords[0]+1,herocoords[1]-1)#↗️
                        return False
                if "DL" in av:
                    if av["DL"]==1:
                        herocoords=(herocoords[0]-1,herocoords[1]+1)#↘️
                        return False
                
                
                
                
                
                
                herocoords=(herocoords[0]+1,herocoords[1]+1)#↘️
                return False
                
                
        elif av["DR"]==10:
            #la case est de l'eau
            if "RIGHT" in av:
                if av["RIGHT"]==1:
                    herocoords=(herocoords[0]+1,herocoords[1])#➡️
                    return False
            if "DOWN" in av:
                if av["DOWN"]==1:
                    herocoords=(herocoords[0],herocoords[1]+1)#⬇️
                    return False
            if "UR" in av:
                if av["UR"]==1:
                    herocoords=(herocoords[0]+1,herocoords[1]-1)#↗️
                    return False
            if "DL" in av:
                if av["DL"]==1:
                    herocoords=(herocoords[0]-1,herocoords[1]+1)#↘️
                    return False
            if "RIGHT" in av:
                if av["RIGHT"]==5:
                    herocoords=(herocoords[0]+1,herocoords[1])#➡️
                    return False
            if "DOWN" in av:
                if av["DOWN"]==5:
                    herocoords=(herocoords[0],herocoords[1]+1)#⬇️
                    return False
            if "UR" in av:
                if av["UR"]==5:
                    herocoords=(herocoords[0]+1,herocoords[1]-1)#↗️
                    return False
            if "DL" in av:
                if av["DL"]==5:
                    herocoords=(herocoords[0]-1,herocoords[1]+1)#↙️
                    return False
            else:
                herocoords=(herocoords[0]+1,herocoords[1]+1)#↘️
                return False
    #
    elif "DOWN" in av:
        #Vérifie la case ⬇️
        if av["DOWN"]==1 or (not "RIGHT" in av and not "DL" in av and not "UR" in av and not "UP" in av and not "UL" in av and not "LEFT" in av) :
            
            herocoords=(herocoords[0],herocoords[1]+1)#⬇️
        elif av["DOWN"]==5:
                if "DL" in av:
                    if av["DL"]==1:
                        herocoords=(herocoords[0]-1,herocoords[1]+1)#↙️
                        return False
                if "LEFT" in av:
                    if av["LEFT"]==1:
                        herocoords=(herocoords[0]-1,herocoords[1])#⬅️
                        return False
                
                
                #if "UR" in av:
                    #if av["UR"]==1:
                        #herocoords=(herocoords[0]+1,herocoords[1]-1)#↗️
                        #if herocoords==goalcoords:
                            #return True
                        #else:
                            #return False
                
                herocoords=(herocoords[0],herocoords[1]+1)#⬇️
                return False
        elif av["DOWN"]==10:
            #Vérifie la case ⬇️
            if "DL" in av:
                if av["DL"]==1:
                    herocoords=(herocoords[0]-1,herocoords[1]+1)#↘↙️
                    return False
            
            if "RIGHT" in av:
                if av["RIGHT"]==1:
                    herocoords=(herocoords[0]+1,herocoords[1])#➡️
                    return False
            if "LEFT" in av:
                if av["LEFT"]==1:
                    herocoords=(herocoords[0]-1,herocoords[1])#⬅️
                    return False
            if "DL" in av:
                if av["DL"]==5:
                    herocoords=(herocoords[0]-1,herocoords[1]+1)#↘↙️
                    return False
            
            if "RIGHT" in av:
                if av["RIGHT"]==5:
                    herocoords=(herocoords[0]+1,herocoords[1])#➡️
                    return False
            if "LEFT" in av:
                if av["LEFT"]==5:
                    herocoords=(herocoords[0]-1,herocoords[1])#⬅️
                    return False
            
            
            herocoords=(herocoords[0],herocoords[1]+1)#⬇️
            return False
                
                
        
        
    elif "RIGHT" in av:
        #Vérifie la case ➡️
        if av["RIGHT"]==1 or (not "DL" in av and not "UR" in av and not "UP" in av and not "UL" in av and not "LEFT" in av) :
            
            herocoords=(herocoords[0]+1,herocoords[1])#➡️
        elif av["RIGHT"]==5:
                if "RIGHT" in av:
                        if av["RIGHT"]==1:
                            herocoords=(herocoords[0]+1,herocoords[1])#➡️
                            return False
                        
                if "UR" in av:
                    if av["UR"]==1:
                        herocoords=(herocoords[0]+1,herocoords[1]-1)#↗️
                        return False
                if "UP" in av:
                    if av["UP"]==1:
                        herocoords=(herocoords[0]+1,herocoords[1]-1)#⬆️
                        return False
                if "UL" in av:
                    if av["UL"]==1:
                        herocoords=(herocoords[0]-1,herocoords[1]-1)#↗️
                        return False
                
                herocoords=(herocoords[0]+1,herocoords[1])#➡️
                return False
        elif av["RIGHT"]==10:
            if "RIGHT" in av:
                if av["RIGHT"]==1:
                    herocoords=(herocoords[0]+1,herocoords[1])#➡️
                    return False
                    
            
            if "UR" in av:
                    if av["UR"]==1:
                        herocoords=(herocoords[0]+1,herocoords[1]-1)#↗️
                        return False
            if "UP" in av:
                if av["UP"]==1:
                    herocoords=(herocoords[0]+1,herocoords[1]-1)#⬆️
                    return False
            
            
            
            if "RIGHT" in av:
                if av["RIGHT"]==5:
                    herocoords=(herocoords[0]+1,herocoords[1])#➡️
                    return False
                    
                    
                    
            if "UR" in av:
                    if av["UR"]==5:
                        herocoords=(herocoords[0]+1,herocoords[1]-1)#↗️
                        return False
            if "UP" in av:
                if av["UP"]==5:
                    herocoords=(herocoords[0]+1,herocoords[1]-1)#⬆️
                    return False
            
            
            
            herocoords=(herocoords[0]+1,herocoords[1])#➡️
            return False
    else:
        print("Le héros s'est perdu et est mort de faim dans d'atroces souffrances")
        return True
        

clear = lambda: os.system('cls')
board={}#Le tableau de jeu, qui est sous la forme {(0,0):"#",(0,1):"#",etc...} Les chiffres dedans sont la valeur des obstacles
stepped={}#Le tableau des cases déjà visitées sous la forme {(0,0):True,(0,1):True,etc...} Cela évite de revenir sur une case déjà visitée
"""
genmap(20,10)
print(board)
print(avilable(1,1))
print(herocoords)
step()
print(herocoords)
display()
"""
genmap(30,3)
points=0
while not step():
    clear()
    display()
    points+=board[herocoords]
    print("Nombre de points : "+str(points))
    time.sleep(0.5)
    
