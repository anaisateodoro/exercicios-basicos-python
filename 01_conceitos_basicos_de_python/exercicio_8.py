""8)Faça um Programa que pergunte quanto você ganha por hora e o
número de horas trabalhadas no mês.Calcule e mostre o total do seu
salário no referido mês.""

valor_hora = float(input('Informe quanto você ganha por hora: '))
numero_horas = int(input('Informe o número de horas trabalhada no mês: '))
salario = valor_hora * numero_horas
print(f'Total do seu salário no referido mês é: R${salario:.2f}')