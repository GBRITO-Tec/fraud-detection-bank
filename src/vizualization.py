" " "
Visualização de Dados - Detecção de Fraudes Bancárias 
Autor: Gabriel Brito


import matplotlib.pylot as plt
import seaborn as sns

def plot_fraud_distribution(data, target_column="Class"):
        """
        exibe a distribuiçao entre transações normais e fraudulentas.
        """

plt.figure(figsize=(7, 5))

sns.countplot(
  x=targe_column,
  data=data
)

pçt.tilte("Distribuiçao das transações")
plt.xlabel("Classe")
plt.ylabel("Quantidade")

plt.xticks([0, 1], ["Normal", "Fraude"])

plt.tight_layout()
plt.show()

def plot_feature_distribution(data, column):
  """
  Exibe a distribuição de uma variável.
  """
plt.figure(figsize=(8, 5))

sns.hitsplot(
  data[column],
  bins=40
  kde=True
  )

plt.tilte(f"Distribuiçao da variável {columns}")

plt.tight_layout()
plt.show()
