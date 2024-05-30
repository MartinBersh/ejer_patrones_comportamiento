from Employee import Employee
from Organization import Organization

if __name__ == "__main__":

    jefe = Employee("Juan", "Jefe")
    ventas = Employee("Mario", "Ventas")
    marketing = Employee("Jaime", "Marketing")
    rh = Employee("David", "Recusos humanos")
    ventas2 = Employee("María", "Subordinado ventas")
    marketing2 = Employee("Camila", "Subordinado Marketing")

    jefe.add_suobordinate(ventas)
    jefe.add_suobordinate(marketing2)
    ventas.add_suobordinate(ventas2)
    marketing.add_suobordinate(marketing2)

    org = Organization(jefe)

    for employee in org:
        print(employee)
