# 4 notas bimestrais e a média

nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))
nota_4 = float(input('Digite a quarta nota: '))
media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# abaixo coloquei um simples "if" para verificar se a média é menor que 5, se for, o aluno está reprovado, se for maior ou igual a 5, o aluno está aprovado
if media < 5:
    print('sua média é: ', media)
    print('Reprovado')
elif media >= 5 and media <= 10:
    print('sua média é: ', media)
    print('Aprovado')
