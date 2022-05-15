import random
from math import *
from dadosnormalizados import DADOS
from funcoes import *

#dados e listas necessários
lista_de_paises =[]
lista_distancia = []
lista_dicas = []
lista_letras_capital = []
for pais in DADOS.keys():
    lista_de_paises.append(pais)

resposta_certa = random.choice(lista_de_paises)
raioterra = 6371
contador_tentativas = 0
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

while chances > 0:

    if palpite == resposta_certa:
        print('*** Parabéns! Você acertou após {} tentativas!'. format(contador_tentativas))
        rodada_nova = input('Jogar novamente? [s|n]')
        if rodada_nova == 's':
            chances = 20
            resposta_certa = random.choice(lista_de_paises)
            print('Um país foi escolhido, tente adivinhar!') 
            print('Você tem {} tentativa(s)'.format(chances))
            palpite = input('Qual seu palpite? ')
        else:
            chances = 0 #isso faz com que saia do while e termine o código

    elif palpite in DADOS.keys() and palpite != resposta_certa:
        distancia = int(haversine(raioterra, DADOS[resposta_certa]['geo']['latitude'], DADOS[resposta_certa]['geo']['longitude'], DADOS[palpite]['geo']['latitude'], DADOS[palpite]['geo']['longitude']))
        lista_distancia = adiciona_em_ordem2(palpite, distancia, lista_distancia)
