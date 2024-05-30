from abc import ABC, abstractmethod


class Cliente(ABC):
    def __init__(self, nombre, fecha_nacimiento, direccion):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion

    @abstractmethod
    def accept(self, visitor):
        pass