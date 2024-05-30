from patron_visitor.Cliente import Cliente


class ClientePremium(Cliente):
    def accept(self, visitor):
        visitor.visit_cliente_premium(self)