def insertionSort(lista, chave=None, reverso=False):

    dados = lista.copy()
    n = len(dados)

    def valor(item):
        return item[chave] if chave else item

    for i in range(1, n):
        atual = dados[i]
        j = i - 1

        while j >= 0:
            if not reverso:
                deveMover = valor(dados[j]) > valor(atual)
            else:
                deveMover = valor(dados[j]) < valor(atual)

            if not deveMover:
                break

            dados[j + 1] = dados[j]
            j -= 1

        dados[j + 1] = atual

    return dados


if __name__ == '__main__':
    numeros = [5, 2, 8, 1, 9, 3]
    print(insertionSort(numeros))

    pessoas = [
        {'nome': 'Ana', 'idade': 30},
        {'nome': 'Bia', 'idade': 22}
    ]

    print(insertionSort(pessoas, chave='idade'))