from abc import ABC,ABCMeta,abstractmethod

class ICalcGeo(metaclass=ABCMeta):

    @property
    @abstractmethod
    def surface(self)->float:
        pass
    
    # def surface(self)->float:...
        