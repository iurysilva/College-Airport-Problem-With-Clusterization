from Objetos import Kmeans, Centroide, BancoDeDados
import matplotlib.pyplot as plt

teste = Kmeans(4)
teste.centroides.append(Centroide(teste.numero_centroides))
banco = BancoDeDados()

x0 = []
y0 = []

x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []

xcentroide = []
ycentroide = []
bairros = list(banco.bairros)

for i in range(4):
    teste.centroides[i].gera_posicao_aleatoria(banco)
    xcentroide.append(teste.centroides[i].posicao[0])
    ycentroide.append(teste.centroides[i].posicao[1])

teste.classifica_amostras(banco)
print(teste.centroides[0].bairros)
print(teste.centroides[1].bairros)
print(teste.centroides[2].bairros)
print(teste.centroides[3].bairros)

for bairro in banco.bairros:
    if banco.bairros[bairro]['centroide'] == 0:
        x0.append(banco.bairros[bairro]['coordenadas'][0])
        y0.append(banco.bairros[bairro]['coordenadas'][1])
    elif banco.bairros[bairro]['centroide'] == 1:
        x1.append(banco.bairros[bairro]['coordenadas'][0])
        y1.append(banco.bairros[bairro]['coordenadas'][1])
    elif banco.bairros[bairro]['centroide'] == 2:
        x2.append(banco.bairros[bairro]['coordenadas'][0])
        y2.append(banco.bairros[bairro]['coordenadas'][1])
    elif banco.bairros[bairro]['centroide'] == 3:
        x3.append(banco.bairros[bairro]['coordenadas'][0])
        y3.append(banco.bairros[bairro]['coordenadas'][1])

plt.plot(xcentroide[0], ycentroide[0], 'go', xcentroide[1], ycentroide[1], 'bo', xcentroide[2], ycentroide[2], 'yo', xcentroide[3], ycentroide[3], 'ro', x0, y0,'g^', x1, y1, 'b^',x2, y2, 'y^', x3, y3, 'r^')
plt.show()