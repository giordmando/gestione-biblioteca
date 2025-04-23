from src.models.Interfaces.IUser import IUser


class User(IUser):
    def __init__(self, id:int, username: str, nome: str):
        self.id = id
        self.name = nome
        self.username = username

    def get_id(self) -> int:
        return self.id
    
    def get_username(self) -> str:
        return self.username

    def set_username(self, username: str) -> None:
        self.username = username

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name