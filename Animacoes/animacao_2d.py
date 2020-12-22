import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

plot2d = 0
anim = 0
kmeans = 0

def animacao_2d(frame):
    global plot2d, anim, kmeans
    kmeans.classifica_amostras()
    for removendo in plot2d:
        removendo.remove()
    plt.xlim(-48.52, -48.38)
    plt.ylim(-1.5, -1.3)
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

    for centroide in range(kmeans.numero_centroides):
        xcentroide.append(kmeans.centroides[centroide].posicao[1])
        ycentroide.append(kmeans.centroides[centroide].posicao[0])

    for bairro in kmeans.banco.bairros:
        if kmeans.banco.bairros[bairro]['centroide'] == 0:
            x0.append(kmeans.banco.bairros[bairro]['coordenadas'][1])
            y0.append(kmeans.banco.bairros[bairro]['coordenadas'][0])
        elif kmeans.banco.bairros[bairro]['centroide'] == 1:
            x1.append(kmeans.banco.bairros[bairro]['coordenadas'][1])
            y1.append(kmeans.banco.bairros[bairro]['coordenadas'][0])
        elif kmeans.banco.bairros[bairro]['centroide'] == 2:
            x2.append(kmeans.banco.bairros[bairro]['coordenadas'][1])
            y2.append(kmeans.banco.bairros[bairro]['coordenadas'][0])
        elif kmeans.banco.bairros[bairro]['centroide'] == 3:
            x3.append(kmeans.banco.bairros[bairro]['coordenadas'][1])
            y3.append(kmeans.banco.bairros[bairro]['coordenadas'][0])
    plot2d = plt.plot(xcentroide[0], ycentroide[0], 'go', xcentroide[1], ycentroide[1], 'bo', xcentroide[2], ycentroide[2], 'yo', xcentroide[3], ycentroide[3], 'ro', x0, y0, 'g^', x1, y1, 'b^', x2, y2, 'y^', x3, y3, 'r^')
    kmeans.iteracoes -= 1
    plt.title('iteracoes faltando: %d' % (kmeans.iteracoes + 1))
    kmeans.move_centroides()
    if kmeans.iteracoes == -1 or not kmeans.houve_movimentacao:
        kmeans.calcula_distancia_total()
        print(kmeans.distancia_total)
        anim.event_source.stop()


def rodar_animacao_2d(kmeans2, velocidade_animacao):
    global anim, kmeans, plot2d
    kmeans = kmeans2
    plot2d = plt.plot(0, 0)
    print("Initializing with 2D animation")
    anim = FuncAnimation(plt.gcf(), animacao_2d, interval=velocidade_animacao, repeat=False)
    plt.show()

