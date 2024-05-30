from patron_visitor.Cliente import Cliente


class ClienteNormal(Cliente):
    def accept(self, visitor):
        visitor.visit_cliente_normal(self)