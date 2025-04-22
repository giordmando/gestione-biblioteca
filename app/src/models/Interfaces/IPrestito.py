from abc import ABC, abstractmethod

class IPrestito(ABC):
    @abstractmethod
    def presta(self):
        pass
    
    @abstractmethod
    def restituisci(self):
        pass
    
    @abstractmethod
    def is_disponibile(self):
        pass

    @abstractmethod
    def get_data_prestito(self):
        pass

    @abstractmethod
    def get_data_scadenza(self):
        pass

    @abstractmethod
    def get_info_utente(self):
        pass

    @abstractmethod
    def get_element(self):
        pass