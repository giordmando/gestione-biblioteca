import logging
from src.models.Prestito import Prestito
from src.models.Interfaces import IPrestito
from src.service.Interfaces.IPrestitoService import IPrestitoService
from src.utils.utility import Utility as utility

class PrestitoHandler(IPrestitoService):
    def __init__(self):
        self.prestiti = {}

    def add_prestito(self, prestito: IPrestito):
        """Aggiunge un prestito al sistema."""
        self.prestiti[prestito.get_element().get_id()] = prestito

    def add_new_prestito(self, elemento, user, data_inizio, data_fine):
        """Aggiunge un nuovo prestito."""
        try:
            utility.verifica_prestabilita(elemento)
            prestito = Prestito(data_inizio, data_fine, elemento, user)
            self.add_prestito(prestito)
            prestito.presta()
            return prestito
        except Exception as e:
            logging.error(f"Errore durante la creazione del prestito: {str(e)}")
            raise

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
    
    def tutti_prestiti_utente(self, user_id: int):
        """Restituisce tutti i prestiti di un utente."""
        return [prestito for prestito in self.prestiti.values() if prestito.get_info_utente().get_id() == user_id] 
    
       