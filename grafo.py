class Grafo:
    def __init__(self, orientado = False):
        self.n = 0
        self.m = 0
        
    def definirN(self, n):
        self.n = n
        self.m = 0

    def vertices(self):
        lista = []
        for i in range(1, self.n + 1):
            lista.append(i)
        return lista
