import random

dados_aleatorios = df.to_dict("records")

random.shuffle(dados_aleatorios)

print("Planilha após embaralhamento aleatório:")
display(pd.DataFrame(dados_aleatorios).head())