import math
import sys
from Objetos.centroide import Centroide
import numpy as np

class Kmeans:
    def __init__(self, numero_centroides):
        self.numero_centroides = numero_centroides
        self.centroides = [Centroide(i) for i in range(numero_centroides)]

    def classifica_amostras(self, bd):
        for bairro in bd.bairros:
            menor_distancia = sys.maxsize
            for centroide in self.centroides:
                distancia_atual = math.sqrt((bd.bairros[bairro]['coordenadas'][0] - centroide.posicao[0]) ** 2 + (bd.bairros[bairro]['coordenadas'][1] - centroide.posicao[1]) ** 2)
                if distancia_atual <= menor_distancia:
                    menor_distancia = distancia_atual
                    bd.bairros[bairro]['centroide'] = centroide.nome

            if bd.bairros[bairro]['centroide'] == 0:
                self.centroides[0].bairros.append(bairro)
                self.centroides[0].num_bairros += 1
            elif bd.bairros[bairro]['centroide'] == 1:
                self.centroides[1].bairros.append(bairro)
                self.centroides[1].num_bairros += 1
            elif bd.bairros[bairro]['centroide'] == 2:
                self.centroides[2].bairros.append(bairro)
                self.centroides[2].num_bairros += 1
            elif bd.bairros[bairro]['centroide'] == 3:
                self.centroides[3].bairros.append(bairro)
                self.centroides[3].num_bairros += 1

    def move_centroides(self, bd):
        for centroide in range(self.numero_centroides):
            nova_posicao = np.zeros(bd.dimensoes)
            for bairro in self.centroides[centroide].bairros:
                for componente in range(bd.dimensoes):
                    nova_posicao[componente] += bd.bairros[bairro]['coordenadas'][componente]
            for componente in range(bd.dimensoes):
                self.centroides[centroide].posicao[componente] = nova_posicao[componente]/3
