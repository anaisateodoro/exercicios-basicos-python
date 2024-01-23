#1. Faça um Programa que peça dois números e imprima o maior deles.
def imprimir_maior_numero():
    
    while True:
    
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    
        if num1 > num2:
            print(f"O maior número é: {int(num1)}")
        elif num2 > num1:
            print(f"O maior número é: {int(num2)}")
        else:
            print("Os números são iguais.")


imprimir_maior_numero()