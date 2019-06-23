class Grafo:
    def __init__(self):
        self.n: int = 0
        self.m: int = 0
        self.V: list = None
        self.Peso: list = None

    def definirN(self, n):
        self.n = n
        self.m = 0
        self.V = [i for i in range(1, (self.n + 1))]

    def vertices(self):
        return self.V
