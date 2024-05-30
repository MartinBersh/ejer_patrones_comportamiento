from patron_visitor.Cliente import Cliente


class ClienteNuevo(Cliente):
    def accept(self, visitor):
        visitor.visit_cliente_nuevo(self)