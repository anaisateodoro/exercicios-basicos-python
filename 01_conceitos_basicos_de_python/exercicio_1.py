'''1. Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão'''

# Input
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
# Operações aritméticas
#Soma
soma = numero1 + numero2
print("Soma: {:.2f}".format(soma))
#Subtração
subtracao = numero1 - numero2
print("Subtração: {:.2f}".format(subtracao))
#Multiplicação
multiplicacao = numero1 * numero2
print("Multiplicação: {:.2f}".format(multiplicacao))
# Divisão 
if numero2 != 0: # Aqui verificar se o denominador não é zero antes de realizar a divisão
    divisao = numero1 / numero2
    print("Divisão: {:.2f}".format(divisao))
else:
    print("Erro: Divisão por zero não é permitida.")
