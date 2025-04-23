
from src.models.Interfaces.IElementPrestabile import IElementPrestabile

class DVD(IElementPrestabile):
    
    def __init__(self, title: str, director: str, year: int, duration: int):
        self.id = hash(title + director + str(year) + str(duration))
        self.title = title
        self.director = director
        self.year = year
        self.duration = duration
        self.disponibile = True

    def __str__(self) -> str:
        return f"DVD: {self.id} - {self.title}, directed by {self.director}, Year: {self.year}, Duration: {self.duration} minutes"
    
    def get_id(self):
        return self.id
    
    def get_titolo(self):
        return self.title
    
    def is_disponibile(self):
        return self.disponibile
    
    def set_disponibile(self, disponibile: bool):
        """Imposta la disponibilità del libro."""
        self.disponibile = disponibile
    
