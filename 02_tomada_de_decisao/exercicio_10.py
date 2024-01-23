def mostrar_em_ordem_crescente():
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    num3 = int(input("Digite o terceiro número inteiro: "))


    #Não sei se podia usar .sort, então fiz assim
    if num1 <= num2 and num1 <= num3:
        menor = num1
        if num2 <= num3:
            meio, maior = num2, num3
        else:
            meio, maior = num3, num2
    elif num2 <= num1 and num2 <= num3:
        menor = num2
        if num1 <= num3:
            meio, maior = num1, num3
        else:
            meio, maior = num3, num1
    else:
        menor = num3
        if num1 <= num2:
            meio, maior = num1, num2
        else:
            meio, maior = num2, num1

    print("Números em ordem crescente:", menor, meio, maior)

mostrar_em_ordem_crescente()