from abc import ABC, abstractmethod

from src.models.Interfaces import IElement, IPrestito, IUser

class IPrestitoService(ABC):
    @abstractmethod
    def add_prestito(self, prestito:IPrestito):
        pass

    @abstractmethod
    def add_new_prestito(self, elemento:IElement, user:IUser, data_inizio:str, data_fine:str):
        pass
    
    @abstractmethod
    def rimuovi_prestito(self, id:int):
        pass
    
    @abstractmethod
    def ricerca_prestito(self, id:int):
        pass

    @abstractmethod
    def tutti_prestiti_utente(self, user_id:int):
        pass

    @abstractmethod
    def tutti_prestiti(self):
        pass