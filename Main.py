import pandas as pd


def carregar_dados(caminhoArquivo):

    df = pd.read_csv(
        caminhoArquivo,
        encoding='utf-8-sig'
    )

    coluna = next(
        c for c in df.columns
        if str(c).strip().lower() == "areamunkm"
    )

    return df, coluna


df, coluna = carregar_dados('TabelaCSVComFiltro.csv')

print("Coluna encontrada:", coluna)
print("Quantidade de registros:", len(df))

print("\nVisualização parcial da planilha:")
print(df.head())