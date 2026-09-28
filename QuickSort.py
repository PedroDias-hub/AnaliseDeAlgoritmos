def quickSort(lista, chave=None, reverso=False):

    dados = lista.copy()

    def valor(item):
        return item[chave] if chave else item

    def ordenar(esquerda, direita):

        if esquerda >= direita:
            return

        pivo = valor(dados[direita])
        indice = esquerda

        for i in range(esquerda, direita):

            if not reverso:
                deveTrocar = valor(dados[i]) <= pivo
            else:
                deveTrocar = valor(dados[i]) >= pivo

            if deveTrocar:
                dados[indice], dados[i] = dados[i], dados[indice]
                indice += 1

        dados[indice], dados[direita] = dados[direita], dados[indice]

        ordenar(esquerda, indice - 1)
        ordenar(indice + 1, direita)

    ordenar(0, len(dados) - 1)

    return dados


if __name__ == '__main__':
    numeros = [5, 2, 8, 1, 9, 3]
    print(quickSort(numeros))

    pessoas = [
        {'nome': 'Ana', 'idade': 30},
        {'nome': 'Bia', 'idade': 22}
    ]

    print(quickSort(pessoas, chave='idade'))