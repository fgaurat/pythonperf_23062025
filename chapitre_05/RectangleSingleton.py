



class RectangleSingleton:
    __slots__ = "__longueur","__largeur"
    __cpt = 0

    # initialisateur (constructeur)
    def __init__(self,longueur=1, largeur=1): # self -> this
        assert longueur>0 and largeur>0
        self.__longueur = longueur
        self.__largeur = largeur
        RectangleSingleton.__cpt+=1

    @classmethod
    def build_from_str(cls,value):
        longueur,largeur= [int(v) for v in value.split(';')] # ["12","4"]
        
        return cls(longueur,largeur)

    @property
    def longueur(self):
        return self.__longueur

    @longueur.setter
    def longueur(self,longueur):
        assert longueur>0
        self.__longueur = longueur
    
    @property
    def largeur(self):
        return self.__largeur
    
    @largeur.setter
    def largeur(self,largeur):
        assert largeur>0
        self.__largeur = largeur
    
    @property
    def surface(self):
        return self.__longueur*self.__largeur
    
    @staticmethod
    def get_cpt():
        return RectangleSingleton.__cpt

    # destructeur
    def __del__(self):
        pass

    def __str__(self)->str:
        return f"{__class__.__name__}({self.__longueur=},{self.__largeur=})"
    
    def __int__(self)->int:
        return self.surface

    def __eq__(self,o):
        return self.longueur == o.longueur and self.largeur == o.largeur

    def __hash__(self) -> int:
        return hash((self.longueur,self.largeur))