import time

resultados = [
    ["Algoritmo", "Inversamente ordenada", "Aleatória"],
]

def bubble_sort(dados):

    dados = dados.copy()

    for i in range(len(dados) - 1):

        for j in range(len(dados) - 1 - i):

            if dados[j][coluna] > dados[j + 1][coluna]:

                dados[j], dados[j + 1] = dados[j + 1], dados[j]

    return dados


inicio = time.perf_counter()

resultado_inverso = bubble_sort(dados)

fim = time.perf_counter()

tempo_inverso = fim - inicio


inicio = time.perf_counter()

resultado_aleatorio = bubble_sort(dados_aleatorios)

fim = time.perf_counter()

tempo_aleatorio = fim - inicio


resultados.append([
    "Bubble Sort",
    tempo_inverso,
    tempo_aleatorio
])


diferenca = tempo_inverso - tempo_aleatorio


print("BUBBLE SORT")
print()
print(f"Simulação 1 - Inversamente ordenada: {tempo_inverso:.2e} segundos")
print(f"Simulação 2 - Aleatória:              {tempo_aleatorio:.2e} segundos")
print()
print(f"Diferença entre os tempos: {abs(diferenca):.2e} segundos")


if diferenca > 0:

    print(
        f"O algoritmo gastou {diferenca:.2e} segundos a mais "
        f"na situação inversamente ordenada."
    )

elif diferenca < 0:

    print(
        f"O algoritmo gastou {abs(diferenca):.2e} segundos a mais "
        f"na situação aleatória."
    )

else:

    print("O algoritmo apresentou o mesmo tempo nas duas situações.")