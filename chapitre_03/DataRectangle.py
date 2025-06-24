from dataclasses import dataclass

@dataclass
class DataRectangle:
    longueur:int=1
    largeur:int=1

    @property
    def surface(self):
        return self.longueur*self.largeur
  
