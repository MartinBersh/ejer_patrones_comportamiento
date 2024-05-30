class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []


    def add_suobordinate(self, subordinates):
        self.subordinates.append(subordinates)

    def __str__(self):
        return f'{self.position}: {self.name}'
