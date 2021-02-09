import pandas as pd

databaseName = "./automacao-processos/database/vendas.xlsx"
tableSell = pd.read_excel(databaseName)

revenuesColumns = tableSell[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
revenuesColumns = revenuesColumns.sort_values(by="Valor Final", ascending=False)

print(revenuesColumns)