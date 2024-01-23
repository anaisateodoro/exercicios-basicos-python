"""Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0."""

media_alunos = [0, 0, 0, 0, 0]

# Solicitar as notas dos alunos e calcular as médias
for i in range(5):
    nota1 = float(input('Digite a primeira nota do aluno {}: '.format(i+1)))
    nota2 = float(input('Digite a segunda nota do aluno {}: '.format(i+1)))
    nota3 = float(input('Digite a terceira nota do aluno {}: '.format(i+1)))
    nota4 = float(input('Digite a quarta nota do aluno {}: '.format(i+1)))
    
    media_alunos[i] = (nota1 + nota2 + nota3 + nota4) / 4

# Contar números de alunos com média >= 7.0
contador = 0
for i in range(5):
    if media_alunos[i] >= 7.0:
        contador += 1

print('Número de alunos com média maior ou igual a 7.0: ', contador)
