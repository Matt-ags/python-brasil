# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

semana_trabalhos = int(input('Digite quantos dias você trabalha por semana?: '))
mes = semana_trabalhos * 4

# Realizei algumas alterações da proposta original, ao invéz das horas trabalhadas no mês,
# pedi as horas trabalhadas por dia

valor_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = float(input('Digite quantas horas você trabalha por dia: '))
salario_dia = valor_hora * horas_trabalhadas
salario = salario_dia * mes
print('Você trabalha ', semana_trabalhos, 'dias por semana e ', mes, 'dias por mês')
print('O total do seu salário no dia é: ', salario_dia, 'R$')
print('O total do seu salário no mês é: ', salario, 'R$')
