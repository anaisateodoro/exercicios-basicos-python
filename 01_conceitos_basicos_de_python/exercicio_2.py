# 2- Peça ao usuário para informar o ano de nascimento.Em seguida, calcule e imprima a idade atual.
ano_atual = 2024
ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - ano_nascimento
if ano_atual < ano_nascimento:
   idade -= 1
print("Você tem {} anos.".format(idade))

