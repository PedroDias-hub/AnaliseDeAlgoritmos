dados = df.sort_values(
    by=coluna,
    ascending=False
).to_dict("records")

print("Planilha após ordenação decrescente (PIOR CASO - TROCA DE TODOS OS ELEMENTOS):")
display(pd.DataFrame(dados).head())