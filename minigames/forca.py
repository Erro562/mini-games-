from random import choice

def escolhe_tema(temas):
    if temas == "Bebidas":
        bebidas = choice(["cerveja","gin","licor","rum","Vinho","Vodka","Tequila","Whisky","Guaraná" ])
        return bebidas
    elif temas == "frutas":
        frutas = choice(["abacaxi", "abacate", "amora", "banana", "bacuri", "buriti","Açaí","Acerola","Cacau","Caqui","Carambola" ])
        return frutas
    else:
        nomes = choice(["Alice","Laura","Beatriz","Manuela","Helena","Maria","Eduarda","Isabela","Valentina","Júlia","Sophia"])
        return nomes

temas = choice(["Bebidas", "frutas", "Nomes"])
palavra_secreta = escolhe_tema(temas).upper()
ganhou = False
tentativas = 5
letras_corretas = set()

def chuta_palavra():
    global ganhou, tentativas, letras_corretas

    print("O tema é {}".format(temas))

    while tentativas > 0 and not ganhou:
        chute = input("Digite uma letra ou a palavra inteira: ").upper()

        if len(chute) == 1:  # Se o chute é uma única letra
            acertou = False
            for i, letra in enumerate(palavra_secreta):
                if chute == letra or letra in letras_corretas:
                    print(letra, end=" ")
                    if chute == letra:
                        letras_corretas.add(chute)
                        acertou = True
                else:
                    print("_", end=" ")
            print()

            if not acertou:
                tentativas -= 1
                print("Letra incorreta! Tentativas restantes: {}".format(tentativas))

        elif chute == palavra_secreta:  # Se o chute é a palavra inteira
            ganhou = True

        else:
            print("Chute incorreto! Tente novamente.")

        if set(palavra_secreta) == letras_corretas:
            ganhou = True

    if ganhou:
        print("Parabéns! Você acertou a palavra secreta com {} tentativas restante".format(tentativas))
    else:
        print("Você perdeu. A palavra era:", palavra_secreta)

chuta_palavra()