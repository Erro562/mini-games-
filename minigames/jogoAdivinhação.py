import random 
numeroLimite = 100

def menu():
    print("""
        ---------------------------
        -  Jogo da Adivinhação v1 -
        ---------------------------
        """)

def numero_aleatorio():
    numeroAleatorio = random.randint(0, numeroLimite)
    return numeroAleatorio

def verifica_numero():
    tentativas = 1
    numeroSorteado = int(numero_aleatorio())
    
    while True:
      numeroSecreto = int(input("De um chute de 1 a {}: ".format(numeroLimite)))
      

      if numeroSecreto == numeroSorteado:
          print("Parabens você acertou o numero secreto em {} Tentativas!".format(tentativas))
          break
      else: 
          tentativas +=1
          print("O numero Sorteado é menor que seu chute!")if numeroSecreto > numeroSorteado else print("O numero Sorteado é maior que seu chute!")  

def play_game():
  menu()
  verifica_numero()

play_game()