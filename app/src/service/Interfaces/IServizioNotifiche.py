from abc import ABC, abstractmethod
from src.models.Interfaces import IElement, IPrestito, IUser


class IServizioNotifiche(ABC):
    @abstractmethod
    def notifica_ritardo(self, utente:IUser, prestito:IPrestito):
        pass
    
    @abstractmethod
    def notifica_disponibilita(self, utente:IUser, elemento:IElement):
        pass

    @abstractmethod
    def notifica_prestito(self, utente: IUser, prestito: IPrestito):
        """
        Notifica un utente riguardo a un nuovo prestito effettuato.

        :param utente: L'utente da notificare.
        :param prestito: Il prestito effettuato.
        """
        pass