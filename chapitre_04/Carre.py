from Rectangle import Rectangle


class Carre(Rectangle):

    def __init__(self, cote=1):
        super().__init__(cote, cote)
        self.__cote = cote

    @property
    def cote(self):
        return self.__cote

    @cote.setter
    def cote(self,cote):
        self.__cote = cote
        self.longueur = cote
        self.largeur = cote

    def __str__(self):
        s = super().__str__()        
        return f"{__class__.__name__}({self.__cote}),{s}"