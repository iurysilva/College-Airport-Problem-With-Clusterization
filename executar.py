from Objetos import Kmeans, BancoDeDados
from Animacoes import rodar_animacao_2d


iteracoes = 10
velocidade_animacao = 2000 #milissegundos
clusters = 4

banco = BancoDeDados()
kmeans = Kmeans(clusters, iteracoes, banco)
kmeans.gera_posicoes_aleatorias()

rodar_animacao_2d(kmeans, velocidade_animacao)
