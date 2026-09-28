def bubbleSort(lista, chave=None, reverso=False):

    dados = lista.copy()
    n = len(dados)

    def valor(item):
        return item[chave] if chave else item

    for i in range(n - 1):
        trocou = False
        for j in range(n - 1 - i):
            a = valor(dados[j])
            b = valor(dados[j + 1])
            deveTrocar = a > b if not reverso else a < b
            if deveTrocar:
                dados[j], dados[j + 1] = dados[j + 1], dados[j]
                trocou = True
        if not trocou:
            break

    return dados


if __name__ == '__main__':
    numeros = [5, 2, 8, 1, 9, 3]
    print(bubbleSort(numeros))

    pessoas = [{'nome': 'Ana', 'idade': 30}, {'nome': 'Bia', 'idade': 22}]
    print(bubbleSort(pessoas, chave='idade'))
