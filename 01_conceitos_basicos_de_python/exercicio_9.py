""9)Solicite ao usuário o número de horas de exercício físico por semana.
Calcule o total de calorias queimadas em um mês, considerando uma
média de 5 calorias por minuto de exercício.""

horas_semana = int(input("Digite o número de horas de exercício físico por semana: "))
if horas_semana < 0:
    print('O valor deve ser maior que zero!')
else:
    semanas_mes = int(input("Digite o número de semanas em um mês: "))
    
    if semanas_mes <= 0:
        print('O número de semanas deve ser maior que zero!')
    else:
        minutos = horas_semana * 60
        # Calcula o total de calorias queimadas em um mês
        calorias_mes = minutos * 5 * semanas_mes
        print("O total de calorias queimadas em um mês é:", calorias_mes)
