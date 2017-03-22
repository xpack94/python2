from case import Case


class tic_tac_toe:
    #dIntervale = debut d'intervale , fInterval = fin d'intervale
    #car chaque tic_tac_toe a son propre intervale de nombre
    #exemple le 1er entre [0-8] 2 eme entre [9-17] etc...

    def __init__(self,dIntervale=0,fIntervale=0,etat="",dernierCoup=0,nom="",number=0):
        c=Case(dIntervale,"00")
        self._grid=[[c] * 3 for i in range(3)]
        self._nom=nom
        self._grid= self.initialiser(self._grid,dIntervale,etat,dernierCoup)
        self._dIntervale=dIntervale
        self._fIntervale=fIntervale
        self._numberofTicTacToe=number
        self._val=[]




    def initialiser(self,grid,number,etat,dernierCoup):

        #etat=18bits
        index_low=0
        index_high=2


        for i in range(3):
            for j in range(3):
                if i==0:
                    nom="t"+str(j+1)
                elif i==1:
                    nom="m"+str(j+1)
                else:
                     nom="b"+str(j+1)


                c = Case(number, etat[index_low:index_high],nom,dernierCoup)
                grid[i][j]=c
                index_low=index_high
                index_high+=2
                number=c._number+1




        return grid
    #cette methode retourne une configuration possible selon le nombre du jeu tic_tac_toe
    #cette configuration represente les cas possible de victoire
    def trouver_alignement(self,grid):
        alignments=[]
        if grid._dIntervale ==0:
            alignments=[{"pas":+1 , "depart":[0,3,6]},{"pas":+3,"depart":[0,1,2]},{"pas":+4,"depart":[0]},{"pas":-2,"depart":[6]}]
        elif grid._dIntervale==9:
            alignments = [{"pas": +1, "depart": [9, 12, 15]}, {"pas": +3, "depart": [9, 10, 11]},
                          {"pas": +4, "depart": [9]}, {"pas": -2, "depart": [15]}]
        elif grid._dIntervale==18:
            alignments = [{"pas": +1, "depart": [18, 21, 24]}, {"pas": +3, "depart": [18, 19, 20]},
                          {"pas": +4, "depart": [18]}, {"pas": -2, "depart": [24]}]
        elif grid._dIntervale == 27:
            alignments = [{"pas": +1, "depart": [27, 30, 33]}, {"pas": +3, "depart": [27, 28, 29]},
                          {"pas": +4, "depart": [27]}, {"pas": -2, "depart": [33]}]
        elif grid._dIntervale==36:
            alignments = [{"pas": +1, "depart": [36, 39, 42]}, {"pas": +3, "depart": [36, 37, 38]},
                          {"pas": +4, "depart": [36]}, {"pas": -2, "depart": [42]}]
        elif grid._dIntervale==45:
            alignments = [{"pas": +1, "depart": [45, 48, 51]}, {"pas": +3, "depart": [45, 46, 47]},
                          {"pas": +4, "depart": [45]}, {"pas": -2, "depart": [51]}]

        elif grid._dIntervale==54:
            alignments = [{"pas": +1, "depart": [54, 57, 60]}, {"pas": +3, "depart": [54, 55, 56]},
                          {"pas": +4, "depart": [54]}, {"pas": -2, "depart": [60]}]
        elif grid._dIntervale==63:
            alignments = [{"pas": +1, "depart": [63, 66, 69]}, {"pas": +3, "depart": [63, 64, 65]},
                          {"pas": +4, "depart": [63]}, {"pas": -2, "depart": [69]}]
        elif grid._dIntervale==72:
            alignments = [{"pas": +1, "depart": [72, 75, 78]}, {"pas": +3, "depart": [72, 73, 74]},
                          {"pas": +4, "depart": [72]}, {"pas": -2, "depart": [78]}]

        return alignments




    #la methode victoire retourne l'etat de la personne qui a gagné
    #retourn 01 si x a gagné , 10 si O , 00 si il ya partie nulle
    def victoire(self,t):

        alignments= self.trouver_alignement(t)


        for i in alignments:
            pas=i["pas"]
            departs=i["depart"]
            for j in range(len(departs)):
                pos=departs[j]
                if self.sym(t._grid,pos)!="00":
                    for k in range(3):
                        if self.sym(t._grid,pos)!=self.sym(t._grid,pos+k*pas):
                            break
                        if k==2:
                            return self.sym(t._grid,pos)

        if self.occupees(t._grid) == 9:
            return "00"

        return "11"


    #methode sym retourne l'etat d'une position donnée
    def sym(self,grid,position):
        for i in range(3):
            for j in range(3):
                if grid[i][j]._number==position:
                    return grid[i][j]._etat

        return ""

    def print(self):
        for i in range(3):
            for j in range(3):
                print(self._grid[i][j]._signe, end=" ")

            print()

    #recoit une jeu tic_tac_toe en argument
    # retourne la position de la case qui
    #est le meilleur coup pour le joueur à qui c’est le tour
    def meilleur_coup(self,t,tour,n):


        valMax=-2
        posMax=None
        for i in range(3):
            for j in range(3):
              if t._grid[i][j]._etat=="00":

                val=self.valeur_coup(t,t._grid[i][j]._number,tour)

                if val>=valMax:
                    valMax=val
                    posMax=t._grid[i][j]._number

                    if n == 1:
                      self._val.append(val)
                    if val==1:
                        self.affecter(t, t._grid[i][j]._number, tour)
                        if self.victoire(t)==tour:

                            self.affecter(t, t._grid[i][j]._number, "00")
                            return posMax
                        self.affecter(t, t._grid[i][j]._number, "00")



        if n==1:
            if self.check_tab(t):

                if tour=="01":
                    c_t="10"
                else:
                    c_t="01"

                return self.block(t,c_t)


        return posMax

    #la methode permet de changer le tour du joueur
    def changer_tour(self,joueur):
        if joueur=="00":
            tour="01"
        elif joueur=="01" :
            tour="10"
        else:
            tour="01"

        return tour
    #prend une position en parametre et affect curerent_tour a cette position
    def affecter(self,t,pos,current_tour):


        for i in range(3):
            for j in range(3):
                if t._grid[i][j]._number == pos:
                     t._grid[i][j]._etat = current_tour
                     break


    # retourne la valeur de la configuration obtenue en jouant à la case pos
    def valeur_coup(self,t,pos,tour):


        self.affecter(t,pos,tour)

        if self.victoire(t) == "01" or self.victoire(t) == "10":
            val = +1
        elif self.occupees(t._grid) == 9:
            val = 0
        else:
            c_tour=self.changer_tour(tour)
            val=-self.valeur_coup(t,self.meilleur_coup(t,c_tour,0),c_tour)
            c_tour = self.changer_tour(tour)

        self.affecter(t,pos,"00")



        return val


    #cette methode compte le nombre  cases  occupees
    def occupees(self,grid):
        co=0
        for i in range(3):
            for j in range(3):
                if grid[i][j]._etat!="00":
                    co+=1



        return co

    #cette methode ce fait pour verifier si toute les valeurs de self._val sont egales a -1
    def check_tab(self,t):
        co=0
        for i in t._val:
            if i==-1:
                co+=1

        if co==len(t._val):
            return True

        return False
    #la methode block est appelé lorsque tous les coups possible ne permettent ni de gangné ni de faire une partie nulle
    #donc elle retourne le meilleur coup en se basant de la configuration actuel
    def block(self,t,state):
        alignments = self.trouver_alignement(t)
        val=0

        for i in alignments:
            pas = i["pas"]
            departs = i["depart"]
            for j in range(len(departs)):
                pos = departs[j]

                for k in range(3):
                    if self.sym(t._grid,pos)==state:
                        if self.sym(t._grid, pos) != self.sym(t._grid, pos + k * pas):
                            if k!=1:
                                if val==1:
                                    return pos-pas
                            if k==2:
                                return pos+k*pas

                            else:
                                break

                    elif self.sym(t._grid,pos)=="00":
                        val+=1
                        pos=pos+pas
                    else:
                        break
                    if val>1:
                        break

                val=0


        return -1



    def encoder(self,t,codage):

        for i in range(3):
            for j in range(3):
                codage+=t._grid[i][j]._etat



        return  codage










def main():

    t=tic_tac_toe(0,8,"000000000000000001","","t1")
    t.print()

    print(t.meilleur_coup(t,"10",1))
    #print(t.block(t,"01"))














