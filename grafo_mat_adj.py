from grafo import Grafo

class GrafoMatrizAdj(Grafo):

    def definirN(self, n: int):
        super(GrafoMatrizAdj, self).definirN(n)
        self.M = self.createMatrizAdj()
        self.explorado = []
        self.visitado = []
        self.descoberto = []

    def addVertice(self, v1: int):
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

    def removeAresta(self, v1: int, v2: int):
        self.M[v1][v2] = 0
        self.M[v2][v1] = 0
        self.m -= 1

    def is_adj(self, v1, v2):
        return self.M[v1][v2] == 1

    def getListVerticesAdj(self, v: int):
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

    #  CheckPoint 2

    def rotular(self):
        self.visitado= [False] * self.n
        for i in range(self.n):
            self.explorado.append([False] * self.n)
            self.descoberto.append([False]* self.n)
    
    # Slide 5
    def busca(self):
        self.rotular()           
        self.buscaSlide5(3)

    def buscaSlide5(self, r: int):
        self.visitado[r] = True
        for i in range(self.n):
            for j in range(self.n):                    
                if(self.visitado[i] and  not self.explorado[i][j]):
                    self.explorado[i][j] = True
                    if(not self.visitado[j]):
                        self.visitado[j] = True
                        self.descoberto[i][j] = True 

    #Slide 6
    def buscaCompleta(self):
        self.rotular()
        for i in range(self.n):
            if( not self.visitado[i]):
                self.buscaSlide5(i)

    # Slide 9
    def ehConexo(self) -> bool:
        self.busca()
        for i in range(self.n):
            if(not self.visitado[i]):
                return False
            return True  

    # Slide 10
    def temCiclo(self) -> bool:
        self.buscaCompleta()
        for i in range(self.n):
            for j in range(self.n):
                if(self.m[i][j] == 1):
                    if(not self.descoberto[i][j]):
                        return True
        return False

    # Slide 11
    def ehFloresta(self) -> bool:
        return not self.temCiclo()

    # Slide 12
    def ehArvore(self) -> bool:
        self.busca()
        for i in range(self.n):
            if(not self.visitado[i]):
                return False
            return True  

    # Slide 13
    def ehArvoreSlide13(self) -> bool:
        return self.ehConexo and not self.temCiclo()

    # Slide 17
    # def obterFlorestaGeradora(self) -> GrafoMatrizAdj:
    #     T = GrafoMatrizAdj()
    #     T.n = self.n
    #     T.m = self.m
    #     self.buscaCompleta()

    #     return T