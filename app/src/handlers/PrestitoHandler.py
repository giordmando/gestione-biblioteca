from src.models.Prestito import Prestito
from src.models.Interfaces import IElement, IPrestito, IUser
from src.service.Interfaces.IPrestitoService import IPrestitoService

class PrestitoHandler(IPrestitoService):
    def __init__(self):
        self.prestiti = {}

    def add_prestito(self, prestito: IPrestito):
        """Aggiunge un prestito al sistema."""
        self.prestiti[prestito.get_element().get_id()] = prestito

    def add_new_prestito(self, elemento:IElement, user:IUser, data_inizio:str, data_fine:str):
        """Aggiunge un nuovo prestito."""
        prestito = Prestito(data_inizio, data_fine, elemento, user)
        self.add_prestito(prestito)
        prestito.presta()
        return prestito

    def rimuovi_prestito(self, id: int):
        """Rimuove un prestito dal sistema."""
        if id in self.prestiti:
            prestito = self.prestiti[id]
            prestito.restituisci()
        else:
            raise Exception("Prestito non trovato.")
        return prestito
    
    def ricerca_prestito(self, id: int):
        """Cerca un prestito per ID."""
        return self.prestiti.get(id, None)  

    def tutti_prestiti(self):
        """Restituisce tutti i prestiti."""
        return list(self.prestiti.values()) 
    
       