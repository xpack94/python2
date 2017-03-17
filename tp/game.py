from case import Case
from ticTacToe import tic_tac_toe
import random

class theGame:
    #le constructeur prend un seul parametre qui correspond a la configuration d'entier(decimale)
    def __init__(self,configuration=""):

        self._jeu=[[""] * 3  for i in range(3)]
        self._con = bin(int(configuration))[2:]
        self._dernierCoup = self._con[0:7]
        self._jeu= self.initialiser(self._jeu, self._con,int(self._dernierCoup,2))


    # cette methode initialise le la grille du UTTT
    #t= top et correspond a la 1er ligne de la grille du jeu
    #m=middle et correpond a la 2eme ligne de la grille du jeu
    #b=bottom et correspond a la 3eme ligne de la grille du jeu
    def initialiser(self,jeu, config,dernierCoup):
        c = config[7:]
        low_index=0
        high_index=18
        debut=0
        fin=8

        for i in range(3):
            for j in range(3):
                if i==0:
                    nom="t"+str(j+1)
                elif i==1:
                    nom="m"+str(j+1)
                else:
                    nom="b"+str(j+1)

                t = tic_tac_toe(debut, fin, c[low_index:high_index], dernierCoup,nom)
                jeu[i][j]=t
                debut=fin+1
                fin+=9
                low_index=high_index
                high_index+=18




        return jeu




    def jouerCoup(self,jeu,configuration,dernierCoup):
        dCoup=int(dernierCoup,2)
        #le caractere qui represente le dernier coup joué est placé dans la variable tour
        case_a_jouer,tour=self.chercher_nom_de_la_cas_du_dernierCoup(dCoup,jeu)
        if case_a_jouer!="":
            for i in range(3):
                for j in range(3):
                    if jeu[i][j]._nom==case_a_jouer:


                        #la variable coup est affectée le numero du coup a jouer
                        #la methode meilleur_coup est appelé pour retourner le numero du meilleur coup
                        coup=jeu[i][j].meilleur_coup(jeu[i][j],tour,1)

                        #tester si le tic_tac_toe ou on vas jouer n'est pas completé ou gagné deja par un des joueurs
                        if jeu[i][j].victoire(jeu[i][j])=="11":
                            self.jouer(jeu[i][j],coup,jeu[i][j].changer_tour(tour),case_a_jouer)
                        #sinon le joueur pourra jouer n'importe ou dans le jeu principal
                        else:
                            break





    #methode qui traverse la grille du jeu principale et renvoi le nom de la case du dernier coup joué

    def chercher_nom_de_la_cas_du_dernierCoup(self,dernierCoup,jeu):
        for i in range(3):
            for j in range(3):
                if jeu[i][j]._dIntervale<= dernierCoup <=jeu[i][j]._fIntervale :
                    return self.trouver_nom_de_la_case(jeu[i][j]._grid,dernierCoup)


        return "" ,"00"



    #mthode qui traverse une grille de tic_tac_toe ou le dernier coup a etait joué et renvoi son nom
    #elle permet de trouver ou le prochain coup sera jouer
    def trouver_nom_de_la_case(self,grid,dernierCoup):
        for i in range(3):
            for j in range(3):
                if grid[i][j]._number ==dernierCoup:
                    #retourner le nom de la case du dernier coup et retourner l'etat du dernier coup
                    #pour savoir a quel tour c'est
                    grid[i][j]=Case(grid[i][j]._number,grid[i][j]._etat,grid[i][j]._nom,"")
                    return grid[i][j]._nom , grid[i][j]._etat



        return ""


    #methode qui cherche tout les coups possible a jouer et les mets dans un tableau
    # def trouver_coups_possibles(self,jeu):
    #     coups_possible=[]
    #     for i in range(3):
    #         for j in range(3):
    #             if jeu[i][j]._etat=="00":
    #                 coups_possible.append(jeu[i][j]._number)



        return coups_possible


    def jouer(self,jeu,coup,tour,nom):

        for i in range(3):
            for j in range(3):
                if jeu._grid[i][j]._number == coup:
                     c=Case(coup,tour,nom,coup)
                     jeu._grid[i][j]=c
                     jeu._grid[i][j]._number






    #la methode display permet d'afficher la grille du  jeu au complet
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
    #t.display()
    t.jouerCoup(t._jeu,"459329034283597291728327479273734123420780266358036",t._dernierCoup)
    t.display()








main()


