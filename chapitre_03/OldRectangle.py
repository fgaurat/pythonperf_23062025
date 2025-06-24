



class OldRectangle:

    # constructeur
    def __init__(self,longueur, largeur): # self -> this
        assert longueur>0 and largeur>0
        self.__longueur = longueur
        self.__largeur = largeur
        
    def get_longueur(self):
        return self.__longueur

    def set_longueur(self,longueur):
        assert longueur>0
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self,largeur):
        assert largeur>0
        self.__largeur = largeur

    def get_surface(self):
        return self.__longueur*self.__largeur
    
    # destructeur
    def __del__(self):
        pass

    longueur = property(get_longueur,set_longueur,doc="Longueur property")
    largeur = property(get_largeur,set_largeur,doc="Largeur property")
    surface = property(get_surface,doc="Surface property")