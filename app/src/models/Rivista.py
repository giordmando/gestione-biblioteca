from src.models.Interfaces.IElement import IElement

class Rivista(IElement):
    
    def __init__(self, titolo, editore, anno_pubblicazione):
        self.id = hash(titolo + editore + str(anno_pubblicazione))
        self.titolo = titolo
        self.editore = editore
        self.anno_pubblicazione = anno_pubblicazione
        self.disponibile = True

    def __str__(self):
        return f"Rivista: {self.id} - {self.titolo}, Editore: {self.editore}, Anno: {self.anno_pubblicazione}"
    
    def get_id(self):
        return self.id
    
    def get_titolo(self):
        return self.titolo
    
    def is_disponibile(self):
        return self.disponibile
    
    def set_disponibile(self, disponibile: bool):
        """Imposta la disponibilità del libro."""
        self.disponibile = disponibile