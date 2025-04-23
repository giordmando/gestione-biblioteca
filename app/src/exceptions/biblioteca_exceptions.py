class BibliotecaException(Exception):
    """Classe base per tutte le eccezioni della biblioteca"""
    pass

class ElementoNonPrestabileException(BibliotecaException):
    """Sollevata quando si tenta di prestare un elemento non prestabile"""
    pass

class ElementoNonDisponibileException(BibliotecaException):
    """Sollevata quando si tenta di prestare un elemento non disponibile"""
    pass

class ElementoGiaPrestatoException(BibliotecaException):
    """Sollevata quando si tenta di prestare un elemento già in prestito"""
    pass

class ElementoNonTrovatoException(BibliotecaException):
    """Sollevata quando un elemento non è presente nel catalogo"""
    pass

class UtenteNonAutorizzatoException(BibliotecaException):
    """Sollevata quando un utente non è autorizzato a effettuare un'operazione"""
    pass