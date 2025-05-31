import numpy as np
import matplotlib.pyplot as plt

# ESTA FUNÇÃO PADRONIZA OS VALORES DE UMA LISTA
def padronizar(lista: list):
    media = np.mean(lista)
    desvio_padrao = np.std(lista)
    lista_padronizada = [(num-media)/desvio_padrao for num in lista]
    return lista_padronizada

def plot_serie_temporal_padronizado(lista_x, lista_y_1, nome_1, titulo_grafico, grafico_largura, grafico_altura, lista_y_2: list = None, nome_2: str = None):
    if lista_y_2 is None:
        fig, ax = plt.subplots(figsize = (grafico_largura, grafico_altura))
        lista_y_1 = padronizar(lista_y_1)
        ax.plot(lista_x, lista_y_1, label = nome_1)
        ax.set_title(titulo_grafico)
        ax.legend()
        return plt.show()
    else:
        fig, ax = plt.subplots(figsize = (grafico_largura, grafico_altura))
        lista_y_1 = padronizar(lista_y_1)
        lista_y_2 = padronizar(lista_y_2)
        ax.plot(lista_x, lista_y_1, label = nome_1)
        ax.plot(lista_x, lista_y_2, label = nome_2)
        ax.set_title(titulo_grafico)
        ax.legend()
        return plt.show()