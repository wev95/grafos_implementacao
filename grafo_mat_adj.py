from grafo import Grafo

class GrafoMatrizAdj(Grafo):

    def definirN(self, n):
        super(GrafoMatrizAdj, self).definirN(n)
        self.M = [None] * (self.n + 1)
        self.V = [i for i in range(1, (self.n + 1))]
        for i in range(1, self.n + 1):
            self.M[i] = [0] * (self.n + 1)

    def addAresta(self, u, v):
        self.M[u][v] = 1
        self.M[v][u] = 1
        self.m += 1

    def removeAresta(self, u, v):
        self.M[u][v] == 0
        self.M[v][u] == 0
        self.m -= 1

    def saoAdj(self, v1, v2):
        return self.M[v1][v2] == 1

    def getListVerticesAdj(self, v):
        lista = []
        for i in range(1, self.n + 1):
            if(self.saoAdj(v, i)):
                lista.append(i)
        return lista

    def getArestas(self):
        lista = []
        verticesAux = self.vertices()
        for v1 in verticesAux:
            for v2 in verticesAux:
                if(self.saoAdj(v1, v2) and (not [f'{v2}', f'{v1}'] in lista)):
                    lista.append([f'{v1}', f'{v2}'])
        return lista