from grafo_mat_adj import GrafoMatrizAdj
import math

def prim(G : GrafoMatrizAdj) -> GrafoMatrizAdj:
    custo: int = 0
    T = GrafoMatrizAdj()
    T.definirN(len(G.V))
    cT: list = [math.inf] * (G.n + 1)
    eT: list = [0] * (G.m + 1)
    cT[1] = None
    for v in G.vertices():
        if(G.M[1][v] == 1):
            cT[v] = G.M[1][v]
            eT[v] = 1 

    lista_aux: list = []
    for i in G.vertices():
        lista_aux.append(i)
    lista_aux.pop(0)

    for i in lista_aux:
        u: int = argMin(cT)
        T.addAresta(u, eT[u])
        custo += G.Peso[u][eT[u]]
        cT[u] = None
        for v in range(1, G.n + 1):
            if(G.M[u][v] == 1 and cT[v] != None):
                if(cT[v] > G.Peso[u][v]):
                    cT[v] = G.Peso[u][v]
                    eT[v] = u
    print(f'Custo: {custo}')
    return T

def argMin(cT: list) -> int:        
    aux = math.inf      
    for i in range(len(cT)):
        if(cT[i] != None and cT[i] < aux and cT[i] !=- 1):
            aux = cT[i]
    return cT.index(aux)