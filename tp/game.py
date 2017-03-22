from case import Case
from ticTacToe import tic_tac_toe
import random

class theGame:
    #le constructeur prend un seul parametre qui correspond a la configuration d'entier(decimale)
    def __init__(self,configuration=""):

        self._jeu=[[""] * 3  for i in range(3)]
        self._con=str(bin(int(configuration))[2:])
        self._dernierCoup,self._jeu= self.initialiser(self._jeu, self._con)
        self._tab=[]
        self._tabCinfig=[]



    # cette methode initialise le la grille du UTTT
    #t= top et correspond a la 1er ligne de la grille du jeu
    #m=middle et correpond a la 2eme ligne de la grille du jeu
    #b=bottom et correspond a la 3eme ligne de la grille du jeu
    def initialiser(self,jeu, config):

        if len(config)<169:

            config=self.ajouter_des_zeros(config)


        dernierCoup=config[0:7]
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

                t = tic_tac_toe(debut, fin, c[low_index:high_index], int(dernierCoup,2),nom,j+3*i)
                jeu[i][j]=t
                debut=fin+1
                fin+=9
                low_index=high_index
                high_index+=18



        return dernierCoup,jeu

    #cette methode ajoute des zeros a la configuration pour faire 196 bits
    def ajouter_des_zeros(self,config):

        for i in range(len(config),169):
            config="0"+str(config)


        return config

    def jouerCoup(self,jeu,configuration,dernierCoup,param):
        dernier=""
        dCoup=int(dernierCoup,2)
        #le caractere qui represente le dernier coup joué est placé dans la variable tour
        case_a_jouer,tour=self.chercher_nom_de_la_cas_du_dernierCoup(dCoup,jeu)
        if case_a_jouer!="":
            for i in range(3):
                for j in range(3):
                    if jeu[i][j]._nom==case_a_jouer:


                        #la variable coup est affectée le numero du coup a jouer
                        #la methode meilleur_coup est appelé pour retourner le numero du meilleur coup

                        if param!="a":
                            coup=jeu[i][j].meilleur_coup(jeu[i][j],tour,1)

                        #tester si le tic_tac_toe ou on vas jouer n'est pas completé ou gagné deja par un des joueurs
                        if jeu[i][j].victoire(jeu[i][j])=="11":
                            if param=="a":
                                self.trouver_tout_les_coups_dans_un_tictactoe(jeu[i][j],jeu[i][j].changer_tour(tour))
                                return tour
                            else:
                                dernier=self.jouer(jeu[i][j],coup,jeu[i][j].changer_tour(tour),case_a_jouer)
                        #sinon le joueur pourra jouer n'importe ou dans le jeu principal
                        else:
                            if param=="a":
                               self.trouver_tous_les_coups_dans_leJeu_principale(jeu,jeu[i][j].changer_tour(tour))
                            else:
                                dernier=self.jouer_nimporte_ou(case_a_jouer,jeu[i][j].changer_tour(tour))



        return dernier


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





        return coups_possible


    def jouer(self,jeu,coup,tour,nom):

        for i in range(3):
            for j in range(3):
                if jeu._grid[i][j]._number == coup:
                     c=Case(coup,tour,nom,coup)
                     jeu._grid[i][j]=c
                     return jeu._grid[i][j]._number





    def jouer_nimporte_ou(self,case,tour):

        valMax =-2
        pos =None
        nom=""
        jeu=None
        for i in range(3):
            for j in range(3):
                if self._jeu[i][j]._nom!=case:
                    #verifier  qu'on peut jouer dans ce tictactoe
                    if self._jeu[i][j].victoire(self._jeu[i][j])=="11":
                        meilleur=self._jeu[i][j].meilleur_coup(self._jeu[i][j],tour,1)
                        dernier=self.jouer(self._jeu[i][j],meilleur,tour,self._jeu[i][j]._nom)
                        #on joue le coup et verifier s'il le joueur gagne
                        if self._jeu[i][j].victoire(self._jeu[i][j])==tour:
                            #si le coup joueé permet de gagner dans ce tic tac toe
                            val = +1
                        elif self._jeu[i][j].victoire(self._jeu[i][j])=="00":
                            #si le coup joué permet de faire un match null dans ce tic tac toe
                            val=0
                        else:
                            #si le coup joué ne fait rien
                            val=-1
                        #appeler la methode affecter pour déjouer le coup qu'on vient de jouer

                        self.dejouer(self._jeu[i][j], meilleur, "00")

                        if val>valMax:
                            valMax=val
                            pos=meilleur
                            nom=self._jeu[i][j]._nom
                            jeu=self._jeu[i][j]


        return self.jouer(jeu,pos,tour,nom)



    def dejouer(self,grid,pos,etat):
        for i in range(3):
            for j in range(3):
                if grid._grid[i][j]._number==pos:
                    c=Case(grid._grid[i][j]._number,etat,grid._grid[i][j]._nom,"")
                    grid._grid[i][j]=c




    def coder(self,configuration,dernier):

        codage=""

        #dernier =bin(self.jouerCoup(self._jeu,configuration,self._dernierCoup,param))[2:]

        for i in range(3):
            for j in range(3):
                codage=self._jeu[i][j].encoder(self._jeu[i][j],codage)


        return int(str(dernier)+str(codage),2)



    #la methode qui permet de trouver tous les coups possible dans la grille principale
    #cette methode est appelée quand le joueur est envoyé jouer dans une case qui est deja gagné
    #donc ce dernier peut jouer dans n'importe quelle case
    def trouver_tous_les_coups_dans_leJeu_principale(self,jeu,tour):
        for i in range(3):
            for j in range(3):
                if jeu[i][j].victoire(jeu[i][j])=="11":
                    self.trouver_tout_les_coups_dans_un_tictactoe(jeu[i][j],tour)

    #methode qui permet de trouevr tous les coups possible dan un seul jeu de tic tac toe
    #met tous les coups possible dans le tableau self._tab
    def trouver_tout_les_coups_dans_un_tictactoe(self,jeu,tour):

        for i in range(3):
            for j in range(3):
                if jeu._grid[i][j]._etat=="00":
                  self._tab.append(jeu._grid[i][j]._number)
                  self._tab.append(jeu._grid[i][j]._nom)






    #metode qui retourne le tic_tac_toe qui contient la case donnée en parametres
    def chercher_jeu(self,jeu,numero):

        for i in range(3):
            for j in range(3):
                if jeu[i][j]._dIntervale <= int(numero) <=jeu[i][j]._fIntervale:

                    return jeu[i][j]

        return ""

    #la methode qui permet d'afficher l'arbre avec une profondeur donnée
    def affichage_arbre(self,t,configuration,param,profondeur):

        co=0
        count=0
        dernier = t.jouerCoup(t._jeu, configuration, t._dernierCoup, param)
        t.codage_arbre(configuration, t._jeu, dernier)
        counter=int(len(self._tab)/2)

        for i in range(1,profondeur):

            for j in range(co,counter):
                        t._tab = []
                        f=theGame(t._tabCinfig[j])
                        dernier = f.jouerCoup(f._jeu, t._tabCinfig[j] ,f._dernierCoup, param)
                        count+=int(len(f._tab)/2)

                        f.codage_arbre(t._tabCinfig[j], f._jeu, dernier)
                        self.merge(t, f)


            co=counter
            counter+=count

        t._tab=[]
        self.print_arbre(t,configuration)





    def merge(self,t,f):
        for i in f._tabCinfig:
            t._tabCinfig.append(i)


    def codage_arbre(self,configuration,jeu,tour):

        c_tour= self.change_joueur(tour)

        for i in range(0,len(self._tab),2):
            tic=self.chercher_jeu(jeu,self._tab[i])
            dernier= bin(self.jouer(tic, self._tab[i], c_tour,self._tab[i+1]))[2:]
            self._tabCinfig.append(self.coder(configuration,dernier))
            self.dejouer(tic,self._tab[i],"00")







    def print_arbre(self,game,configuration):
        print(configuration,end="  ")
        for i in range(len(game._tabCinfig)):
            print(game._tabCinfig[i],end="  ")
        print()
        print(len(game._tabCinfig))
        game._tabCinfig=[]


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



    def change_joueur(self,tour):
        if tour == "01":
            return "10"
        else:
            return "01"

    # cette methode renvoi le joueur qui a gagné
    #si c'est x ça retourne 01 , si s'est o ça retourn 10 , si match nul ça retourne 00
    # si partie inachevé ça retourne 11
    def victoire(self, grille):

        alignments= grille[0][0].trouver_alignement(grille[0][0])

        for i in alignments:
            pas=i["pas"]
            departs=i["depart"]
            for j in range(len(departs)):

                pos=departs[j]
                if self.sym(grille,pos)!="11" or self.sym(grille,pos)!="00":
                    for k in range(3):
                        if self.sym(grille,pos)!=self.sym(grille,pos+k*pas):
                            break
                        if k==2:
                            return self.sym(grille,pos)


        if self.occupee(grille)==9:
            return "00"


        return "11"

    #la methode sym permet de retourner le joueur qui a gagné dans un tic tac toe donné
    def sym(self,grille,pos):
        for i in range(3):
            for j in range(3):
                if grille[i][j]._numberofTicTacToe==pos:
                    return grille[i][j].victoire(grille[i][j])


    #compte si toute les case on etait gagnée par un joueur soit x ou o
    def occupee(self,grille):
        co=0
        for i in range(3):
            for j in range(3):
                if  grille[i][j].victoire(grille[i][j])!="11":
                    co+=1


        return co



def main():
    t=theGame("459329034283597291728327479273734123420780266358036")
    t.display()

    #t.display()
    #t.jouerCoup(t._jeu,"441791014635626456709883261281138727184909075842324",t._dernierCoup)
    # if parametre ==""
    # dernier=t.jouerCoup(t._jeu,"459329034283597291728327479273734123420780266358036",t._dernierCoup,"")
    # print(t.coder("459329034283597291728327479273734123420780266358036",bin(dernier)[2:]))





    #if parametre =="a"
    t.affichage_arbre(t,"459329034283597291728327479273734123420780266358036","a",3)
    #dernier = t.jouerCoup(t._jeu, "459329034283597291728327479273734123420780266358036", t._dernierCoup, "a")
    # t.codage_arbre("459329034283597291728327479273734123420780266358036",t._jeu ,dernier)

    #print(t.coder("459329034283597291728327479273734123420780266358036","a"))


    j=theGame("412560981889008398670328118285239794137896400028948")

    j.display()














main()


