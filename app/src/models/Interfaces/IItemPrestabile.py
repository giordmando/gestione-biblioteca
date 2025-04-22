from abc import ABC, abstractmethod

class IItemPrestabile(ABC):
    
    @abstractmethod
    def is_disponibile(self):
        pass

    @abstractmethod
    def set_disponibile(self, disponibile: bool):
        pass