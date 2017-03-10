from case import Case


class tic_tac_toe:
    def __init__(self,number=0,etat=""):
        c=Case(number,"00")
        self._grid=[[c] * 3 for i in range(3)]
        self._grid= self.initialiser(self._grid,number,etat)
        self.afficher(self._grid)


    #class has method victory
    #method turn
    #method afficher

    def initialiser(self,grid,number,etat):
        #appeler la method decoder pour le decodage des etats
        #etat=18bits
        index_low=0
        index_high=2

        c= Case(number,etat[index_low:index_high])
        for i in range(3):
            for j in range(3):
               grid[i][j]=c
               index_low=index_high
               index_high+=2
               c=Case(c._number+1,etat[index_low:index_high])



        return grid










    def afficher(self,grid):
        for i in range(3):
            for j in range(3):
                print(grid[i][j]._signe ,end="")
                print(" ",end="")
            print()




def main():

    t=tic_tac_toe(0,"010000111000000000")

main()
