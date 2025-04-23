from src.exceptions.biblioteca_exceptions import BibliotecaException, ElementoNonDisponibileException, ElementoNonPrestabileException
from src.handlers.Catalogo import Catalogo
from src.handlers.NotificheHandler import NotificheHandler
from src.handlers.PrestitoHandler import PrestitoHandler
from src.models.Libro import Libro
from src.models.Rivista import Rivista
from src.models.User import User
from src.models.Dvd import DVD
from src.service.Interfaces.IBibliotecaService import BibliotecaService
from src.utils.utility import Utility as utility


def main():
    print("\n\nBenvenuto nel sistema di gestione biblioteca!\n\n")
    # Aggiungi qui il codice per avviare l'applicazione

    libri = [
        Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, "Fantasy"),
        Libro("1984", "George Orwell", 1949, "Dystopian"),
        Libro("Il Grande Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
    ]

    dvd = [DVD("Inception", "Christopher Nolan", 2010, 148),
           DVD("The Matrix", "Lana Wachowski", 1999, 136)]
    
    riviste = [Rivista("National Geographic", "National Geographic Society", 1888),
               Rivista("TIME", "Time USA, LLC", 1923)]
    
    catalogo = Catalogo()
    notifiche_handler = NotificheHandler()
    prestito_handler = PrestitoHandler()

    Biblioteca = BibliotecaService(catalogo, prestito_handler, notifiche_handler)
    Biblioteca.aggiungi_elementi(libri) 
    Biblioteca.aggiungi_elementi(dvd)
    Biblioteca.aggiungi_elementi(riviste)

    try:
        id_elemento = 1  # ID del libro da cercare
        id_elemento_no_prest = 0
        print("Catalogo iniziale:")
        for elemento in Biblioteca.mostra_elementi():
            print(f"{elemento}") 
            if utility.verifica_prestabilita(elemento): 
                id_elemento = elemento.get_id()  # ID da cercare
            else:
                id_elemento_no_prest = elemento.get_id()  # ID da cercare
        
        # Esempio di prestito
        elemento_da_prestare = Biblioteca.cerca_elemento(id_elemento)  # ID dell'elemento da prestare 
        utente = User(1, "mrossi", "Mario Rossi")  # Nome dell'utente che richiede il prestito
        utente_2 = User(2, "mbianchi", "Mario Bianchi")  # Nome dell'utente che richiede il prestito
        data_inizio = "2023-10-01"  # Data di inizio prestito
        data_fine = "2023-10-15"  # Data di fine prestito       

        prestito = Biblioteca.presta_elemento(elemento_da_prestare, utente, data_inizio, data_fine)
        print(f"Prestito effettuato: {prestito}")   

        # Esempio di restituzione
        elemento_da_restituire = Biblioteca.cerca_elemento(id_elemento)  # ID del libro da restituire
        utente_id = utente.get_id()  # Nome dell'utente che restituisce il libro
        Biblioteca.restituisci_elemento(elemento_da_restituire.get_id(), utente_id)
        print(f"Elemento {elemento_da_restituire.get_id()} restituito da {utente_id}.")
        
        # Mostra i prestiti attivi
        tutti_prestiti = Biblioteca.mostra_prestiti_attivi()  
        print(f"Prestiti effettuati:")
        for prestito in tutti_prestiti:
            print(f"{prestito}")
        
        id_elemento_2 = 2
        id_elemento_3 = 3
        # Mostra tutti gli elementi nel catalogo
        print("Catalogo aggiornato:")
        for elemento in Biblioteca.mostra_elementi():
            print(f"{elemento}")
            if id_elemento_2==2 and utility.verifica_prestabilita(elemento): 
                id_elemento_2 = elemento.get_id()  # ID del libro da cercare
            elif id_elemento_3==3 and utility.verifica_prestabilita(elemento): 
                id_elemento_3 = elemento.get_id()  # ID del libro da cercare
        
        
        # Esempio di ricerca di un elemento
        elemento_trovato = Biblioteca.cerca_elemento(id_elemento_2)  # ID del libro da cercare
        if elemento_trovato:
            print(f"Elemento trovato: {elemento_trovato}")
        else:
            print("Elemento non trovato.")

        # Esempio di rimozione di un elemento
        elemento_da_rimuovere = Biblioteca.cerca_elemento(id_elemento_3)  # ID del libro da rimuovere
        Biblioteca.rimuovi_elemento(elemento_da_rimuovere.get_id())
        print(f"Elemento {elemento_da_rimuovere.get_id()} rimosso dal catalogo.")
        # Mostra il catalogo dopo la rimozione
        print("Catalogo dopo la rimozione:")
        for elemento in Biblioteca.mostra_elementi():
            print(f"{elemento}")

        # Esempio di aggiunta di un nuovo elemento
        nuovo_libro = Libro("Il Codice Da Vinci", "Dan Brown", 2003, "Thriller")
        Biblioteca.aggiungi_elemento(nuovo_libro)
        print(f"Nuovo elemento aggiunto: {nuovo_libro}")
        # Mostra il catalogo dopo l'aggiunta
        print("Catalogo dopo l'aggiunta:")      
        for elemento in Biblioteca.mostra_elementi():
            print(f"{elemento}")
        
        # Esempio di prestito di un elemento non prestabile
        elemento_non_prestabile = Biblioteca.cerca_elemento(id_elemento_no_prest)  # ID dell'elemento non prestabile   
        try:
            prestito_non_prestabile = Biblioteca.presta_elemento(elemento_non_prestabile, utente, data_inizio, data_fine)
            print(f"Prestito effettuato: {prestito_non_prestabile}")
        except ElementoNonPrestabileException as e:
            print(f"Errore: {str(e)}")
        except ElementoNonDisponibileException as e:
            print(f"Errore: {str(e)}")
        except BibliotecaException as e:
            print(f"Errore di biblioteca: {str(e)}")
        except Exception as e:
            print(f"Errore imprevisto: {str(e)}")

        # generiamo 2 prestiti per utente2 e poi restiuiamo tutti i prestiti dell'utente2
        elemento_da_prestare_2 = Biblioteca.cerca_elemento(id_elemento)  # ID dell'elemento da prestare 
        elemento_da_prestare_3 = Biblioteca.cerca_elemento(id_elemento_2)  # ID dell'elemento da prestare
        prestito_2 = Biblioteca.presta_elemento(elemento_da_prestare_2, utente_2, data_inizio, data_fine)   
        
        prestito_3 = Biblioteca.presta_elemento(elemento_da_prestare_3, utente_2, data_inizio, data_fine)
        print(f"Prestito effettuato: {prestito_2}")
        print(f"Prestito effettuato: {prestito_3}") 

        # Mostra i prestiti attivi
        tutti_prestiti_utente_2 = Biblioteca.mostra_prestiti_utente(utente_2.get_id())
        print(f"Prestiti effettuati da {utente_2.get_name()}:")
        for prestito in tutti_prestiti_utente_2:
            print(f"{prestito}")

    
    except ElementoNonPrestabileException as e:
        print(f"Errore: {str(e)}")
    except ElementoNonDisponibileException as e:
        print(f"Errore: {str(e)}")
    except BibliotecaException as e:
        print(f"Errore di biblioteca: {str(e)}")
    except Exception as e:
        print(f"Errore imprevisto: {str(e)}")
        
  


if __name__ == "__main__":
    main()