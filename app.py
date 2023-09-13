# Importar bibliotecas para trabalhar com dados em Python

import pandas as pd
import matplotlib.pyplot as plt

# Definir uma variável df(Dataframe) onde o pandas lê o arquivo

df = pd.read_csv('Global Population Trends(2016-2022).csv')

# Definir quais dados vamos transformar

Dados_Brasil = df.query("Country == 'Brazil'")

#Fazer o carregamento dos dados(no caso vamos extrair esses dados para vizualizarmos em um arquivo .xlsx no Excel)

Dados_Brasil.to_excel('Dados_Brasil_2016-2022.xlsx')

#Para finalizar nosso ETL

print('Pipeline ETL concluído')