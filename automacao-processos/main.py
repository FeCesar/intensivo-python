import pandas as pd

databaseName = "./automacao-processos/database/vendas.xlsx"
tableSell = pd.read_excel(databaseName)

print(tableSell)