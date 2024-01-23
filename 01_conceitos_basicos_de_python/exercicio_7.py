""7)Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).""

# Solicitar ao usuário o peso e a altura
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / altura ** 2
print("Seu IMC é: {:.2f}".format(imc))
