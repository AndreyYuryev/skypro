class Box:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f"Init Box a = {self.a} b = {self.b}")

class Container(Box):
    def __init__(self, a, b, c):
        self.c = c
        super().__init__(a + 10, b + 10)
        print(f"Init Container a = {self.a} b = {self.b} c = {self.c}")


my_object = Container(1, 2, 3)
my_object = Box(4, 5)