


class Node:

    def __init__(self,element="",next=None):
        self._element=element
        self._next=next



    def getNext(self,):
        return self._next


    def setNext(self,next):
        self._next=next