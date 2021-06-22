from abc import ABC, abstractmethod
from produtos.classes.Caracteristicas import Tamanho600ml, Tamanho1litro, Tamanho2litros, Tamanho3litros


class Produto(ABC):
    def __init__(self, implementation):
        if isinstance(implementation, Tamanho600ml):
            self.implementation = implementation
        if isinstance(implementation, Tamanho1litro):
            self.implementation = implementation
        if isinstance(implementation, Tamanho2litros):
            self.implementation = implementation
        if isinstance(implementation, Tamanho3litros):
            self.implementation = implementation


    @abstractmethod
    def operation(self):
        pass


class CocaCola(Produto):
    def operation(self):
        
        return (f"CocaCola tamanho:"
                f"{self.implementation.operation_implementation()}")


class Pepsi(Produto):
    def operation(self):
        return (f"Pepsi tamanho:"
                f"{self.implementation.operation_implementation()}")


class GuaranaAntartica(Produto):
    def operation(self):
        return (f"Guaraná Antartica tamanho:"
                f"{self.implementation.operation_implementation()}")


class Dolly(Produto):
    def operation(self):
        return (f"Dolly tamanho:"
                f"{self.implementation.operation_implementation()}")