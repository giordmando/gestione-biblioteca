# Interfacce
from abc import abstractmethod

from src.models.Interfaces.IItemPrestabile import IItemPrestabile


class IElement(IItemPrestabile):
    @abstractmethod
    def get_id(self):
        pass
    
    @abstractmethod
    def get_titolo(self):
        pass