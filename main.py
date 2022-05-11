#importando bibliotecas necessárias
import random
from math import *
from dadosnormalizados import DADOS

#página inicial
print(' ============================ ')
print('|                            |')
print('| Bem-vindo ao Insper Países |')
print('|                            |')
print(' ==== Design de Software ==== \n')
print('Comandos:\n' '   dica       - entra no mercado de dicas\n' '   desisto    - desiste da rodada\n' '   inventario - exibe sua posição\n')
print('Um país foi escolhido, tente adivinhar!') 
print('Você tem 20 tentativa(s)')

#inicializando palpite e selecionando aleatoriamente um pais
palpite = input('Qual seu palpite?')
correto = random.choice(DADOS.keys())


