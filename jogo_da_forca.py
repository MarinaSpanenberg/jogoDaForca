import os

print('Olá, Bem-Vindos(as) ao Jogo da Forca!')
desafiante = input("Nome do desafiante: ")
competidor = input("Nome do competidor: ")
#desafiante = propõe o jogo, pensa na palavra
#competidor = adivinha a palavra

os.system("cls")

palavra_chave = input("Palavra chave: ").lower()
dicas = ["Dica 1: ","Dica 2: ","Dica 3: "]
dicas[0] = input("Primeira dica: ")
dicas[1] = input("Segunda dica: ")
dicas[2] = input("Terceira dica: ")
os.system("cls")

    
def solicitar_letra():
    jogadas = input("Digite uma letra:")
    return jogadas.lower()

def dicas_solicitadas(dicas):
    if dicas:
       dica = dicas.pop(0)
       print ("A dica é:", dica)
    else:
        print("Você usou todas as dicas!")
        
#forca
def forca(tentativas_restantes):
    if tentativas_restantes == 6:
        print('  ________     ')
        print(' |        |    ')
        print(' |             ')
        print(' |             ')
        print(' |             ')
        print(' |             ')
        print(' |             ')
        print('/|\            ')

    elif tentativas_restantes == 5:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X_X)  ')
        print(' |             ')
        print(' |             ')
        print(' |             ')
        print(' |             ')
        print('/|\            ')

    elif tentativas_restantes == 4:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X_X)  ')
        print(' |        |    ')
        print(' |        |    ')
        print(' |             ')
        print(' |             ')
        print('/|\            ')

    elif tentativas_restantes == 3:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X_X)  ')
        print(' |        |\   ')
        print(' |        | \  ')
        print(' |             ')
        print(' |             ')
        print('/|\            ')

    elif tentativas_restantes == 2:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X_X)  ')
        print(' |       /|\   ')
        print(' |      / | \  ')
        print(' |             ')
        print(' |             ')
        print('/|\            ')

    elif tentativas_restantes == 1:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X_X)  ')
        print(' |       /|\   ')
        print(' |      / | \  ')
        print(' |         \   ')
        print(' |          \  ')
        print('/|\            ')

    elif tentativas_restantes == 0:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X_X)  ')
        print(' |       /|\   ')
        print(' |      / | \  ')
        print(' |       / \   ')
        print(' |      /   \  ')
        print('/|\            ')




print("A palavra a ser adivinhada tem um total de",len(palavra_chave),"letras")
tentativas_restantes = 6
letras_erradas = []
letras_certas = []
palavra_visivel = "_" * len(palavra_chave)

while tentativas_restantes >= 0:
    escolher_opcoes = input("\nQuer jogar(1) ou solicitar dica(0)?:")
    print("Você tem",tentativas_restantes,"tentativas!")
    if escolher_opcoes == "1":
       jogadas = solicitar_letra()
       if jogadas in palavra_chave:
           letras_certas.append(jogadas)
       else:
           letras_erradas.append(jogadas)
           print("Você errou!")
           forca(tentativas_restantes)
           tentativas_restantes -= 1
    else:
        dicas_solicitadas(dicas)
        jogadas = solicitar_letra()
        if jogadas in palavra_chave:
           letras_certas.append(jogadas)
        else:
           letras_erradas.append(jogadas)
           print("Você errou!")
           forca(tentativas_restantes)
           tentativas_restantes -= 1

    palavra_visivel = ""
    for letra in palavra_chave:
        if letra in letras_certas:
            palavra_visivel += letra
        else:
            palavra_visivel += "_"
    print(palavra_visivel)