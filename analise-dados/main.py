import pandas as pd

table = pd.read_csv(r'./analise-dados/database/clientes.csv', encoding="latin1")
# Sempre tratar os dados
# Excluir ou Corrigir Células vazias
# Excluir colunas inúteis

print(table)