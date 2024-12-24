# Tendo como dados de entrada a altura de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input('Digite sua altura: '))
peso_ideal = (72.7 * altura) - 58
peso_ideal = round(peso_ideal, 2) # este comando é um classico, lembranças do javascript, ele formatará o numero para 2 casas decimais, no javascript seria toFixed(2)
print('Seu peso ideal é: ', peso_ideal)

# ieeei, queria usar loops