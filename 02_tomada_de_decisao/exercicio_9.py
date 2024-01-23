def contar_pares_impares():
    contagem_pares = 0
    contagem_impares = 0

    while True:
        try:
            numero = int(input("Digite um número positivo (ou 0 para encerrar): "))

            if numero == 0:
                break
            elif numero < 0:
                print("Por favor, insira apenas números positivos.")
                continue

            if numero % 2 == 0:
                contagem_pares += 1
            else:
                contagem_impares += 1

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    print(f"Quantidade de números pares: {contagem_pares}")
    print(f"Quantidade de números ímpares: {contagem_impares}")


contar_pares_impares()