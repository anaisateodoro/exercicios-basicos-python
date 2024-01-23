def classificar_idade():
    while True:
        idade = int(input("Digite sua idade: "))

        if idade <= 12:
            print("Você é uma criança.")
        elif 13 <= idade <= 17:
            print("Você é um adolescente.")
        elif 18 <= idade <= 65:
            print("Você é um adulto.")
        else:
            print("Você é um idoso.")

classificar_idade()