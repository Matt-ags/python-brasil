# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em 
# metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 
# 18 litros,
# que custam R$ 80,00. 
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# Constantes
LATAS_LITROS_TINTA = 18
PRECO_LATA = 80.00
COBERTURA_TINTA = 3 # 1 litro para cada 3 metros quadrados

def tinta():
    metros_quadrados = float(input("Qual o tamanho em metros quadrados da área a ser pintada? "))
    litros = metros_quadrados / COBERTURA_TINTA # Calculo da quantidade de litros que será necessário
    latas = litros / LATAS_LITROS_TINTA # Calculo da quantidade de latas que será necessário
    preco_total = latas * PRECO_LATA
    latas = round(latas, 2)
    preco_total = round(preco_total, 2)
    if latas < 1: # Coloquei este "bonus", pois estava em duvida caso fosse uma parede pequena

        # lembra, 1 lata tem 18 litros
        print(f"Será necessário {latas} latas de tinta.")
        litros = round(litros, 2)
        print(f"Como é menos de uma lata, da lata, você precisará de {litros} litros de tinta.")
        porcentagem = (litros / LATAS_LITROS_TINTA) * 100
        porcentagem = round(porcentagem, 2)
        print(f"Isso equivale a {porcentagem}% de uma lata.")
        print(f"O preço total será de R$ {preco_total}.")

    else:
    
        print(f"Será necessário {latas} latas de tinta.")
        print(f"O preço total será de R$ {preco_total}.")

tinta()