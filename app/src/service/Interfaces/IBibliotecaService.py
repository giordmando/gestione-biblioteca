import logging
from src.exceptions.biblioteca_exceptions import BibliotecaException, ElementoNonDisponibileException, ElementoNonPrestabileException, ElementoNonTrovatoException
from src.models.Interfaces import IElement
from src.service.Interfaces import ICatalogo
from src.service.Interfaces import IPrestitoService
from src.service.Interfaces import IServizioNotifiche
from src.utils.utility import Utility as utility

class BibliotecaService:
    def __init__(self, catalog: ICatalogo, prestito_service: IPrestitoService, servizio_notifiche: IServizioNotifiche):
        self.catalogo_service = catalog
        self.prestito_service = prestito_service
        self.servizio_notifiche = servizio_notifiche

    def aggiungi_elemento(self, elemento: IElement):
        """Aggiunge un libro al catalogo."""
        self.catalogo_service.aggiungi(elemento)

    def rimuovi_elemento(self, elemento_id):
        """Rimuove un libro dal catalogo."""
        self.catalogo_service.rimuovi(elemento_id)

    def aggiungi_elementi(self, elementi:list[IElement]): # type: ignore
        """Aggiunge più elementi al catalogo."""
        self.catalogo_service.aggiungi_elementi(elementi)

    def cerca_elemento(self, id_elemento):
        return self.catalogo_service.trova_per_id(id_elemento)
    
    def mostra_elementi(self):
        """Restituisce tutti gli elementi del catalogo."""
        return self.catalogo_service.trova_tutti()

    def presta_elemento(self, elemento, user, data_inizio, data_fine):

        """Gestisce il prestito di un elemento."""
        try:
            # Verifica se l'elemento esiste
            if not elemento:
                raise ElementoNonTrovatoException(f"Elemento non trovato")
                
            # Verifica se l'elemento è prestabile
            if not utility.verifica_prestabilita(elemento):
                raise ElementoNonPrestabileException(f"L'elemento '{elemento.get_titolo()}' non è prestabile")
            
            # Verifica se l'elemento è disponibile
            if not elemento.is_disponibile():
                raise ElementoNonDisponibileException(f"L'elemento '{elemento.get_titolo()}' non è disponibile per il prestito")
                
            # Procedi con il prestito
            prestito = self.prestito_service.add_new_prestito(elemento, user, data_inizio, data_fine)
            self.catalogo_service.trova_per_id(elemento.get_id()).set_disponibile(False)
            self.servizio_notifiche.notifica_prestito(user, prestito)
            return prestito
            
        except BibliotecaException as e:
            # Log dell'errore
            logging.error(f"Errore durante il prestito: {str(e)}")
            # Rilancia l'eccezione
            raise
        except Exception as e:
            # Log dell'errore generico
            logging.error(f"Errore imprevisto durante il prestito: {str(e)}")
            # Trasforma in un'eccezione di dominio
            raise BibliotecaException(f"Errore durante l'operazione di prestito: {str(e)}")


    def restituisci_elemento(self, elemento_id, utente_id):
        prestito = self.prestito_service.rimuovi_prestito(elemento_id)
        self.servizio_notifiche.notifica_disponibilita(prestito.get_info_utente(), prestito.get_element())

    def mostra_prestiti_attivi(self):
        """Restituisce i prestiti attivi per un utente."""
        prestiti = self.prestito_service.tutti_prestiti()
        prestiti_attivi = [prestito for prestito in prestiti if not prestito.get_element().is_disponibile()]
        return prestiti_attivi
    
    def mostra_prestiti_utente(self, utente_id):
        """Restituisce i prestiti attivi per un utente."""
        return self.prestito_service.tutti_prestiti_utente(utente_id)
