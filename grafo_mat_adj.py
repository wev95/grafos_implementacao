from grafo import Grafo

class GrafoMatrizAdj(Grafo):

    def definirN(self, n):
        super(GrafoMatrizAdj, self).definirN(n)
        self.M = self.createMatrizAdj()

    def addVertice(self, v1):
        self.V.append(v1)
        self.V.sort()
        self.n += 1
        # verifica se o vertice adicionado ja não esteve no grafo
        if(v1 > self.n - 1):
            aux = self.createMatrizAdj()
            for u in range(1, self.n):
                for v in range(1, self.n):
                    aux[u][v] = self.M[u][v]
            self.M = aux

    def removeVertice(self, v1):
        self.V.remove(v1)
        self.n -= 1
        for v2 in self.getListVerticesAdj(v1):
            self.removeAresta(v1, v2)
        return False

    def addAresta(self, v1, v2):
        self.M[v1][v2] = 1
        self.M[v2][v1] = 1
        self.m += 1

    def removeAresta(self, v1, v2):
        self.M[v1][v2] = 0
        self.M[v2][v1] = 0
        self.m -= 1

    def is_adj(self, v1, v2):
        return self.M[v1][v2] == 1

    def getListVerticesAdj(self, v):
        lista = []
        for i in range(1, self.n + 1):
            if(self.is_adj(v, i)):
                lista.append(i)
        return lista

    def getArestas(self):
        lista = []
        verticesAux = self.vertices()
        for v1 in verticesAux:
            for v2 in verticesAux:
                if(self.is_adj(v1, v2) and (not [f'{v2}', f'{v1}'] in lista)):
                    lista.append([f'{v1}', f'{v2}'])
        return lista

    def createMatrizAdj(self):
        aux = [None] * (self.n + 1)
        for i in range(1, self.n + 1):
            aux[i] = [0] * (self.n + 1)
        return aux