#Reverso do número. Faça uma função que retorne o reverso de um
#número inteiro informado. Por exemplo: 127 -> 721.

def reverse(num):
    try:
        num = int(num)
        return str(num)[::-1]
    except ValueError:
        return "Entrada inválida. Por favor, digite um número."

numero = input("Digite um número: ")
resultado = reverse(numero)
print(f'O número invertido fica assim: {resultado}')
