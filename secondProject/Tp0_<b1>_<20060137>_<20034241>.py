# fait par Nahnah Abdesselam et Benchikh Mourad
# j'ai remis le devoir en avance de 5 heurs et puis je me suis rendu compte
# 5 jours aprés que il y'avait une petite erreur de sementique alors je l'ai modifié
#c'est pour ça que c'est affiché remis en retard

class Grille:

    def __init__(self,width=0,height=0):
        self.width=width
        self.height=height
        self.grid= self.createGrid()


    def createGrid(self):
        org=Organisme(".",0,0,0)
        grid=[[org]*self.width for i in range(self.height)]
        return grid


    def printgrid(self):
        for i in self.grid:
            for j in i:
                print(j.couleur," ",end="")

            print()
    # methode qui calcule le nombre de voisins d'une case donnée
    #si nbrVoisin>3 alors une case nait
    #si une case non morte contient < 3 voisins alors elle meurt

    def find_Neighbor(self, i, j,org1,org2,org3):
        counter=0
        if (0<i<(len(self.grid)-1)) and (0<j<len(self.grid[0])-1):

            list=[self.check("top",i,j),self.check("bottom",i,j),self.check("right",i,j),self.check("left",i,j),self.check_diagonal("topLeft",i,j)
                  , self.check_diagonal("topRight",i,j),self.check_diagonal("bottomLeft",i,j),self.check_diagonal("bottomRight",i,j)]


        elif 0<i<(len(self.grid)-1) and j==0:
            list=[self.check("top",i,j),self.check("bottom",i,j),self.check("right",i,j),self.check_diagonal("topRight",i,j)
                  ,self.check_diagonal("bottomRight",i,j)]


        elif 0<i<(len(self.grid)-1) and j==len(self.grid[0])-1:
            list=[self.check("top",i,j),self.check("bottom",i,j),self.check("left",i,j),self.check_diagonal("topLeft",i,j)
                  ,self.check_diagonal("bottomLeft",i,j)]

        elif i==0 and 0<j<len(self.grid[0])-1:
            list=[self.check("left",i,j),self.check("right",i,j),self.check("bottom",i,j),
                  self.check_diagonal("bottomLeft",i,j),self.check_diagonal("bottomRight",i,j)]

        elif i==len(self.grid)-1 and 0<j<len(self.grid[0])-1:
            list=[self.check("left",i,j),self.check("right",i,j),self.check("top",i,j),
                  self.check_diagonal("topLeft",i,j),self.check_diagonal("topRight",i,j)]
        elif i==0 and j==0:
            list=[self.check("right",i,j),self.check("bottom",i,j),self.check_diagonal("bottomRight",i,j)]

        elif i==len(self.grid)-1 and j==0:
            list=[self.check("top",i,j),self.check("right",i,j),self.check_diagonal("topRight",i,j)]

        elif i==0 and j==len(self.grid[0])-1:
            list=[self.check("left",i,j),self.check("bottom",i,j),self.check_diagonal("bottomLeft",i,j)]
        else:
            list=[self.check("top",i,j),self.check("left",i,j),self.check_diagonal("topLeft",i,j)]

        counter = list.count(True)
        cel= Cellule(self.grid,i,j)
        self.update(self.grid, cel, counter, org1, org2, org3)


    #methode qui fait la mise a jour d'une case
    def update(self,grid,cel,counter,org1,org2,org3):
        if cel.etat=="morte":
            if counter==3 :
                if org1.condition_verifier():
                    grid[cel.posX][cel.posY]=org1
                elif org2.condition_verifier():
                    grid[cel.posX][cel.posY]=org2
                else:
                    grid[cel.posX][cel.posY]=org3

        elif counter<2 or counter >3:
            grid[cel.posX][cel.posY]=Organisme(".",0,0,0)




    def cycle(self,org1,org2,org3):

        for i,k in enumerate(self.grid):
            for j,c in enumerate(k) :
                  grid =self.find_Neighbor(i,j,org1,org2,org3)


        print()
        self.printgrid()



    #methode qui verifie si il ya un voisin en haut a gauche en bas ou a droite
    def check(self,position,i,j):
        if position=="top":
            return self.grid[i-1][j].couleur!="."
        elif position=="bottom":
            return self.grid[i+1][j].couleur!="."
        elif position=="right":
            return self.grid[i][j+1].couleur!="."
        else:
            return self.grid[i][j-1].couleur!="."
    #methode qui permet de verifier si il ya des voisins dans les elements de la diagonale
    def check_diagonal(self,position,i,j):
        if position=="topLeft":
            return self.grid[i-1][j-1].couleur!="."
        elif position=="topRight":
            return self.grid[i-1][j+1].couleur!="."
        elif  position=="bottomLeft":
            return self.grid[i+1][j-1].couleur!="."
        else:
            return self.grid[i+1][j+1].couleur!="."


class Cellule:
    def __init__(self,grille=[[]],i=0,j=0):
        self.posX=i
        self.posY=j
        self.grid = grille
        self.etat=self.etat()


    def etat(self):
        if self.grid[self.posX][self.posY].couleur==".":
            return "morte"
        else:
            return "contenant un organisme"

class Organisme:

    def __init__(self,couleur="",a=0,b=0,c=0):
        self.couleur=couleur
        self.a=a
        self.b=b
        self.c=c


    def condition_verifier(self):
        if self.b<=self.a<=self.c:
            return True
        return False


    def set(self,grid,i,j):
        grid[i][j]=self




def openFile():
    org4=Organisme(".",0,0,0)
    with open("rules.txt",encoding="utf-8") as myFile:
            lines=myFile.read().split("\n")
            secLine=lines[0].split(":")
            a,b,c=secLine[1].split(",")
            org1=Organisme(secLine[0],a,b,c)
            secLine=lines[1].split(":")
            org2 = Organisme(secLine[0], a,b,c)
            secLine=lines[2].split(":")
            org3 = Organisme(secLine[0],a,b,c)

    with open("config.txt",encoding="utf-8") as myFile:
        lines=myFile.read().split("\n")

        width,height=lines[0].split(",")
        width=int(width)
        height=int(height)
        grid = Grille(width, height)
        for i in range(1, len(lines)-1):
            l=lines[i].split(",")
            if l[0]=="R":
                org1.set(grid.grid,int(l[1]),int(l[2]))
            elif l[0]=="G":
                org2.set(grid.grid, int(l[1]), int(l[2]))
            elif l[0]=="B":
                org3.set(grid.grid, int(l[1]), int(l[2]))
            else:

                org4.set(grid.grid,int(l[1]),int(l[2]))

    return grid,org1,org2,org3

def animate(grid,org1,org2,org3):
    value=""
    while value=="":
        for i in range(29):
            print()
        grid.cycle(org1, org1, org3)
        print("appuyer enter pour un nouvelle animation")
        print("appuyer une autre touche pour quitter")
        value=input()

def main():

    grid,org1,org2,org3=openFile()
    grid.printgrid()
    number_of_cycle = input("entrer le nombre d'iteration ou taper Animation  ")
    if number_of_cycle[0]=="A" or number_of_cycle[0]=="a":
        animate(grid, org1,org2,org3)
    else:
        for i in range(int(number_of_cycle)):
            grid.cycle(org1, org1, org3)



main()