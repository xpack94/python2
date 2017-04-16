from node import Node
class HashMap:
    def __init__(self,capacity=50000):
        n=Node(None,None)
        self._hashTable=2*capacity*[n]
        self._size=0



    def hashFunction(self,k):

        hashCode=0
        length=len(k)
        pow=length-1
        for i in k:
            hashCode+= ord(i)*2**pow
            pow-=1


        return hashCode % len(self._hashTable)


    #methode qui retourne tous le elements a une position donnée
    def get(self,k):
         t=""
         t+="["+str(self._hashTable[k]._element)+"]"
         c=self._hashTable[k]
         while(c._next !=None):
            c=c._next
            t+="["+str(c._element)+"]"

         return t


    #mehode qui permet de faire un set a une position donnée
    def set(self,k,value):
        w=Node(value,None)
        if self._hashTable[k]._element==None:
            self._hashTable[k]=w
        else:
            n=Node(value,self._hashTable[k].getNext())
            self._hashTable[k].setNext(n)




    def delete(self,k):
        n=Node(None,None)
        self._hashTable[k]=n




    #la methode qui permet de lire tous les mots dans le dictionaire dict
    #et les mettre dans la table de hachage
    def readDictionary(self):
            f1 = open("dict.txt")
            while True:
                line = f1.readline()
                line=line[0:-1]
                index=self.hashFunction(line)
                self.set(index,line)
                if ("" == line):
                    break;




    #la methode qui permet de lire le mot qui se trouve dans le fichier input
    def readInput(self):
        input=open("input.txt")
        word=input.readline()[0:-1]
        swapedWord=word
        return self.swap(word)



    #la methode qui permet d'Intervertir chaque paire de caractères adjacents du mot
    #et verifie a chaque fois si le mot generer existe dans le dictionaire
    def swap(self,word):
        swapedWord = word
        t=""
        for i in range(len(word)):
            lowerSubWord = word[:i]
            higherSubWord = word[i + 2:]
            swapedWord = "".join([word[i:i + 2][::-1]])
            swapedWord = lowerSubWord + swapedWord + higherSubWord
            if self.find(swapedWord) != "":
               t+= " "+self.find(swapedWord)

        return t

    #la methode qui permet d'inserer chaque lettre de l'alphabet dans chaque paire de caractaires adjacents
    def insert(self,word):
        alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"
                  ,"v","w","x","y","z"]

        wordsFound=[]

        for i in range(len(word)+1):
            lowerLetter=word[:i]
            higherLetter=word[i:]
            for j in range(len(alphabet)):
                newWord=lowerLetter+str(alphabet[j])+higherLetter
                ifFoundMatch=self.find(newWord)
                if ifFoundMatch!="":
                    wordsFound.append(ifFoundMatch)


        return ifFoundMatch



    #la methode qui permet de supprimer chaque caractaire du mot
    def deleteEveryord(self,word):
        matches_found=[]
        for i in range(len(word)):

            lowerLetter=word[:i]
            letter_to_delete=word[i+1:]
            new_word=lowerLetter+letter_to_delete

            iffoudMatch=self.find(new_word)
            if iffoudMatch!="":
                print(iffoudMatch)
                matches_found.append(iffoudMatch)


    # la methode qui permet de remplacer chaque caractaire par chaque lettre de l'alphabet
    def replaceEveryLetter(self,word):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                    "u"
            , "v", "w", "x", "y", "z"]

        matches_found=[]
        for i in range(len(word)):
            lowerWord=word[:i]
            higherWord=word[i+1:]
            for j in range(len(alphabet)):
                new_word=lowerWord+alphabet[j]+higherWord
                ifFoundMatch=self.find(new_word)
                if ifFoundMatch!="":
                    matches_found.append(ifFoundMatch)


    #la methode qui permet de chercher un mot dans la table et le retourne si il exist
    def find(self,word):
        code=self.hashFunction(word)
        c=self._hashTable[code]

        if c._element==word:
            return word
        else:
            while c._next!=None:
                c=c._next
                if c._element==word:
                    return word

        return ""



    def printTable(self):
        for i in range(len(self._hashTable)):
            print(self.get(i))


def main():

    h=HashMap(50000)
    h.readDictionary()
    #h.printTable()
    #print(h.readInput())

    h.replaceEveryLetter("binjour")





main()


