from grafo import Grafo
from estrutura_de_dados.pilha import Pilha

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
        if(v1 > (self.n - 1)):
            aux = self.createMatrizAdj()
            for u in range(1, self.n):
                for v in range(1, self.n):
                    aux[u][v] = self.M[u][v]
            self.M = aux

    def removeVertice(self, v1 : int) -> bool:
        self.V.remove(v1)
        self.n -= 1
        for v2 in self.getListVerticesAdj(v1):
            self.removeAresta(v1, v2)
        return False

    def addAresta(self, v1: int, v2: int):
        self.M[v1][v2] = 1
        self.M[v2][v1] = 1
        self.m += 1

    def removeAresta(self, v1: int, v2: int):
        self.M[v1][v2] = 0
        self.M[v2][v1] = 0
        self.m -= 1

    def is_adj(self, v1, v2) -> bool:
        return self.M[v1][v2] == 1

    def getListVerticesAdj(self, v1: int) -> list:
        return [v2 for v2 in range(1, self.n + 1) if(self.is_adj(v1, v2))]     

    def getArestas(self) -> list:
        lista = []
        for v1 in self.V:
            for v2 in self.V:
                if(self.is_adj(v1, v2) and (not [f'{v2}', f'{v1}'] in lista)):
                    lista.append([f'{v1}', f'{v2}'])
        return lista

    def createMatrizAdj(self) -> list:
        aux = [None] * (self.n + 1)
        for i in range(1, self.n + 1):
            aux[i] = [0] * (self.n + 1)
        return aux

    #  CheckPoint 2

    def rotular(self):
        self.visitado = [False] * (self.n + 1)
        for i in range(1, (self.n + 2)):
            self.explorado.append([False] * (self.n + 1))
            self.descoberto.append([False] * (self.n + 1))
    
    # Slide 5
    def busca(self):
        self.rotular()     
        self.buscaSlide5(1)

    def buscaSlide5(self, r: int):
        self.visitado[r] = True
        for i in self.V:
            for j in self.V:             
                if(self.visitado[i] and  not self.explorado[i][j] and self.M[i][j] == 1):
                    self.explorado[i][j] = True
                    if(not self.visitado[j]):
                        self.visitado[j] = True
                        self.descoberto[i][j] = True 
                        self.descoberto[j][i] = True 

    #Slide 6
    def buscaCompleta(self):
        self.rotular()
        for i in self.V:
            if(not self.visitado[i]):
                self.buscaSlide5(i)

    # Slide 9
    def ehConexo(self) -> bool:
        self.busca()
        for i in self.V:
            if(not self.visitado[i]):
                return False
        return True  

    # Slide 10
    def temCiclo(self) -> bool:
        self.buscaCompleta()
        for i in self.V:
            for j in self.V:
                if(self.M[i][j] == 1 and not self.descoberto[i][j]):
                    return True
        return False

    # Slide 11
    def ehFloresta(self) -> bool:
        return not self.temCiclo()

    # Slide 12
    def ehArvore(self) -> bool:
        self.busca()
        for i in self.V:
            if(not self.visitado[i]):
                return False
        return True  

    # Slide 13
    def ehArvoreSlide13(self) -> bool:
        return self.ehConexo and not self.temCiclo()

    # Slide 17
    def obterFlorestaGeradora(self):
        T = GrafoMatrizAdj()
        T.n = self.n
        T.M = self.createMatrizAdj()
        self.buscaCompleta()
        print(self.M)
        for i in self.V:
            for j in self.V:
                if(self.M[i][j] == 1 and self.descoberto[i][j]):
                    T.M[i][j] = 1
        return T

    # Slide 26
    def buscaProfundidade(self, v: int):
        pilha = Pilha()
        self.visitado[v] = True
        pilha.push(v)
        pilha.push(self.primeiroViz(v))
        while(pilha.lenght() > 0):
            v = pilha.pop()
            w = v
            while(w > 0):
                pilha.push(v)
                pilha.push(self.proximoViz(v, w))
                if(self.visitado[w]):
                    if (self.M[v][w] == 1 and not self.explorado[v][w]):
                        self.explorado[v][w]=True
                else:
                    self.explorado[v][w] = True
                    self.descoberto[v][w] = True
                    self.visitado[w] = True
                    pilha.push(w)
                    pilha.push(self.primeiroViz(w))
        return None

    def primeiroViz(self, v1: int) -> int:
        for v2 in self.V:
            if(self.M[v1][v2] == 1):
                return v2
        return 0

    def proximoViz(self, v1: int, index: int) -> int:
        for v2 in range(index, len(self.M)):
            if(self.M[v1][v2] == 1):
                return v2
        return 0

        # 27, 57, 62