import pandas as pd
from scipy.stats import levene

# Amostra A
variaveis = ["Var. X", "Var. Y", "Var. Z", "Var. W"]
amostraA = [
    [7.00, 3.20, 4.70, 1.40],
    [6.40, 3.20, 4.50, 1.50],
    [6.90, 3.10, 4.90, 1.50],
    [5.50, 2.30, 4.00, 1.30],
    [6.50, 2.80, 4.60, 1.50],
    [5.70, 2.80, 4.50, 1.30],
    [6.30, 3.30, 4.70, 1.60],
    [4.90, 2.40, 3.30, 1.00],
    [6.60, 2.90, 4.60, 1.30],
    [5.20, 2.70, 3.90, 1.40],
    [5.00, 2.00, 3.50, 1.00],
]
dfA = pd.DataFrame(amostraA, columns=variaveis)

# Amostra B
amostraB = [
    [6.30, 3.30, 6.00, 2.50],
    [5.80, 2.70, 5.10, 1.90],
    [7.10, 3.00, 5.90, 2.10],
    [6.30, 2.90, 5.60, 1.80],
    [6.50, 3.00, 5.80, 2.20],
    [7.60, 3.00, 6.60, 2.10],
    [4.90, 2.50, 4.50, 1.70],
    [7.30, 2.90, 6.30, 1.80],
    [6.70, 2.50, 5.80, 1.80],
    [7.20, 3.60, 6.10, 2.50],
    [6.50, 3.20, 5.10, 2.00],
    [6.40, 2.70, 5.30, 1.90],
    [6.80, 3.00, 5.50, 2.10],
    [5.70, 2.50, 5.00, 2.00],
    [5.80, 2.80, 5.10, 2.40],
    [6.40, 3.20, 5.30, 2.30],
    [6.50, 3.00, 5.50, 1.80],
    [7.70, 3.80, 6.70, 2.20],
    [7.70, 2.60, 6.90, 2.30],
    [6.00, 2.20, 5.00, 1.50],
    [6.90, 3.20, 5.70, 2.30],
]
dfB = pd.DataFrame(amostraB, columns=variaveis)

# Separando as variáveis de interesse (Var. Y e Var. W)
varYA = dfA["Var. Y"]
varYB = dfB["Var. Y"]

varWA = dfA["Var. W"]
varWB = dfB["Var. W"]

# Teste de Levene para Var. Y
stat_y, p_value_y = levene(varYA, varYB)
print(f"Teste de Levene para Var. Y: estatística={stat_y:.4f}, p-valor={p_value_y:.4f}")

# Teste de Levene para Var. W
stat_w, p_value_w = levene(varWA, varWB)
print(f"Teste de Levene para Var. W: estatística={stat_w:.4f}, p-valor={p_value_w:.4f}")

# Interpretação do resultado
significance_level = 0.10
if p_value_y > significance_level:
    print("Não rejeitamos a hipótese nula: as variâncias de Var. Y são iguais.")
else:
    print("Rejeitamos a hipótese nula: as variâncias de Var. Y são diferentes.")

if p_value_w > significance_level:
    print("Não rejeitamos a hipótese nula: as variâncias de Var. W são iguais.")
else:
    print("Rejeitamos a hipótese nula: as variâncias de Var. W são diferentes.")

