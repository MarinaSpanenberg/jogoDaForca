print('Olá, bem-vindo ao jogo da forca')
desafiante = input("Nome do desafiante: ")
competidor = input("Nome do competidor: ")
#desafiante = propõe o jogo, pensa na palavra
#competidor = adivinha a palavra
import os
os.system("cls")

palavra_chave = input("Palavra chave: ").lower()
dicas = ["Dica 1: ","Dica 2: ","Dica 3: "]
dicas[0] = input("primeira dica: ")
dicas[1] = input("segunda dica: ")
dicas[2] = input("terceira dica: ")
os.system("cls")

print("A palavra a ser adivinhada tem um total de",len(palavra_chave),"letras")
tentativas_restantes = 6
letras_erradas = []
letras_certas = []

def solicitar_letra():
    jogadas = input("Digite uma letra:")
    return jogadas

def dicas_solicitadas():
    dicas =- 1
    return dicas

escolher_opcoes = input("Quer jogar(1) ou solicitar dica(0)?:")
if escolher_opcoes == "1":
    solicitar_letra()
    tentativas_restantes =- 1
else:
    print("A dica é:",dicas[0])
    solicitar_letra()
    tentativas_restantes =- 1

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
        print(' |             ')
        print('/|\            ')

    elif tentativas_restantes == 5:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X X)  ')
        print(' |      ( _ )  ')
        print(' |             ')
        print(' |             ')
        print(' |             ')
        print(' |             ')
        print('/|\            ')

    elif tentativas_restantes == 4:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X X)  ')
        print(' |      ( _ )  ')
        print(' |        |    ')
        print(' |        |    ')
        print(' |             ')
        print(' |             ')
        print('/|\            ')

    elif tentativas_restantes == 3:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X X)  ')
        print(' |      ( _ )  ')
        print(' |        |\   ')
        print(' |        | \  ')
        print(' |             ')
        print(' |             ')
        print('/|\            ')

    elif tentativas_restantes == 2:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X X)  ')
        print(' |      ( _ )  ')
        print(' |       /|\   ')
        print(' |      / | \  ')
        print(' |             ')
        print(' |             ')
        print('/|\            ')

    elif tentativas_restantes == 1:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X X)  ')
        print(' |      ( _ )  ')
        print(' |       /|\   ')
        print(' |      / | \  ')
        print(' |         \   ')
        print(' |          \  ')
        print('/|\            ')

    elif tentativas_restantes == 0:
        print('  ________     ')
        print(' |        |    ')
        print(' |      (X X)  ')
        print(' |      ( _ )  ')
        print(' |       /|\   ')
        print(' |      / | \  ')
        print(' |       / \   ')
        print(' |      /   \  ')
        print('/|\            ')


while tentativas_restantes > 0:
    print("você tem",tentativas_restantes,"tentativas")
    for letra in palavra_chave:
        if letra in letras_certas:
            print(letra,end=" ")
        else: 
            print("_", end=" ")
    break
    
print(palavra_chave)
