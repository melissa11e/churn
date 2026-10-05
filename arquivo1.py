import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import numpy as np

df= pd.read_csv(r"C:\Users\nmeli\Downloads\archive\Telco_customer_churn.csv")
# print(df.shape) - colunas e linhas
#print(df.info)
#print(df.isnull()) - mostra todas as colunas e diz
#print(df.isnull().sum()) #soma tudo que é null
#print(df.dtypes)
df['Total Charges'] = df['Total Charges'].replace(" ", '0') #substitui os campos vazios em texto por 0.
df['Total Charges'] = df['Total Charges'].astype('float') # muda o tipo para float.
print(df.dtypes)

print(df.describe()) #mostra os principais cálculos com variáveis quantitativas
print(df.describe())