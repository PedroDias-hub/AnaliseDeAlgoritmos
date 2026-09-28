import time


def selection_sort(dados, coluna):

    dados = dados.copy()

    for i in range(len(dados) - 1):

        menor = i

        for j in range(i + 1, len(dados)):

            if dados[j][coluna] < dados[menor][coluna]:
                menor = j

        dados[i], dados[menor] = dados[menor], dados[i]

    return dados


inicio = time.perf_counter()

resultado_inverso = selection_sort(dados, coluna)

fim = time.perf_counter()

tempo_inverso = fim - inicio


inicio = time.perf_counter()

resultado_aleatorio = selection_sort(dados_aleatorios, coluna)

fim = time.perf_counter()

tempo_aleatorio = fim - inicio


resultados.append([
    "Selection Sort",
    tempo_inverso,
    tempo_aleatorio
])


diferenca = tempo_inverso - tempo_aleatorio


print("SELECTION SORT")
print()

print(
    f"Simulação 1 - Inversamente ordenada: "
    f"{tempo_inverso:.2e} segundos"
)

print(
    f"Simulação 2 - Aleatória:              "
    f"{tempo_aleatorio:.2e} segundos"
)

print()

print(
    f"Diferença entre os tempos: "
    f"{abs(diferenca):.2e} segundos"
)


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

    print(
        "O algoritmo apresentou o mesmo tempo nas duas situações."
    )