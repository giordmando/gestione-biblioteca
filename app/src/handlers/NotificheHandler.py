from src.models.Notifica import Notifica
from src.service.Interfaces.IServizioNotifiche import IServizioNotifiche
from src.models.Interfaces import IElement, IUser, IPrestito

class NotificheHandler(IServizioNotifiche):
    def __init__(self):
        self.notifiche = []

    def notifica_ritardo(self, utente: IUser, prestito: IPrestito):
        messaggio = f"Caro {utente.get_name()}, il prestito dell'elemento '{prestito.get_element().get_titolo()}' è in ritardo. Ti invitiamo a restituirlo al più presto."
        notifica = Notifica(utente, prestito, messaggio)
        self.notifiche.append(notifica)
        self._invia_notifica(notifica)

    def notifica_disponibilita(self, utente: IUser, elemento: IElement):
        messaggio = f"Caro {utente.get_name()}, l'elemento '{elemento.get_titolo()}' è ora disponibile per il prestito."
        notifica = Notifica(utente, None, messaggio)
        self.notifiche.append(notifica)
        self._invia_notifica(notifica)

    def notifica_prestito(self, utente: IUser, prestito: IPrestito):
        messaggio = f"Caro {utente.get_name()}, il prestito dell'elemento '{prestito.get_element().get_titolo()}' è stato registrato con successo."
        notifica = Notifica(utente, prestito, messaggio)
        self.notifiche.append(notifica)
        self._invia_notifica(notifica)

    def _invia_notifica(self, notifica: Notifica):
        """
        Metodo privato per inviare una notifica.
        In questa implementazione, stampa semplicemente il messaggio.
        """
        print(f"Inviando notifica a {notifica.get_utente().get_name()}: {notifica.get_messaggio()}")

    def rimuovi_notifica(self, utente: IUser, prestito: IPrestito) -> None:
        """Rimuove una notifica per un utente."""
        self.notifiche = [
            n for n in self.notifiche if n["utente"] != utente or n["prestito"] != prestito
        ]

    def mostra_notifiche(self, utente: IUser) -> list:
        """Mostra tutte le notifiche per un utente."""
        return [n for n in self.notifiche if n["utente"] == utente]
   