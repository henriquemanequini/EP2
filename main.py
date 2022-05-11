#importando bibliotecas necessárias
import random
from math import *
from dadosnormalizados import DADOS

chances = 20

#página inicial
print(' ============================ ')
print('|                            |')
print('| Bem-vindo ao Insper Países |')
print('|                            |')
print(' ==== Design de Software ==== \n')
print('Comandos:\n' '   dica       - entra no mercado de dicas\n' '   desisto    - desiste da rodada\n' '   inventario - exibe sua posição\n')
print('Um país foi escolhido, tente adivinhar!') 
print('Você tem {} tentativa(s)'.format(chances))

#inicializando palpite e selecionando aleatoriamente um pais
palpite = input('Qual seu palpite? ')
resposta_certa = random.choice(DADOS.keys())

raioterra = 6371
lista_distancia = []
lista_dicas = []

while chances > 0:
    if palpite == 'desisto':
        desistencia = input('Tem certeza que deseja desistir da rodada? [s|n]')
        if desistencia == 's':
            print('>>> Que deselegante desistir, o país era:{}'.format(resposta_certa))
        else:
            palpite = input('Qual seu palpite? ')

    elif palpite == 'dica':
        print('Mercado de Dicas')
        print('----------------------------------------')
        print('1. Cor da bandeira  - custa 4 tentativas')
        print('2. Letra da capital - custa 3 tentativas')
        print('3. Área             - custa 6 tentativas')
        print('4. População        - custa 5 tentativas')
        print('5. Continente       - custa 7 tentativas')
        print('0. Sem dica')
        print('----------------------------------------')
        opcao_dica = input('Escolha sua opção [0|1|2|3|4]: ')
        respostas_dica = ['0','1','2','3','4','5']
        opcao_dica = input('Escolha sua opção [0|1|2|3|4]: ')
        respostas_dica = ['0','1','2','3','4','5']
        
        while opcao_dica not in respostas_dica:
            print ('Opção inválida')
            opcao_dica = input('Escolha sua opção [0|1|2|3|4]: ')
        if opcao_dica == '1':
            chances -= 3
        elif opcao_dica == '2':
            chances -= 2
        elif opcao_dica == '3':
            chances -= 5
        elif opcao_dica == '4':
            chances -= 4
        elif opcao_dica == '0':
            palpite = input('Qual seu palpite? ')    
        else:
            print ('Opção inválida')
            opcao_dica = input('Escolha sua opção [0|1|2|3|4]: ')
