

class Case:
    def __init__(self,number=0,etat="00"):
        self._number=number
        self._etat=etat
        self._signe=self.decoder(self._etat)



    def decoder(self,etat):
        if etat=="00":
            return "."
        elif etat=="01":
            return "x"
        else:
            return "o"

