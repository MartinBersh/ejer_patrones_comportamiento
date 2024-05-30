from patron_visitor.ClienteNormal import ClienteNormal
from patron_visitor.ClienteNuevo import ClienteNuevo
from patron_visitor.ClientePremium import ClientePremium
from patron_visitor.MensajeVIsitor import MensajeVisitor


def main():
    clientes = [
        ClientePremium("Martin", "1980-05-15", "Calle 15N"),
        ClienteNormal("Carlos", "1990-06-20", "Kra 18 #66"),
        ClienteNuevo("Gustavo", "2000-07-25", "Av 14 #10-45")
    ]

    mensaje_visitor = MensajeVisitor()

    for cliente in clientes:
        cliente.accept(mensaje_visitor)

if __name__ == "__main__":
    main()
