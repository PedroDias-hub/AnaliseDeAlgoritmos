import time

def insertion_sort(dados,coluna):

    dados = dados.copy()

    for i in range(1, len(dados)):

        atual = dados[i]

        j = i - 1

        while j >= 0 and dados[j][coluna] > atual[coluna]:

            dados[j + 1] = dados[j]

            j -= 1

        dados[j + 1] = atual

    return dados


inicio = time.perf_counter()

resultado_inverso = insertion_sort(dados)

fim = time.perf_counter()

tempo_inverso = fim - inicio


inicio = time.perf_counter()

resultado_aleatorio = insertion_sort(dados_aleatorios)

fim = time.perf_counter()

tempo_aleatorio = fim - inicio

resultados = []

resultados.append([
    "Insertion Sort",
    tempo_inverso,
    tempo_aleatorio
])


diferenca = tempo_inverso - tempo_aleatorio


print("INSERTION SORT")
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