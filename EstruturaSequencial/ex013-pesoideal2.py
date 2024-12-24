# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

# tive uma idéia, vamos usar funções, tipo, se resposta for f, cham função peso_f(), acho que vai!

def peso():

    h = float(input("Qual a sua altura? (em metros) "))
    sexo = input("Qual o seu sexo? ('m' para masculino e 'f' para feminino) ")

    while True:

        if sexo == 'm' or sexo == 'M':
            peso_ideal = (72.7*h) - 58
            peso_ideal = round(peso_ideal, 2)
            print("Seu peso ideal é: ", peso_ideal, 'kg.')
            break
        
        elif sexo == 'f' or  sexo == 'F':
            peso_ideal = (62.1*h) - 44.7
            peso_ideal = round(peso_ideal, 2)
            print("Seu peso ideal é: ", peso_ideal, 'kg.')
            break
        
        else:
            print("Seleção incorreta, tente novamente.")
            peso()

peso()


