from patron_visitor.Visitor import Visitor


class MensajeVisitor(Visitor):
    def visit_cliente_premium(self, cliente):
        print(f"Enviando mensaje VIP a {cliente.nombre}")

    def visit_cliente_normal(self, cliente):
        print(f"Enviando mensaje normal a {cliente.nombre}")

    def visit_cliente_nuevo(self, cliente):
        print(f"Enviando mensaje de bienvenida a {cliente.nombre}")
