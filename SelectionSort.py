def selectionSort(lista, chave=None, reverso=False):

    dados = lista.copy()
    n = len(dados)

    def valor(item):
        return item[chave] if chave else item

    for i in range(n - 1):
        indice = i

        for j in range(i + 1, n):
            if not reverso:
                if valor(dados[j]) < valor(dados[indice]):
                    indice = j
            else:
                if valor(dados[j]) > valor(dados[indice]):
                    indice = j

        dados[i], dados[indice] = dados[indice], dados[i]

    return dados


if __name__ == '__main__':
    numeros = [5, 2, 8, 1, 9, 3]
    print(selectionSort(numeros))

    pessoas = [
        {'nome': 'Ana', 'idade': 30},
        {'nome': 'Bia', 'idade': 22}
    ]

    print(selectionSort(pessoas, chave='idade'))