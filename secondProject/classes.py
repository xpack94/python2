import random
# class Square:
#     def __init__(self, height="0", width="0"):
#         self.height = height
#         self.width = width
#
#     # This is the getter
#     @property
#     def height(self):
#         print("Retrieving the height")
#
#         # Put a __ before this private field
#         return self.__height
#
#     # This is the setter
#     @height.setter
#     def height(self, value):
#
#         # We protect the height from receiving a bad value
#         if value.isdigit():
#
#             # Put a __ before this private field
#             self.__height = value
#         else:
#             print("Please only enter numbers for height")
#
#     # This is the getter
#     @property
#     def width(self):
#         print("Retrieving the width")
#         return self.__width
#
#     # This is the setter
#     @width.setter
#     def width(self, value):
#         if value.isdigit():
#             self.__width = value
#         else:
#             print("Please only enter numbers for width")
#
#     def getArea(self):
#         return int(self.__width) * int(self.__height)
#
#
# def main():
#     aSquare = Square()
#
#     height = input("Enter height : ")
#     width = input("Enter width : ")
#
#     aSquare.height = height
#     aSquare.width = width
#
#     print("Height :", aSquare.height)
#     print("Width :", aSquare.width)
#
#     print("The Area is :", aSquare.getArea())
#
#
# main()




class Warrior:

    def __init__(self,lifePoint="0", name=""):

        self.lifePoint=lifePoint
        self.name = name


    def name(self):
        return self.__name



    def name(self,value):
        self.__name=value



    def lifePoint(self):
        return self.__lifePoint


    def lifePoint(self,value):
        if value.isdigit():
            self.__lifePoint=value
        else:
            print("life points can only be integers")



    def attack(self,warrior2):
        damage=random.randrange(20)
        warrior2.lifePoint=str(int(warrior2.lifePoint)-damage)
        print("warrior {} has taken {} damage".format(warrior2.name, damage))


    def fight(self,warrior):
        turn = self
        nextTurn = warrior
        while (int(self.lifePoint)>0) and  (int(warrior.lifePoint)>0):
            turn.attack(nextTurn)
            print(" {} has {} life points".format(nextTurn.name,nextTurn.lifePoint))

            if turn==self:
                turn= warrior
                nextTurn= self
            else:
                turn=self
                nextTurn=warrior



        if int(self.lifePoint)<=0:
            print("the winner is ",warrior.name)
        else:
            print("the winner is ",self.name)




def main():
    war1=Warrior()
    war2=Warrior()
    name1=input("enter the warrior1's name")
    lp1=input("enter the life points ")
    name2=input("enter the warrior2's name")
    lp2=input("enter the life points")
    war1.lifePoint=lp1
    war1.name=name1
    war2.lifePoint=lp2
    war2.name=name2

    war1.fight(war2)


main()



