import pandas as pd
import plotly.express as px
import plotly.io as pio
pio.renderers.default = "iframe"

# IMPORT TABLE
# DROPING USELESS COLUMN
table = pd.read_csv(r'./analise-dados/database/clientes.csv', encoding="latin1")
table = table.drop("CLIENTNUM", axis=1) #axis = 0: Linha / axis = 1: Coluna

# DATA PROCESSING
table = table.dropna() # Delete null rows
# infoTable = table.info() # Overview of table
overview = table.describe() # Describe all of the base

# ANALYZE
caregoryTable = table["Categoria"].value_counts(normalize=True).mul(100).round(1).astype(str) + '%' 
    # normalize=True: Mostra os valores em procentagem
    # mul(100): Multiplica por 100
    # round(1): Arredonda em uma casa decimal
    # astyoe(str): Converte em string
    # +: Concatena com '%'

# GRAPHIC
    #MAKE A GRAPHIC
columns = []
for column in table:
    columns.append(column)

def makeGraph(index):
    fig = px.histogram(table, x=index, color="Categoria")
    fig.show()

makeGraph(columns[13])