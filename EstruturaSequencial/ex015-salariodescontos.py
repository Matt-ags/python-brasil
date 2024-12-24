# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, 
# faça um programa que nos dê:
# 1. salário bruto.
# 2. quanto pagou ao INSS.
# 3. quanto pagou ao sindicato.
# 4. o salário líquido.
# - calcule os descontos e o salário líquido, conforme a tabela abaixo:
    #   + Salário Bruto : R$
    #   - IR (11%) : R$
    #   - INSS (8%) : R$
    #   - Sindicato ( 5%) : R$
    #   = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

IR = 0.11 # 11% -> IMPOSTO DE RENDA
INSS = 0.08 # 8% -> INSS
SINDICATO = 0.05 # 5% -> SINDICATO

def salario():
    hora_ganho = float(input("Quanto você ganha por hora? "))
    mes_ganho = int(input("Quantas horas você trabalhou no mês? "))
    salario_bruto = hora_ganho * mes_ganho
    ir = salario_bruto * IR
    inss = salario_bruto * INSS
    sindicato = salario_bruto * SINDICATO
    salario_liquido = salario_bruto - ir - inss - sindicato
    print(f"+ Salário Bruto : R$ {salario_bruto}")
    print(f"- IR (11%) : R$ {ir}")
    print(f"- INSS (8%) : R$ {inss}")
    print(f"- Sindicato (5%) : R$ {sindicato}")
    print(f"= Salário Liquido : R$ {salario_liquido}")

# salario()

# Acima é da forma que a proposta pede, mas sendo sincero, não gostei muito,
# então segue uma outra verção, parecido com a antiga (ex008-salario.py):

def salario_novo():
    # Perguntas para elaborar o calculo:
    semana_trabalhos = int(input('Digite quantos dias você trabalha por semana?: '))

    mes = semana_trabalhos * 4 # Este mes é quantos dias ele, usuário, trabalha, não o mês em si

    valor_hora = float(input('Digite quanto você ganha por hora: '))
    horas_trabalhadas = float(input('Digite quantas horas você trabalha por dia: '))

    # Calculos do salário
    salario_dia = valor_hora * horas_trabalhadas
    salario_bruto = salario_dia * mes
    print('Você trabalha ', semana_trabalhos, 'dias por semana e ', mes, 'dias por mês')
    print('O total do seu salário no dia é: ', salario_dia, 'R$')
    print('O total do seu salário no mês é: ', salario_bruto, 'R$')
    print('Descontos:')

    # Calculos dos descontos
    ir = salario_bruto * IR # IMPOSTO DE RENDA
    inss = salario_bruto * INSS # INSS
    sindicato = salario_bruto * SINDICATO # SINDICATO
    salario_liquido = salario_bruto - ir - inss - sindicato # SALÁRIO LÍQUIDO

    print(f"+ Salário Bruto : R$ {salario_bruto}")
    print(f"- IR (11%) : R$ {ir}")
    print(f"- INSS (8%) : R$ {inss}")
    print(f"- Sindicato (5%) : R$ {sindicato}")
    print(f"= Salário Liquido : R$ {salario_liquido}")

salario_novo()
# Gostei bem mais desta maneira