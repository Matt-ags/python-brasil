# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
# (50 quilos)
# deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite 
# e na variável multa o valor da multa que João deverá pagar. 
# Imprima os dados do programa com as mensagens adequadas.

# deixando por fora as constantes:
LIMITE = 50
MULTA = 4.00
def pesca():
    peso = float(input("Qual o peso dos peixes? "))
    if peso > LIMITE:
        excesso = peso - LIMITE
        multa = excesso * MULTA
        excesso = round(excesso, 2)
        multa = round(multa, 2)
        print(f"O peso dos peixes é de {peso} kg.")
        print(f"O peso excedente é de {excesso} kg e a multa é de R$ {multa}.")
        # este "f" acima é a "formatação", tinha usado no projeto "listas" meu antigo, basicamente deixa ele organzado, sem precisar usar "contatenação".

    else:
        print(f"O peso dos peixes é de {peso} kg.")
        print(f"Peso dentro do limite permitido ({LIMITE} kg.).")
        
pesca()