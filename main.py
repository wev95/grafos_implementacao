import json
from grafo_mat_adj import GrafoMatrizAdj
from grafo_lista_adj import GrafoListaAdj
from json_format import JsonFormat

# matriz adjacente
grafoM = GrafoMatrizAdj()
grafoM.definirN(6)
listaMatriz = []

# lista adjacente
# grafoL = GrafoListaAdj()
# grafoL.definirN(6)
# listaList = []

arquivo = open("arquivo.txt", "r")
for linha in arquivo:
    aux = linha.split(" ")
    v1 = int(aux[0])
    v2 = int(aux[1].split("\\")[0])
    grafoM.addAresta(v1, v2)
    # grafoL.addAresta(v1, v2)

print(grafoM.ehArvore())
# resp = JsonFormat(grafoM.vertices(), grafoM.getArestas())
# print(json.dumps(resp.__dict__)) 
# grafoM.removeVertice(2)
# resp = JsonFormat(grafoM.vertices(), grafoM.getArestas())
# print(json.dumps(resp.__dict__)) 
# arquivo.close()