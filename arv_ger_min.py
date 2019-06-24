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


# matriz adjacente
grafoM = GrafoMatrizAdj()
grafoM.definirN(6)

arquivo = open("arquivo.txt", "r")
for linha in arquivo:
    aux = linha.split(" ")
    v1 = int(aux[0])
    v2 = int(aux[1].split("\\")[0])
    peso = int(aux[2].split("\\")[0])
    grafoM.AddPeso(v1, v2, peso)
    grafoM.addAresta(v1, v2)

print(prim(grafoM).getArestas())
arquivo.close()