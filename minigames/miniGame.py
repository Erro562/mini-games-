from random import choice

jogador_vitorias = 0
maquina_vitorias = 0

def opcao_jogador():
    esc_jogador =input("Escolha (1) - Pedra | (2) - Papel | (3) - Tesoura: ")
    esc_jogador.lower()
    if esc_jogador in ["1","pedra"]:
        return "pedra"
    elif esc_jogador in ["2","papel"]:
        return "papel"
    elif esc_jogador in ["3","tesoura"]:
        return "tesoura"
    else:
        print("A opção está Inválida!. Tente novamente...")
        opcao_jogador()

def opcao_maquina():
    esc_maquina = choice(["pedra","papel","tesoura"])
    return esc_maquina


while True:

    print("_"*30)
    esc_Jogador = opcao_jogador()
    esc_maquina = opcao_maquina()
    print("_"*30)

    if(esc_Jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_Jogador == "papel") and (esc_maquina == "pedra")\
        or (esc_Jogador == "tesoura") and (esc_maquina == "papel"):
        #Jogador ganha
        jogador_vitorias+=1
        print("O Jogador escolheu {} e a Maquina escolheu {}\n Parabéns, Você Ganhou!!".format(esc_Jogador,esc_maquina))

    elif esc_Jogador == esc_maquina:
        #Empate
        print("Ocorreu um empate!")
    else:
        #maquina ganha
        maquina_vitorias+=1
        print("O Jogador escolheu {} e a Maquina escolheu {}\n A Maquina Ganhou!!".format(esc_Jogador,esc_maquina))


    print("_"*30)
    print("Vitorias do Jogador: {}".format(jogador_vitorias))
    print("Vitorias da Maquina: {}".format(maquina_vitorias))
    print("_"*30)

    esc_Jogador = input("Deseja jogar novamente:? ")
    if esc_Jogador in ["Sim","sim","s","S","SIM"]:
        pass
    elif esc_Jogador in [ "Não","nao","Nao","n","N","não","NAO"]:
        break
    else:
        break