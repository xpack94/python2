from case import Case


class tic_tac_toe:
    #dIntervale = debut d'intervale , fInterval = fin d'intervale
    #car chaque tic_tac_toe a son propre intervale de nombre
    #exemple le 1er entre [0-8] 2 eme entre [9-17] etc...

    def __init__(self,dIntervale=0,fIntervale=0,etat="",dernierCoup=0,nom=""):
        c=Case(dIntervale,"00")
        self._grid=[[c] * 3 for i in range(3)]
        self._nom=nom
        self._grid= self.initialiser(self._grid,dIntervale,etat,dernierCoup)
        self._dIntervale=dIntervale
        self._fIntervale=fIntervale



    #class has method victory
    #method turn
    #method afficher

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





def main():

    t=tic_tac_toe(0,8,"100100100100100010")



