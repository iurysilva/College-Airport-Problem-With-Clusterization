import numpy as np

class Centroide:
    def __init__(self, nome, fixo=False):
        self.nome = nome
        self.posicao = [0, 0]
        self.bairros = []
        self.num_bairros = 0
        self.fixo = fixo

    def __repr__(self):
        return '%d' %self.fixo

    def gera_posicao_aleatoria(self, bd):
        posicao_aleatoria = np.random.randint(0, bd.numero_bairros)
        bairros = list(bd.bairros)
        posicao_centroide = bd.bairros[bairros[posicao_aleatoria]]['coordenadas']
        self.posicao = list(posicao_centroide)



