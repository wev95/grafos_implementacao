class Grafo:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.V = None

    def definirN(self, n):
        self.n = n
        self.m = 0
        self.V = [i for i in range(1, (self.n + 1))]

    def vertices(self):
        return self.V
