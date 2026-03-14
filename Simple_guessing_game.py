import random
numero_secreto = random.randint(1, 10)
tentativas = 0
print('Bem-vindo ao jogo de adivinhação!')  
print('Tente adivinhar o número secreto entre 1 e 10.')
while True:
    palpite = input('Digite seu palpite: ')
    palpite = int(palpite)
    tentativas += 1
    if palpite < numero_secreto:
        print('Muito baixo! Tente novamente.')
    elif palpite > numero_secreto:
        print('Muito alto! Tente novamente.')
    else:
        print(f'Parabéns! Você adivinhou o número secreto {numero_secreto} em {tentativas} tentativas!')
        break