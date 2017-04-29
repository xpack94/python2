from SinglyLinkedNode import SinglyLinkedNode


class SinglyLinkedList:

    def __init__(self):
        self._first=None
        self._last=None
        self._size=0



    def __len__(self):
        return self._size


    def isEmpty(self):
        return self._size==0

    def append(self, element):
        newNode = SinglyLinkedNode(element, None)
        if self._last == None:
            self._first = self._last = newNode
        else:
            self._last.next = newNode
            self._last = newNode
        self._size += 1





    def remove(self,k):
        if  not 0<k<self._size:
            raise IndexError("inde out of bounds")
        else:
            node=self._first
            prev=None
            for i in range(1,k):
                prev=node
                node=node.next
            if prev==None:
                self._first=self._first.next
            else:
                prev.next=node.next
                self._size-=1

            if self._size==0:
                self._last=None
            if node.next==None:
                self._last=prev



        return node.element



    def find(self,el):

        if self.isEmpty():
            return None
        else:
            node = self._first
            for i in range(self._size):
                if node.element==el:
                    return i
                else:
                    node=node.next
            return None


    def printList(self):

            if self.isEmpty():
                print()
            else:
                node=self._first
                for i in range(self._size):
                    if node.next != None:
                        print(node.element,"---->",end="")
                        node=node.next
                    else:
                        print(node.element)



def main():
    list=SinglyLinkedList()
    for i in range(5):
       list.append(int(input("enter a number")))

    list.printList()




