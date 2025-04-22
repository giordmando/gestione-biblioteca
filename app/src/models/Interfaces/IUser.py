from abc import ABC, abstractmethod

class IUser(ABC):

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_username(self):
        pass
    
    @abstractmethod
    def get_name(self):
        pass

