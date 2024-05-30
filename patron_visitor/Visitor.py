from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_cliente_premium(self, cliente):
        pass

    @abstractmethod
    def visit_cliente_normal(self, cliente):
        pass

    @abstractmethod
    def visit_cliente_nuevo(self, cliente):
        pass
