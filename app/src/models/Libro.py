from src.models.Interfaces.IElementPrestabile import IElementPrestabile

class Libro(IElementPrestabile):
    def __init__(self, titolo, autore, anno, genere):
        self.id = hash(titolo + autore + str(anno) + genere)
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.genere = genere
        self.disponibile = True  # Attributo per tracciare la disponibilità del libro

    def __str__(self):
        return f"Libro: {self.id} - {self.titolo} by {self.autore} ({self.anno}) - ISBN: {self.genere}"

    def get_id(self):
        return self.id
    
    def get_titolo(self):
        return self.titolo
    
    def is_disponibile(self):
        return self.disponibile

    def set_disponibile(self, disponibile: bool):
        """Imposta la disponibilità del libro."""
        self.disponibile = disponibile
