import pandas as pd 
 
def pesquisarDados(caminhoArquivo, ColunaFiltro, valorFiltro):
    
    carregarDados = pd.read_csv(caminhoArquivo, dtype=str)
    
    
    linhasFiltradas = carregarDados[
        carregarDados[ColunaFiltro].str.strip().str.lower() == str(valorFiltro).strip().lower()
    ]
    
    return linhasFiltradas
    print(pesquisarDados('TabelaCSVComFiltro.csv', 'municipio', 'Juara'))


