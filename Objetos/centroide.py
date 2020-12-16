import numpy as np
from bancodedados import BancoDeDados as bd

class Centroide(object):
    def __init__(self, nome):
        self.nome = nome
        self.posicao = [0,0]

    def gera_posicao_aleatoria(self, bd):
        posicao_aleatoria = np.random.randint(0, bd.numero_bairros)
        bairros = list(bd.bairros)
        posicao_centroide = bd.bairros[bairros[posicao_aleatoria]]['coordenadas']
        self.posicao = posicao_centroide



