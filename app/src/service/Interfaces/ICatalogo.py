from abc import ABC, abstractmethod


from src.models.Interfaces import IElement

class ICatalogo(ABC):
    @abstractmethod
    def aggiungi(self, elemento:IElement):
        pass

    @abstractmethod
    def rimuovi(self, elemento_id):
        pass
    
    @abstractmethod
    def trova_per_id(self, elemento_id):
        pass
    
    @abstractmethod
    def trova_tutti(self):
        pass