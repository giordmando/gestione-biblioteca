from src.models.Interfaces import IElement
from src.service.Interfaces.ICatalogo import ICatalogo


class Catalogo(ICatalogo):
    def __init__(self):
        self.elementi = {}

    def aggiungi(self, elemento: IElement) -> None:
        """Aggiunge un elemento al catalogo."""
        self.elementi[elemento.get_id()] = elemento

    def aggiungi_elementi(self, elementi: list[IElement]) -> None: # type: ignore
        """Aggiunge più elementi al catalogo."""
        for elemento in elementi:
            self.aggiungi(elemento)

    def rimuovi(self, elemento_id: int) -> None:
        """Rimuove un elemento dal catalogo."""
        if elemento_id in self.elementi:
            del self.elementi[elemento_id]
   
    def trova_per_id(self, elemento_id):
        """Trova un elemento per ID."""
        return self.elementi.get(elemento_id, None)
    
    def trova_tutti(self):
        """Restituisce tutti gli elementi del catalogo."""
        return list(self.elementi.values())