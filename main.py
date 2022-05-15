#importando bibliotecas necessárias
from msilib.schema import _Validation_records
import random
from math import *
from dadosnormalizados import DADOS
import funções 

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
    # CASO DESISTO
    if palpite == 'desisto':
        desistencia = input('Tem certeza que deseja desistir da rodada? [s|n]')
        if desistencia == 's':
            print('>>> Que deselegante desistir, o país era:{}'.format(resposta_certa))
        else:
            palpite = input('Qual seu palpite? ')

    # CASO DICAS
    elif palpite == 'dica':
        # a cada rodada de dica, as opcoes do jogador diminuem
        # CASO 1: primeira vez pedindo dicas
        if lista_dicas == []:
            print('Mercado de Dicas')
            print('----------------------------------------')
            print('1. Cor da bandeira  - custa 4 tentativas')
            print('2. Letra da capital - custa 3 tentativas')
            print('3. Área             - custa 6 tentativas')
            print('4. População        - custa 5 tentativas')
            print('5. Continente       - custa 7 tentativas')
            print('0. Sem dica')
            print('----------------------------------------')
            opcao_dica = input('Escolha sua opção [0|1|2|3|4|5]: ')
            respostas_dica = ['0','1','2','3','4','5']
            while opcao_dica not in respostas_dica:
                print ('Opção inválida')
                opcao_dica = input('Escolha sua opção [0|1|2|3|4|5]: ')

        # CASO 2: o jogador ja pediu a dica de área, somente ela
        elif 'Área' in lista_dicas and 'População'  not in lista_dicas and 'Continente' not in lista_dicas:
            print('Mercado de Dicas')
            print('----------------------------------------')
            print('1. Cor da bandeira  - custa 4 tentativas')
            print('2. Letra da capital - custa 3 tentativas')
            print('4. População        - custa 5 tentativas')
            print('5. Continente       - custa 7 tentativas')
            print('0. Sem dica')
            print('----------------------------------------')
            opcao_dica = input('Escolha sua opção [0|1|2|4|5]: ')
            del(respostas_dica[3])
            while opcao_dica not in respostas_dica:
                print ('Opção inválida')
                opcao_dica = input('Escolha sua opção [0|1|2|3|4|5]: ')
            
        if opcao_dica == '1':
            if chances<=3:
                print('Mercado de Dicas')
                print('----------------------------------------')
                print ('0. Sem dica')
                print('----------------------------------------')
                print('>>> Infelizmente, acabou seu estoque')
            chances -= 3
            for pais, dados in DADOS.items():
                if pais == resposta_certa:
                    for informacoes, valores in dados.items():
                        if informacoes == 'bandeira':
                            for cor,porcentagem in valores.items():
                                if porcentagem > 0 and cor not in lista_dicas:
                                    print('Dica:')
                                    print(' - Cores da bandeira:{0}'.format(cor))
                                    lista_dicas.append(cor)
                                    break
        elif opcao_dica == '2':
            chances -= 2
            for pais, dados in DADOS.items():
                if pais == resposta_certa:
                    for informacoes, valores in dados.items():
                        if informacoes == 'capital':
                            for letras in valores:
                                lista_letras_capital.append(letras)
                            letra_escolhida = random.choice(lista_letras_capital)
                            print('- Letras da capital: {0}'.format(letra_escolhida))
        elif opcao_dica == '3':
            chances -= 5
            # acessando a area
            for pais2, caracteristicas2 in DADOS.items():
                if pais2 == palpite:
                    for c, d in caracteristicas2.items():
                        if c == 'area':
                            lista_dicas.append('-Área: {}'.format(d))
            
        elif opcao_dica == '4':
            chances -= 4
            # acessando a populacao
            for pais3, caracteristicas3 in DADOS.items():
                if pais3 == palpite:
                    for e, f in caracteristicas3.items():
                        if e == 'area':
                            lista_dicas.append('-População: {}'.format(f))

        elif opcao_dica == '5':
            chances -= 6
            # acessando o continente
            for nome_pais, caracteristicas in DADOS.items():
                if nome_pais == palpite:
                    for a, b in caracteristicas.items():
                        if a == 'continente':
                            lista_dicas.append('-Continente: {}'.format(b))
            
        elif opcao_dica == '0':
            print('Dica: ')
            palpite = input('Qual seu palpite? ')

        print('Distâncias: \n {}'.format(lista_distancia))
        print('Dicas: \n {}'.format(lista_dicas))
        palpite = input('Qual seu palpite? ')

    # CASO PAÍS NÃO EXISTE
    elif palpite not in DADOS.keys():
        print('país desconhecido')
        palpite = input('Qual seu palpite? ')

    # CASO ACERTOU O PAÍS
    elif palpite == resposta_certa:
        print('*** Parabéns! Você acertou após {} tentativas!'. format(contador_tentativas))
        chances = 0 #isso faz com que saia do while e termine o código

    # CASO CHUTE NOME DE UM PAÍS
    else: 
        #latitude e longitude
        for pais, dados in DADOS.items():
            if pais == resposta_certa:
                for informacoes, valores in dados.items():
                    if informacoes == 'geo':
                        for lat_long, valores_lat_long in valores.items():
                            if lat_long == 'latitude':
                                x1 = valores_lat_long
                            if lat_long == 'longitude':
                                y1 = valores_lat_long
            if pais == palpite:
                for item2, especificidades2 in pais.items():
                    if item2 == 'latitude':
                        x2 = especificidades2 
                    if item2 == 'longitude':
                        y2 = especificidades2 
        distancia = funções.haversine(raioterra, x1, y1, x2, y2)
        lista_distancia.append('{} km -> {}'.format(distancia, palpite)) #tem que por em ordem da menor distancia para maior
        print('Distâncias: \n {}'.format(lista_distancia))
    
{'afeganistao': 
{'area': 652230, 'populacao': 31390200, 'capital': 'Cabul', 'geo': 
{'latitude': 33.93911, 'longitude': 67.709953}, 
'bandeira': {'vermelha': 28, 'laranja': 1, 'amarela': 0, 'verde': 33, 'azul': 0, 'azul claro': 0, 'preta': 33, 'branca': 3, 'outras': 5},
 'continente': 'asia'}}

