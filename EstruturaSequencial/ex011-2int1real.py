# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1 - o produto do dobro do primeiro com metade do segundo .
# 2 - a soma do triplo do primeiro com o terceiro.
# 3 - o terceiro elevado ao cubo

# Realizei com loops pois estava  preocupado com a utilizaçÃo/validaçÃo dos numeros int e float
# Dai pensei nesta abordagem, de usar loop para retornar caso haja erros...

def numeros():
    # esta fora para que ao entrar no loops, já vai direto para os ifs.
    # deixa tudo float, para funcionar o is_integer(), não achei o "é_flutuante()" algo assim no python ;-;
    n1 = float(input("Digite um número inteiro (primeiro número): "))
    n2 = float(input("Digite outro número inteiro (segundo número): "))
    n3 = float(input("Digite um número real (terceiro número): "))
    while True:
        
        if n1.is_integer() and n2.is_integer(): # esse "is_integer()" é muito top, ele é basicamente o "n1.é_inteiro()?"
            # show de bola

            produto = (n1 * 2) * (n2 / 2)
            soma = (n1 * 3) + n3
            cubo = n3 ** 3

            print("O produto do dobro do primeiro com metade do segundo é:", produto)
            print("A soma do triplo do primeiro com o terceiro é:", soma)
            print("O terceiro elevado ao cubo é:", cubo)
            print("Fim do programa.")
            break

        elif n3.is_integer():
            print("O terceiro número deve ser um número real. Tente novamente.")
            numeros() # o mais certo seria usar continue, mas não faça isso, pois fica infinitamente uma mensagem

        else:
            print("Os dois primeiros números devem ser inteiros. Tente novamente.")
            numeros()

numeros()
# talvez seria melhor um if para cada numero? para ficar mais dinamico? eu não sei... mas que """funciona""", funciona.
