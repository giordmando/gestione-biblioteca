from src.models.Interfaces.IElement import IElement
from src.models.Interfaces.IItemPrestabile import IItemPrestabile

class IElementPrestabile(IElement, IItemPrestabile):
    """Un'interfaccia che rappresenta elementi che possono essere prestati."""
    pass