import statistics
import math
import matplotlib.pyplot as plt

def calcular_incertezas(dados, incertezas_tipo_B):
    media = statistics.mean(dados)
    desvio_padrao = statistics.stdev(dados)
    incerteza_A = desvio_padrao / math.sqrt(len(dados))
    incerteza_C = math.sqrt(incerteza_A**2 + sum(incertezas_tipo_B)**2)
    incerteza_relativa_percentual = round((incerteza_C / media) * 100, 2)

    return media, desvio_padrao, incerteza_A, incerteza_C, incerteza_relativa_percentual

def exibir_resultados(prefixo, media, desvio_padrao, incerteza_A, incerteza_tipo_B, incerteza_C, incerteza_relativa_percentual):
    print(f"{prefixo}Média: {media}")
    print(f"{prefixo}Desvio Padrão: {desvio_padrao}")
    print(f"{prefixo}Incerteza Tipo A: {incerteza_A}")
    print(f"{prefixo}Incerteza Tipo B: {incerteza_tipo_B}")
    print(f"{prefixo}Incerteza Tipo C: {incerteza_C}")
    print(f"{prefixo}Incerteza Relativa (%): {incerteza_relativa_percentual:.2f}%\n")

# Dados
dados_regua = [25.0, 25.1, 25.0, 25.1, 25.2]
dados_paquimetro_1 = [24.7, 24.85, 24.7, 24.7, 24.75]
dados_paquimetro_2=[31.75,31.80,31.85,31.80,31.90]
dados_paquimetro_3=[49.65,49.70,49.70,49.69,49.70]
dados_paquimetro_4=[59.45,59.55,59.5,59.75,59.40]
dados_paquimetro_5=[74.95,75.0,74.65,74.85,74.90]
incertezas_tipo_B_regua = [0.5] * len(dados_regua)
incertezas_tipo_B_paquimetro_1 = [0.05] * len(dados_paquimetro_1)

# Calcular incertezas para a régua
media_regua, desvio_padrao_regua, incerteza_A_regua, incerteza_C_regua, incerteza_relativa_regua = calcular_incertezas(dados_regua, incertezas_tipo_B_regua)

# Calcular incertezas para o paquímetro
media_paquimetro_2, desvio_padrao_paquimetro_2, incerteza_A_paquimetro_2, incerteza_C_paquimetro_2, incerteza_relativa_paquimetro_2 = calcular_incertezas(dados_paquimetro_2, incertezas_tipo_B_paquimetro_1)

# Exibir resultados para a régua
exibir_resultados("Régua - ", media_regua, desvio_padrao_regua, incerteza_A_regua, incertezas_tipo_B_regua, incerteza_C_regua, incerteza_relativa_regua)

# Exibir resultados para o paquímetro
exibir_resultados("Paquímetro - ", media_paquimetro_2, desvio_padrao_paquimetro_2, incerteza_A_paquimetro_2, incertezas_tipo_B_paquimetro_1, incerteza_C_paquimetro_2, incerteza_relativa_paquimetro_2)

# Plotando o gráfico tipo scatter para x e y com cores diferentes
plt.scatter(dados_paquimetro_2, dados_regua, label='Paquímetro vs. Régua', color='blue', marker='o')
plt.xlabel('Paquímetro (x)')
plt.ylabel('Régua (y)')
plt.title('Relação entre Paquímetro e Régua')
plt.legend()
plt.show()
