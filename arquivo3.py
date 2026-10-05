import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\nmeli\Downloads\archive\Telco_customer_churn.csv")
df['Total Charges'] = df['Total Charges'].replace(" ", '0') #substitui os valores vazios dessa coluna por 0
df['Total Charges'] = df['Total Charges'].astype(float) #converte a coluna para float.

df["Churn_1_Month"] = np.where(
    (df["Tenure Months"] <= 1) & (df["Churn Label"] == "Yes"),
    "Yes",
    "No"
)
colunas = [
    ""
    "Phone Service",
    "Multiple Lines",
    "Internet Service",
    "Online Security",
    "Online Backup",
    "Device Protection",
    "Tech Support",
    "Streaming TV",
    "Streaming Movies",
    "Contract",
    "Paperless Billing",
    "Payment Method",
    "Churn Reason"
]

for coluna in colunas:

    print("\n==============================")
    print(coluna)
    print("==============================")

    tabela = pd.crosstab(
        df[coluna],
        df["Churn_1_Month"],
        normalize="index"
    ) * 100

    print(tabela.round(2))


axReason = sns.countplot(
    y="Churn Reason",
    data=df,
    hue="Churn_1_Month"
)
plt.title("Churn por motivo")

for bars in axReason.containers:
    axReason.bar_label(bars)

plt.tight_layout()
plt.show()

axContract = sns.countplot(x="Contract",data=df, hue="Churn_1_Month")
plt.title("Churn em até 1 mês por tipo de contrato")
for bars in axContract.containers:
    axContract.bar_label(bars)
plt.show()

axGender = sns.countplot(x="Gender",data=df, hue="Churn_1_Month")
for bars in axGender.containers:
    axGender.bar_label(bars)
plt.title("Churn em até 1 mês por gênero")
plt.show()

axSenior = sns.countplot(x="Senior Citizen",data=df, hue="Churn_1_Month")
for bars in axSenior.containers:
    axSenior.bar_label(bars)
plt.xticks([0, 1], ['Jovens', 'Idosos'])
plt.title("Churn em até 1 mês por faixa etária")
plt.show()

axDependents = sns.countplot(x="Dependents",data=df, hue="Churn_1_Month")
for bars in axDependents.containers:
    axDependents.bar_label(bars)
plt.title("Churn em até 1 mês por dependentes ")
plt.show()


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

# Divide as colunas em grupos de 3
grupos = [
    colunas[0:3],
    colunas[3:6],
    colunas[6:9]
]

for grupo in grupos:

    fig, axes = plt.subplots(
        3, 1,
        figsize=(12, 12)
    )

    for ax, coluna in zip(axes, grupo):

        sns.countplot(
            x=coluna,
            data=df,
            hue="Churn_1_Month",
            ax=ax
        )

        # Coloca os números em cima das barras
        for bars in ax.containers:
            ax.bar_label(bars, fontsize=9)

        ax.set_title(coluna, fontsize=14)
        ax.set_xlabel("")
        ax.set_ylabel("Quantidade")

    plt.tight_layout()
    plt.show()

axPayment = sns.countplot(x="Payment Method",data=df, hue="Churn_1_Month")
plt.title("Churn em até 1 mês por tipo de contrato")
for bars in axPayment.containers:
    axPayment.bar_label(bars)
plt.show()

axReason = sns.countplot(
    y="Churn Reason",
    data=df,
    hue="Churn_1_Month"
)

plt.title("Churn por motivo")

for bars in axReason.containers:
    axReason.bar_label(bars)

plt.tight_layout()
plt.show()