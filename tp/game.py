from ticTacToe import tic_tac_toe


class theGame:
    #le constructeur prend un seul parametre qui correspond a la configuration d'entier(decimale)
    def __init__(self,configuration=""):

        self._jeu=[[""] * 3  for i in range(3)]
        self._con = bin(int(configuration))[2:]
        self._dernierCoup = self._con[0:7]
        self._jeu= self.initialiser(self._jeu, self._con,int(self._dernierCoup,2))


    # cette methode initialise le la grille du UTTT
    def initialiser(self,jeu, config,dernierCoup):
        c = config[7:]
        low_index=0
        high_index=18
        debut=0
        fin=8
        t = tic_tac_toe(debut, fin, c[low_index:high_index],dernierCoup)
        for i in range(3):
            for j in range(3):

                jeu[i][j]=t
                debut=fin+1
                fin+=9
                low_index=high_index
                high_index+=18
                t=tic_tac_toe(debut,fin,c[low_index:high_index],dernierCoup)

        return jeu






    #la methode display permet d'afficher le jeu au complet
    def display(self):
        self.printLine(0)
        print("-------------------------------")
        self.printLine(1)
        print("-------------------------------")
        self.printLine(2)
        print("-------------------------------")



    #la methode printLine permet d'afficher une ligne du jeu
    def printLine(self,k):

        for i in range(3):
            self.afficher(k,0,i)
            self.afficher(k,1,i)
            self.afficher(k,2,i)
            print()

    #la methode afficher permet d'afficher les composante x o . de la grille
    def afficher(self, row,col,num):

        print(self._jeu[row][col]._grid[num][0]._signe, end="  ")
        print(self._jeu[row][col]._grid[num][1]._signe, end="  ")
        print(self._jeu[row][col]._grid[num][2]._signe, end="  ")
        if col!=2:
            print("|", end="")











def main():
    t=theGame("459329034283597291728327479273734123420780266358036")
    t.display()





main()


