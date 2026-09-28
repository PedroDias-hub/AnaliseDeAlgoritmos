import time


def quick_sort(dados, coluna):

    if len(dados) <= 1:
        return dados.copy()

    pivo = dados[len(dados) // 2][coluna]

    menores = []
    iguais = []
    maiores = []

    for registro in dados:

        if registro[coluna] < pivo:
            menores.append(registro)

        elif registro[coluna] > pivo:
            maiores.append(registro)

        else:
            iguais.append(registro)

    return (
        quick_sort(menores, coluna)
        + iguais
        + quick_sort(maiores, coluna)
    )


inicio = time.perf_counter()

resultado_inverso = quick_sort(dados, coluna)

fim = time.perf_counter()

tempo_inverso = fim - inicio


inicio = time.perf_counter()

resultado_aleatorio = quick_sort(dados_aleatorios, coluna)

fim = time.perf_counter()

tempo_aleatorio = fim - inicio


resultados.append([
    "Quick Sort",
    tempo_inverso,
    tempo_aleatorio
])


diferenca = tempo_inverso - tempo_aleatorio


print("QUICK SORT")
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