def pedir_nota():
    while True:
        nota = input("Digite uma nota entre zero e dez: ")

        if nota.replace('.', '', 1).isdigit():
            nota = float(nota)
            if 0 <= nota <= 10:
                print(f"Nota válida: {nota}")
                break
            else:
                print("Valor inválido. A nota deve estar entre zero e dez.")
        else:
            print("Valor inválido. Por favor, digite um número.")

pedir_nota()