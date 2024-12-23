# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
mes = 30

# Realizei algumas alterações da proposta original, ao invéz das horas trabalhadas no mês,
# pedi as horas trabalhadas por dia
valor_hora = float(input('Digite quanto você ganha por hora: '))
horas_trabalhadas = float(input('Digite quantas horas você trabalha por dia: '))
salario_dia = valor_hora * horas_trabalhadas
salario = salario_dia * mes
print('O total do seu salário no dia é: ', salario_dia, 'R$')
print('O total do seu salário no mês é: ', salario, 'R$')
print('importantr: Estamos trabalhando numa idÉia que que o mes seja 30 dias, o resultado pode não ser o esperado')
