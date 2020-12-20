import math
import sys
from Objetos.centroide import Centroide

class Kmeans:
    def __init__(self, numero_centroides):
        self.centroides = [Centroide(i) for i in range (numero_centroides)]

    def clusterizacao(self, bd):
        for bairro in bd.bairros:
            menor_distancia = sys.maxsize
            for centroide in self.centroides:
                distancia_atual = math.sqrt((bd.bairros[bairro]['coordenadas'][0] - centroide.posicao[0]) ** 2 + (bd.bairros[bairro]['coordenadas'][1] - centroide.posicao[1]) ** 2)
                if distancia_atual <= menor_distancia:
                    menor_distancia = distancia_atual
                    bd.bairros[bairro]['centroide'] = centroide.nome

            if bd.bairros[bairro]['centroide'] == 0:
                self.centroides[0].bairros.append(bairro)
            elif bd.bairros[bairro]['centroide'] == 1:
                self.centroides[1].bairros.append(bairro)
            elif bd.bairros[bairro]['centroide'] == 2:
                self.centroides[2].bairros.append(bairro)


