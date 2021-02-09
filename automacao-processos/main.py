import pandas as pd

databaseName = "./automacao-processos/database/vendas.xlsx"
tableSell = pd.read_excel(databaseName)

revenuesColumns = tableSell[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()
revenuesColumns = revenuesColumns.sort_values(by="Valor Final", ascending=False)

amountColumns = tableSell[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()
amountColumns = amountColumns.sort_values(by="Quantidade", ascending=False)

ticketMiddle = revenuesColumns["Valor Final"] / amountColumns["Quantidade"]
ticketMiddle = ticketMiddle.to_frame()
print(ticketMiddle)

