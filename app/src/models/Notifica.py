from src.models.Interfaces.INotifica import INotifica
from src.models.Interfaces import IUser, IPrestito

class Notifica(INotifica):
    def __init__(self, utente: IUser, prestito: IPrestito, messaggio: str):
        self._utente = utente
        self._prestito = prestito
        self._messaggio = messaggio

    def get_utente(self) -> IUser:
        return self._utente

    def get_prestito(self) -> IPrestito:
        return self._prestito

    def get_messaggio(self) -> str:
        return self._messaggio