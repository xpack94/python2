from case import Case


class tic_tac_toe:
    #dIntervale = debut d'intervale , fInterval = fin d'intervale
    #car chaque tic_tac_toe a son propre intervale de nombre
    #exemple le 1er entre [0-8] 2 eme entre [9-17] etc...

    def __init__(self,dIntervale=0,fInterval=0,etat="",dernierCoup=0):
        c=Case(dIntervale,"00")
        self._grid=[[c] * 3 for i in range(3)]
        self._grid= self.initialiser(self._grid,dIntervale,etat,dernierCoup)



    #class has method victory
    #method turn
    #method afficher

    def initialiser(self,grid,number,etat,dernierCoup):

        #etat=18bits
        index_low=0
        index_high=2

        c= Case(number,etat[index_low:index_high],dernierCoup)
        for i in range(3):
            for j in range(3):
               grid[i][j]=c
               index_low=index_high
               index_high+=2
               c=Case(c._number+1,etat[index_low:index_high],dernierCoup)



        return grid





    # def affiche(self):
    #     e=""
    #     for i in range(3):
    #         for j in range(3):
    #            e+= str(self._grid[i][j]._signe )
    #            e+=str(" ")
    #         e+=str("| ")
    #
    #
    #
    #     return e


def main():

    t=tic_tac_toe(0,8,"100100100100100010")
    print(t.affiche())

