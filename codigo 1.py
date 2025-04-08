import pandas as pd
import matplotlib.pyplot as plt  # Importar antes de usar

# Carregar o arquivo Excel
df = pd.read_excel("C:/Users/User/Desktop/PROJETOS/Projeto-PyPandas/Desempenho_Equipe1.xlsx")
print(df.head())

# Contar a frequência de cada nome
print(df["Nome"].value_counts())

# Criar gráfico de pizza
df.groupby("Nome")["Atingido Jan"].sum().plot.pie(
    autopct="%1.1f%%", 
    figsize=(6, 6)
)

# Adicionar título e remover rótulo do eixo Y
plt.title("Desempenho em Janeiro")
plt.ylabel("")

# Exibir gráfico
plt.show()
