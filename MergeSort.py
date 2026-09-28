import time


def merge_sort(dados, coluna):

    if len(dados) <= 1:
        return dados.copy()

    meio = len(dados) // 2

    esquerda = merge_sort(dados[:meio], coluna)
    direita = merge_sort(dados[meio:], coluna)

    resultado = []

    i = 0
    j = 0

    while i < len(esquerda) and j < len(direita):

        if esquerda[i][coluna] <= direita[j][coluna]:
            resultado.append(esquerda[i])
            i += 1

        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado