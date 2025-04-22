from src.models.Interfaces.IPrestito import IPrestito
from src.models.Interfaces import IElement, IUser

class Prestito(IPrestito):
    def __init__(self, data_inizio: str, data_fine: str, elemento: IElement, utente: IUser):
        self.data_inizio = data_inizio
        self.data_fine = data_fine
        self.element = elemento
        self.user = utente

    def __str__(self):
        return f"Prestito(disponibile= {self.is_disponibile()}, id_elemento={self.element.get_id()}, data_inizio={self.data_inizio}, data_fine={self.data_fine}, id_elemento={self.element.get_id()}, id_utente={self.user.get_id()})"

    def presta(self):
        """Marks the item as loaned."""
        if not self.element.is_disponibile():
            raise Exception("L'elemento non è disponibile per il prestito.")
        self.element.set_disponibile(False)

    def restituisci(self):
        """Marks the item as returned."""
        if self.element.is_disponibile():
            raise Exception("L'elemento è già disponibile.")
        self.element.set_disponibile(True)

    def is_disponibile(self):
        """Checks if the item is available for loan."""
        return self.element.is_disponibile()

    def get_data_prestito(self):
        """Returns the start date of the loan."""
        return self.data_inizio

    def get_data_scadenza(self):
        """Returns the end date of the loan."""
        return self.data_fine

    def get_info_utente(self):
        """Returns the user ID associated with the loan."""
        return self.user

    def get_element(self):
        """Returns the item ID associated with the loan."""
        return self.element  