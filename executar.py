from Objetos import Kmeans, BancoDeDados

banco = BancoDeDados()
teste = Kmeans(4, banco)
teste.gera_posicoes_aleatorias()

teste.classifica_amostras()
print(teste.centroides[0].bairros)
print(teste.centroides[1].bairros)
print(teste.centroides[2].bairros)
print(teste.centroides[3].bairros)

teste.plota_mapa()
