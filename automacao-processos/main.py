import pandas as pd

databaseName = "database/Vendas.xlsx"
tabela = pd.read_excel(databaseName)

print(tabela)