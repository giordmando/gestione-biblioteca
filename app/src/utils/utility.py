from src.models.Interfaces.IElementPrestabile import IElementPrestabile
from src.exceptions.biblioteca_exceptions import ElementoNonPrestabileException


class Utility:
    @staticmethod
    def verifica_prestabilita(elemento):
        """Verifica che un elemento sia prestabile"""
        if not isinstance(elemento, IElementPrestabile):
            print(f"Errore: L'elemento '{elemento.get_titolo()}' non è prestabile")
            return False
        return True
