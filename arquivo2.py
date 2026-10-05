import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\nmeli\Downloads\archive\Telco_customer_churn.csv")
#print(df.shape) # Mostra as linhas e colunas.
#print(df.info) # Mostra informações sobre o DataFrame, como o número de entradas, colunas, tipos de dados e valores nulos.
#print(df.isnull()) #motra se as linhas estão vazias ou preenchidas com valores nulos.
#print(df.isnull().sum()) # Mostra a quantidade de valores nulos em cada coluna.   
df['Total Charges'] = df['Total Charges'].replace(" ", '0') #substitui os valores vazios dessa coluna por 0
df['Total Charges'] = df['Total Charges'].astype(float) #converte a coluna para float.
#print(df.describe()) # mostra cálculos numéricos das colunas (média, desvio padrão, mínimo, máximo, quartis, etc.)
#print(df.describe(include='object')) # mostra cálculos numéricos das colunas categóricas (count:nulos, unique:valores diferentes, top:o que mais aparece, freq: Quantidade do que mais aparece)

#def conv(value):
    #if value == 1:
        #return 'yes'
    #else:
        #return 'no'

# essa função pega o valor na coluna senior citizen e armazena em conv, para depois aplica a função e mudar o nome.

#df['Senior Citizen'] = df['Senior Citizen'].apply(conv) #converte a coluna Senior Citizen para yes ou no (mas no meu caso já estava)

# ----> GRÁFICO DE BARRAS
axChurn=sns.countplot(x="Churn Label", data=df) #armazena em ax os valores contados da variavel Churn Label, do df.
axChurn.bar_label(axChurn.containers[0]) #cria as barras do gráfico com os valores contados.
plt.show() #exibe

# ----> GRÁFICO DE PIZZA COM   GROUPYBY
#Essa forma de agrupar os valores usa groupby.agg()
#   gb=df.groupby('Churn Label').agg({'Churn Label':"count"})
#   plt.pie(gb['Churn Label'],labels = gb.index, autopct="%1.2f%%")


#GRÁFICO DE PIZZA
# ---->> essa forma de agrupar usa o .value_counts() para armazenar. Esse é melhor.
gb = df['Churn Label'].value_counts() #esse e o anterior fazema mesma coisa. Ele
#   print(gb)
plt.pie(gb,labels = gb.index, autopct="%1.2f%%")
#   plt.title("Contagem de Customer Churn")
plt.show()



#GÊNERO
#    GRÁFICO DE BARRAS MAS N ENUMERA AS COLUNAS DIREITO
axGender=sns.countplot(x="Gender", data=df) #armazena em ax os valores contados da variavel Gender, do df.
axGender.bar_label(axGender.containers[0])
plt.title("Quantidade de homens e mulheres")
plt.show()

#    GRÁFICO DE BARRAS QUE ENUMERA AS COLUNAS DIREITO
## Separa o churn em sim/não por gênero, mas só dá nome a uma das barras.
axGender=sns.countplot(x="Gender", data=df, hue="Churn Label") # o hue separa uma vriável 
axGender.bar_label(axGender.containers[0])
for bars in axGender.containers:
    axGender.bar_label(bars)
plt.title('Saída/permanencia por Gênero')
plt.show()


## JOVENS E IDOSOS
axSenior=sns.countplot(x="Senior Citizen", data=df) #armazena em ax os valores contados da variavel Gender, do df.
axSenior.bar_label(axSenior.containers[0])
plt.xticks([0, 1], ['Jovens', 'Idosos'])
plt.title("Quantidade de jovens e idosos")
plt.show()

axSenior=sns.countplot(x="Senior Citizen", data=df, hue="Churn Label")
for bars in axSenior.containers:
    axSenior.bar_label(bars)
plt.xticks([0, 1], ['Jovens', 'Idosos'])
plt.title("Saída/permanência por grupo etário")
plt.show()

## DEPENDENTES
axDependents=sns.countplot(x="Dependents", data=df) #armazena em ax os valores contados da variavel Gender, do df.
axDependents.bar_label(axDependents.containers[0])
plt.title("Quantidade de pessoas com ou sem dependentes")
plt.show()

axDependents=sns.countplot(x="Dependents", data=df, hue="Churn Label")
for bars in axDependents.containers:
    axDependents.bar_label(bars)
plt.xticks([0, 1], ['Sem Dependentes', 'Com dependentes'])
plt.title("Saída/permanência por dependentes")
plt.show()

# PERCEIROS
axPartner=sns.countplot(x="Partner", data=df) #armazena em ax os valores contados da variavel Gender, do df.
axPartner.bar_label(axPartner.containers[0])
plt.title("Quantidade de pessoas com parceiros")
plt.show()

## TEMPO DE PERMANENCIA
# TENURE — TEMPO DE PERMANÊNCIA

# Cria as faixas de meses
bins = [0, 5, 12, 24, 36, 48, 60, 72]
labels = ['0–5', '6–12', '13–24', '25–36', '37–48', '49–60', '61–72']

df['Tenure Faixa'] = pd.cut(
    df['Tenure Months'],
    bins=bins,
    labels=labels,
    include_lowest=True
)

# Gráfico
axTenure = sns.countplot(
    x='Tenure Faixa',
    data=df,
    hue='Churn Label'
)

# Coloca os valores em cima das barras
for bars in axTenure.containers:
    axTenure.bar_label(bars)

plt.xlabel('Tempo de permanência (meses)')
plt.ylabel('Quantidade de clientes')
plt.title('Saída/permanência por tempo de contrato')

plt.show()


#TIPO DE CONTRATO
axContract=sns.countplot(x="Contract", data=df)
for bars in axContract.containers:
    axContract.bar_label(bars)
plt.title("Tipos de contrato")
plt.show()

axContract=sns.countplot(x="Contract", data=df, hue="Churn Label")
for bars in axContract.containers:
    axContract.bar_label(bars)
plt.title("Saída/permanência por tipo de contrato")
plt.show()


print(df.columns)

#  AGORA AS COLUNAS DE SERVIÇOS!!

colunas = [
    "Phone Service",
    "Multiple Lines",
    "Internet Service",
    "Online Security",
    "Online Backup",
    "Device Protection",
    "Tech Support",
    "Streaming TV",
    "Streaming Movies"
]

fig, axes = plt.subplots(3, 3, figsize=(18, 12))

for ax, coluna in zip(axes.flat, colunas):
    sns.countplot(x=coluna, data=df, hue="Churn Label", ax=ax)

    for bars in ax.containers:
        ax.bar_label(bars)

    ax.set_title(coluna)

plt.tight_layout()
plt.show()