#Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. Calcule e imprima o consumo médio em km/l.
litros = float(input("Digite a quantidade de litros de combustível consumidos: "))
distancia = float(input("Digite a distância percorrida em km: "))
# Calcular o consumo médio de combustível em km/l
consumo_medio = distancia / litros
print("O consumo médio é {:.2f} km/l".format(consumo_medio))

