from grafo import Grafo

class GrafoListaAdj(Grafo):
    class NoAresta:
        def __init__(self):
            self.Viz = None
            self.e = None
            self.Prox = None
    
    class Aresta:
        def __init__(self):
            self.v1 = None
            self.No1 = None
            self.v2 = None
            self.No2 = None
        
    def definirN(self, n):
        super(GrafoListaAdj, self).definirN(n)
        self.L = [None] * (self.n + 1)
        for i in range(1, self.n + 1):
            self.L[i] = GrafoListaAdj.NoAresta()

    def addAresta(self, u, v):
        
        def addLista(u, v, e):
            no = GrafoListaAdj.NoAresta()
            no.viz = v
            no.e = e
            no.prox = self.L[u].Prox
            self.L[u].Prox =  no
            return no
        
        e = GrafoListaAdj.Aresta()
        e.v1 = u
        e.v2 = v
        e.No1 = addLista(u, v, e)
        e.No2 = addLista(v, u, e)
        self.m += 1
        return e
            
        def removeAresta(self, uv):
            
            def removeLista(no):
                no.ant.prox = no.prox
                if(no.prox != None):
                    no.prox.ant = no.ant
                    
            removeLista(uv.No1)
            removeLista(uv.No2)
