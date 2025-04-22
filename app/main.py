from src.handlers.Catalogo import Catalogo
from src.handlers.NotificheHandler import NotificheHandler
from src.handlers.PrestitoHandler import PrestitoHandler
from src.models.Libro import Libro
from src.models.Rivista import Rivista
from src.models.User import User
from src.models.Dvd import DVD
from src.service.Interfaces.IBibliotecaService import BibliotecaService


def main():
    print("Benvenuto nel sistema di gestione biblioteca!")
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

    id_elemento = 1  # ID del libro da cercare
    print("Catalogo iniziale:")
    for elemento in Biblioteca.mostra_elementi():
        print(f"{elemento}")  
        id_elemento = elemento.get_id()  # ID del libro da cercare
    
    # Esempio di prestito
    elemento_da_prestare = Biblioteca.cerca_elemento(id_elemento)  # ID del libro da prestare 
    utente = User("mrossi", "Mario Rossi")  # Nome dell'utente che richiede il prestito
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
    tutti_prestiti = Biblioteca.mostra_prestiti_attivi(utente_id)  
    print(f"Prestiti effettuati:")
    for prestito in tutti_prestiti:
        print(f"{prestito}")
    
    # Mostra tutti gli elementi nel catalogo
    print("Catalogo aggiornato:")
    for elemento in Biblioteca.mostra_elementi():
        print(f"{elemento}")
    
    # Esempio di ricerca di un elemento
    elemento_trovato = Biblioteca.cerca_elemento(2)  # ID del libro da cercare
    if elemento_trovato:
        print(f"Elemento trovato: {elemento_trovato.get_titolo()} - {elemento_trovato.get_autore()} ({elemento_trovato.get_anno_pubblicazione()})")
    else:
        print("Elemento non trovato.")

    # Esempio di rimozione di un elemento
    elemento_da_rimuovere = Biblioteca.cerca_elemento(3)  # ID del libro da rimuovere
    Biblioteca.rimuovi_elemento(elemento_da_rimuovere.get_id())
    print(f"Elemento {elemento_da_rimuovere.get_id()} rimosso dal catalogo.")
    # Mostra il catalogo dopo la rimozione
    print("Catalogo dopo la rimozione:")
    for elemento in Biblioteca.mostra_elementi():
        print(f"{elemento.get_id()}: {elemento.get_titolo()} - {elemento.get_autore()} ({elemento.get_anno_pubblicazione()})")

    # Esempio di aggiunta di un nuovo elemento
    nuovo_libro = Libro("Il Codice Da Vinci", "Dan Brown", 2003, "Thriller")
    Biblioteca.aggiungi_elemento(nuovo_libro)
    print(f"Nuovo libro aggiunto: {nuovo_libro.get_titolo()} - {nuovo_libro.get_autore()} ({nuovo_libro.get_anno_pubblicazione()})")
    # Mostra il catalogo dopo l'aggiunta
    print("Catalogo dopo l'aggiunta:")      
    for elemento in Biblioteca.mostra_elementi():
        print(f"{elemento.get_id()}: {elemento.get_titolo()} - {elemento.get_autore()} ({elemento.get_anno_pubblicazione()})")
    
    
    
  


if __name__ == "__main__":
    main()