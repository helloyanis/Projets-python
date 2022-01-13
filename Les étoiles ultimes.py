def starsquare(a):
    for i in range(a):
        for i in range(a):
            print("*", end=" ")
        print()
def starrec(h,l):
    for i in range(h):
        for i in range(l):
            print("*", end=" ")
        print()
def carrevide(a):
        for i in range(a):
            print("*",end=" ")
        print()
        for i in range(a-2):
            print("*", end=" ")
            for i in range(a-2):
                print(" ",end=" ")
            print("*")
        if a>1:
            for i in range(a):
                print("*",end=" ")
        print()
def carrediaginv(a):
        for i in range(a):
            print("*",end=" ")
        print()
        for i in range(a-2):
            print("*", end=" ")
            b=((a-3)-i)
            for i in range(b):
                print(" ",end=" ")
            print("*",end=" ")
            for i in range((a-b)-3):
                print(" ",end=" ")
            print("*")
        if a>1:
            for i in range(a):
                print("*",end=" ")
        print()
def carrediag(a):
        for i in range(a):
            print("*",end=" ")
        print()
        for i in range(a-2):
            print("*", end=" ")
            b=((a-3)-i)
            for i in range((a-b)-3):
                print(" ",end=" ")
            print("*",end="")
            for i in range(b):
                print(" ",end=" ")
            print(" *")
        if a>1:
            for i in range(a):
                print("*",end=" ")
        print()
def carrevidewhile(a):
            b=0
            while b<a:
                b=b+1
                print("*",end=" ")
            print()
            c=0
            while c<(a-2):
                c=c+1
                print("*", end=" ")
                d=0
                while d<(a-2):
                    d=d+1
                    print(" ",end=" ")
                print("*")
            if a>1:
                e=0
                while e<a:
                    print("*",end=" ")
                    e=e+1
            print()
def carrechiffre(a):
    for i in range(a):
        for i in range(a):
            print(i, end=" ")
        print()
def escalier(a):
        print(" _")
        for i in range(a):
            print("|", end=" ")
            b=((a-3)-i)
            for i in range((a-b)-3):
                print(" ",end=" ")
            print("|",end="_")
            print()
        if a>1:
            print("|",end="")
            for i in range(a*2+1):
                print("_",end="")
            print("|", end="")
        print()
        
def fib(n):
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()

def sablier(n):
    for i in range(n):#1e ligne
        print('*', end=' ')
    print()
    b=0
    for i in range(n-2):#Le numéro de la ligne
        print(" ", end=" ")
        for j in range (n-2):# c'est l'enfroit dans la ligne
            if(j==b or j==n-3-b):#J=B pour \ et J=n-3-b pour /
                print('*',end=' ')
            else:
                print(' ',end=' ')
            
        
        print()
        b=b+1
    for i in range(n):#derniere ligne
        print('*', end=' ')
    print()
    
#L'argument est la longueur de la forme
sablier(40)
escalier(15)
carrevide(10)
carrevidewhile(11)
carrediag(13)
carrediaginv(8)