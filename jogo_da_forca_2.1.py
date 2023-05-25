#Dupla: João Vitor Bortoluz - RA:1134776 e Marina Barbosa - RA:1135358
import os

#funções criadas para economizar linhas
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

    if tentativas_restantes == 5:
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

#Looping do código   
while True:
    print('Olá, Bem-Vindos(as) ao Jogo da Forca!')
    print("Feito por João Vitor Bortoluz e Marina Barbosa \nTurma A")
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

    print("A palavra a ser adivinhada tem um total de",len(palavra_chave),"letras")
    tentativas_restantes = 6
    letras_erradas = []
    letras_certas = [] 
    while tentativas_restantes >= 0:
        print("Você tem",tentativas_restantes,"tentativas!")
        forca(tentativas_restantes)
        print("Letras erradas:", letras_erradas)
        for letra in palavra_chave:
            if letra in letras_certas:
                print(letra,end=" ")
            else: 
                print("_", end=" ")
        escolher_opcoes = input("\nQuer jogar(1) ou solicitar dica(0)?:").lower()
        if escolher_opcoes == "1":
            jogadas = solicitar_letra()
            if jogadas in palavra_chave:
                letras_certas.append(jogadas)
            else:
                if jogadas in letras_erradas:
                    print("Você já tentou esse letra!")
                else:
                    letras_erradas.append(jogadas)
                    print("Você errou!")
                    tentativas_restantes -= 1
        elif escolher_opcoes == "0":
            dicas_solicitadas(dicas)
            jogadas = solicitar_letra()
            if jogadas in palavra_chave:
                letras_certas.append(jogadas)
            else:
                if jogadas in letras_erradas:
                    print("Você já tentou esse letra!")
                else:
                    letras_erradas.append(jogadas)
                    print("Você errou!")       
                    tentativas_restantes -= 1
        else:
            print("Tente novamente!")
        if set(palavra_chave).issubset(set(letras_certas)):
            print("A palavra era",palavra_chave)
            print("Parabéns {}!!! Tente um desafio mais complexo, {}.".format(competidor,desafiante))
            break
        elif tentativas_restantes == 0:
            forca(tentativas_restantes=0)
            print("A palavra era",palavra_chave)
            print("Parabéns {}!!! {} não conseguiu vencer seu desafio.".format(desafiante,competidor))
            break
        
    jogar_novamente = input("Você deseja jogar novamente? Sim(1) ou Não(0): ")
    if jogar_novamente == "0":
       print("Obrigado por jogar! Até a próxima!")
       break
    elif jogar_novamente != "1" and jogar_novamente != "0":
        print("Resposta inválida. O jogo será encerrado!")
        break