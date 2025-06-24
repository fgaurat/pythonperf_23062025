from abc import ABC,abstractmethod

class ICalcGeo(ABC):

    @property
    @abstractmethod
    def surface(self):
        pass