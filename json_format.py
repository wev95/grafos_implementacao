class JsonFormat:
    def __init__(self, vertices: list, arestas: list):
        self.nome = "GRAFO_G1_SLIDE_GRUPO_N_6"
        self.vertices = vertices
        self.arestas = arestas

    def getNome(self):
        return self.nome

    def getVertices(self):
        return self.vertices

    def getArestas(self):
        return self.arestas

    Nome = property(getNome)
    Vertices = property(getVertices)
    Arestas = property(getArestas)