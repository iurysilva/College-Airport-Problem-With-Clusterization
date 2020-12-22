from Objetos import Kmeans, BancoDeDados
from Animacoes import rodar_animacao_2d

movimento_minimo = 0.00001
iteracoes = 1000
velocidade_animacao = 20 #milissegundos
clusters = 4

banco = BancoDeDados()
kmeans = Kmeans(clusters, iteracoes, movimento_minimo, banco)
kmeans.gera_posicoes_aleatorias()

rodar_animacao_2d(kmeans, velocidade_animacao)
