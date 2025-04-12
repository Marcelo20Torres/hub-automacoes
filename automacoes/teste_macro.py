import pandas as pd

def executar(args=None):

    caminho_arquivo = 'dados/Teste M.xlsx'
    arquivo_saida = 'dados/Teste.txt'

    df = pd.read_excel(caminho_arquivo)

    df_filtrado = df[df['Status'] != 'Não pago']

    soma_por_nome = df_filtrado.groupby('Nome', as_index=False)['Valor'].sum()
    soma_por_nome.columns = ['Nome', 'Total Valor']  

    
    with open(arquivo_saida, 'w', encoding='utf-8') as f:
        f.write("### DADOS PAGOS ###\n")
        df_filtrado.to_csv(f, sep='\t', index=False)
        
        f.write("\n### TOTAIS POR NOME ###\n")
        soma_por_nome.to_csv(f, sep='\t', index=False)

    return f"Relatorio de pagamentos gerado em {arquivo_saida}"

