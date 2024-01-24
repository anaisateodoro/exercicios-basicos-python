'''6) Vamos construir um jogo de forca. O programa escolherá aleatoriamente uma palavra secreta de uma lista predefinida. A palavra secreta será representada por espaços em branco, um para cada letrada palavra. 
O jogador terá um número limitado de 6 tentativas. Em cada tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente na palavra secreta, ela será revelada nas posições correspondentes. Se
a letra não estiver na palavra, uma mensagem de erro deverá ser informada. Após um número máximo de erros, o jogador perde. O jogo
continua até que o jogador adivinhe a palavra ou exceda o número máximo de tentativas.
Dica: Você precisará importar uma biblioteca para resolver esse
exercício
'''
import random
print('\n-------------------------------------------------------------------------------------')
print('\n-------------------------------------------------------------------------------------')
print('\n------------------------------JOGO DA FORCA \O/ WOMAKERSCODE-------------------------')
print('\n-------------ADVINHE O NOME DE UMA DAS DEVS DO BOOTCAMP BACK-END PYTHON -------------')
print('\n-------------------------------------------------------------------------------------')
print('\n-------------------------------------------------------------------------------------')

# Lista de palavras disponíveis (Devs da WomakeCoders)
palavras = ['Cynthia', 'Camila', 'Mariana']

palavra_secreta = random.choice(palavras).lower()
palavra_revelada = ['_' for _ in palavra_secreta]
numero_de_tentativas = 6

def verifica_letra(palavra_secreta, letra, palavra_revelada):
    indices = [i for i, char in enumerate(palavra_secreta) if char == letra]
    for indice in indices:
        palavra_revelada[indice] = letra
    return len(indices) > 0

while numero_de_tentativas > 0:
    print(' '.join(palavra_revelada))
    letra = input("Digite uma letra: ").lower()

    if verifica_letra(palavra_secreta, letra, palavra_revelada):
        if '_' not in palavra_revelada:
            print("Parabéns, você ganhou! O nome da Dev é " + palavra_secreta.upper() + ".")
            break
    else:
        print("Letra incorreta")
        numero_de_tentativas -= 1

    if numero_de_tentativas == 0:
        print("Desculpe, você perdeu. O nome da Deve é" + palavra_secreta.upper() + ".")
