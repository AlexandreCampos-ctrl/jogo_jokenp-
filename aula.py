from colorama import Fore
import random
import time

opcoes = ['PEDRA', 'PAPEL', 'TESOURA']

print(Fore.CYAN + '=-' * 10)
print(Fore.GREEN + '    JOKENPÔ    ')
print(Fore.CYAN + '=-' * 10)

print("Suas opções:\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA")
# Recebe a escolha do jogador
jogador = int(input('Qual é a sua jogada? '))

# Verifica se a opção é válida
if jogador < 1 or jogador > 3:
    print(Fore.BLUE + 'Opção invalida. pfvr Tente Novamente!' )
else:
    # Converte para o nome da jogada
    jogada_jogador = opcoes[jogador -1]

    # Escolha do computador
    computador = random.randint(1, 3)
    jogada_computador = opcoes[computador -1]

    # Animação estilo "JO-KEN-PO"
    print(Fore.YELLOW + '\nJO...')
    time.sleep(0.5)

    print('KEN...')
    time.sleep(0.5)

    print('PÔ!!!\n')
    time.sleep(0.3)

    print(Fore.GREEN + '<-' * 12)
    print(Fore.LIGHTMAGENTA_EX + f'Você jogou: {jogada_jogador}')
    print(f'Computador jogou: {jogada_computador}')
    print(Fore.GREEN + '->' * 12)-

    if jogador == computador:
        print(Fore.BLUE + 'Empate!')
    elif(jogador == 1 and computador == 3) or \
        (jogador == 2 and  computador ==1) or \
        (jogador == 3 and computador == 2):
        print(Fore.GREEN + 'Você VENCEU!')
    else:
        print(Fore.RED +  'Você PERDEU!.🎉')
           





