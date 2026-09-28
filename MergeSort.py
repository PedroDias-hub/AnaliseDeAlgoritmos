def mergeSort(lista, chave=None, reverso=False):

    def valor(item):
        return item[chave] if chave else item

    def merge(esquerda, direita):
        resultado = []

        i = 0
        j = 0

        while i < len(esquerda) and j < len(direita):

            if not reverso:
                if valor(esquerda[i]) <= valor(direita[j]):
                    resultado.append(esquerda[i])
                    i += 1
                else:
                    resultado.append(direita[j])
                    j += 1

            else:
                if valor(esquerda[i]) >= valor(direita[j]):
                    resultado.append(esquerda[i])
                    i += 1
                else:
                    resultado.append(direita[j])
                    j += 1

        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])

        return resultado

    def ordenar(dados):

        if len(dados) <= 1:
            return dados

        meio = len(dados) // 2

        esquerda = ordenar(dados[:meio])
        direita = ordenar(dados[meio:])

        return merge(esquerda, direita)

    return ordenar(lista.copy())


if __name__ == '__main__':
    numeros = [5, 2, 8, 1, 9, 3]
    print(mergeSort(numeros))

    pessoas = [
        {'nome': 'Ana', 'idade': 30},
        {'nome': 'Bia', 'idade': 22}
    ]

    print(mergeSort(pessoas, chave='idade'))