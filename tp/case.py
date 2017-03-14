

class Case:
    def __init__(self,number=0,etat="00",nom="",dernierCoup=0):
        self._number=number
        self._etat=etat
        self._nom=nom
        self._signe=self.decoder(self._etat,dernierCoup)



    def decoder(self,etat,dernierCoup):
        if etat=="00":
            return "."
        elif (etat=="01") :
            if self._number==dernierCoup:
                return "X"
            else:
                return "x"
        elif etat=="10":
            if self._number==dernierCoup:
                return "O"
            else:
                return "o"

