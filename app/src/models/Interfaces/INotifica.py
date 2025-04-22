from abc import ABC, abstractmethod
from src.models.Interfaces import IUser, IPrestito

class INotifica(ABC):
    @abstractmethod
    def get_utente(self) -> IUser:
        """Restituisce l'utente associato alla notifica."""
        pass

    @abstractmethod
    def get_prestito(self) -> IPrestito:
        """Restituisce il prestito associato alla notifica."""
        pass

    @abstractmethod
    def get_messaggio(self) -> str:
        """Restituisce il messaggio della notifica."""
        pass