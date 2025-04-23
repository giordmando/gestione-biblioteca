# Interfacce
from abc import ABC, abstractmethod

class IElement(ABC):
    @abstractmethod
    def get_id(self):
        pass
    
    @abstractmethod
    def get_titolo(self):
        pass