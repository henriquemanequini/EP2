from ctypes.wintypes import VARIANT_BOOL
import random
from math import *
from dadosnormalizados import DADOS
from funcoes import *

#dados e listas necessários
lista_de_paises =[]
lista_distancia = []
lista_dicas = []
mostrador_dicas = []
letra_escolhida = []
dicionario_cores = {'- Cores da bandeira': []}
dicionario_capital = {}
mercado = 'Mercado de Dicas \n ---------------------------------------- \n 1. Cor da bandeira  - custa 4 tentativas \n 2. Letra da capital - custa 3 tentativas \n 3. Área             - custa 6 tentativas \n 4. População        - custa 5 tentativas \n 5. Continente       - custa 7 tentativas \n 0. Sem dica \n ----------------------------------------'
letras_capital = []
continente_cont = 0
area_cont = 0
populacao_cont = 0

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
        print('* Parabéns! Você acertou após {} tentativas!'. format(contador_tentativas))

    elif palpite in DADOS.keys() and palpite != resposta_certa:
        distancia = int(haversine(raioterra, DADOS[resposta_certa]['geo']['latitude'], DADOS[resposta_certa]['geo']['longitude'], DADOS[palpite]['geo']['latitude'], DADOS[palpite]['geo']['longitude']))
        lista_distancia = adiciona_em_ordem2(palpite, distancia, lista_distancia)
        print('Distâncias: {}'.format(lista_distancia))
        print('Dicas: {}'.format(lista_dicas))

    elif palpite == 'dica':
        print(mercado)
        texto_opcao_dica = 'Escolha sua opção [0|1|2|3|4|5]: '
        opcao_dica = input(texto_opcao_dica)
        respostas_dica = ['0','1','2','3','4','5']

        while opcao_dica not in respostas_dica:
            print ('Opção inválida')
            opcao_dica = input(texto_opcao_dica)

        if opcao_dica == '1':
            if chances < 5:
                print('Mercado de Dicas')
                print('----------------------------------------')
                print ('0. Sem dica')
                print('----------------------------------------')
                print('>>> Infelizmente, acabou seu estoque')
                palpite = input('Qual seu palpite? ')

            else:
                chances -= 3
                for pais, dados in DADOS.items():
                    if pais == resposta_certa:
                        for informacoes, valores in dados.items():
                            if informacoes == 'bandeira':
                                for cor, porcentagem in valores.items():
                                    if porcentagem > 0 and cor not in mostrador_dicas:
                                        dicionario_cores['- Cores da bandeira'].append(cor)
                                        print('Distâncias:'.format(lista_distancia))
                                        print('Dicas:')
                                        print(' - Cores da bandeira:{0}'.format(cor))
                                        lista_dicas.append(dicionario_cores)
                                        mostrador_dicas.append(cor)
                                        break
                                        
        elif opcao_dica == '2':
            if chances < 4:
                print('Mercado de Dicas')
                print('----------------------------------------')
                print ('0. Sem dica')
                print('----------------------------------------')
                print('>>> Infelizmente, acabou seu estoque')
                palpite = input('Qual seu palpite? ')
            else:
                chances -= 2
                for pais, dados in DADOS.items():
                    if pais == resposta_certa:
                        for informacoes, valores in dados.items():
                            if informacoes == 'capital':
                                sorteada = sorteia_letra(dados['capital'],letra_escolhida)
                                letra_escolhida.append(sorteada)
                                print('Distâncias'.format(lista_distancia))
                                print('Dicas:')
                                print('- Letras da capital: {0}'.format(letra_escolhida))
                                lista_dicas.append('- Letras da capital: {0}'.format(letra_escolhida))
        elif opcao_dica == '3':
            if chances < 7:
                print('Mercado de Dicas')
                print('----------------------------------------')
                print ('0. Sem dica')
                print('----------------------------------------')
                print('>>> Infelizmente, acabou seu estoque')
                palpite = input('Qual seu palpite? ')
            elif chances>=7 and area_cont == 0 :
                mercado = mercado.replace('3. Área             - custa 6 tentativas\n', '')
                chances -= 5
                area = DADOS[resposta_certa]['area']
                print('Distância:'.format(lista_distancia))
                print('Dicas:')
                print('-Área: {}'.format(area))
                lista_dicas.append('-Área: {}'.format(area))
                area_cont += 1
                texto_opcao_dica = texto_opcao_dica.replace('3|', '')
            else:
                print('Opção inválida')
                opcao_dica = input(texto_opcao_dica)

        elif opcao_dica == '4':
            if chances < 6:
                print('Mercado de Dicas')
                print('----------------------------------------')
                print ('0. Sem dica')
                print('----------------------------------------')
                print('>>> Infelizmente, acabou seu estoque')
                palpite = input('Qual seu palpite? ')
            elif chances>=6 and populacao_cont==0:
                mercado = mercado.replace('4. População        - custa 5 tentativas \n', '')
                chances -= 4
                populacao = DADOS[resposta_certa]['populacao']
                print('Distâncias:'.format(lista_distancia))
                print('Dicas:')
                print('-População: {}'.format(populacao))
                lista_dicas.append('-População: {}'.format(populacao))
                populacao_cont += 1
                texto_opcao_dica = texto_opcao_dica.replace('4|', '')
            else:
                print('Opção inválida')
                opcao_dica = input(texto_opcao_dica)
    
        elif opcao_dica == '5':
            if chances < 8:
                print('Mercado de Dicas')
                print('----------------------------------------')
                print ('0. Sem dica')
                print('----------------------------------------')
                print('>>> Infelizmente, acabou seu estoque')
                palpite = input('Qual seu palpite? ')
            elif chances>=8 and continente_cont==0: 
                mercado = mercado.replace('5. Continente       - custa 7 tentativas \n', '')
                chances -= 6
                continente = DADOS[resposta_certa]['continente']
                lista_dicas.append('-Continente: {}'.format(continente))
                print('Distâncias:'.format(lista_distancia))
                print('Dicas:')
                print('-Continente: {}'.format(continente))
                continente_cont += 1
                texto_opcao_dica = texto_opcao_dica.replace('|5', '')
            else:
                print('Opção inválida')
                opcao_dica = input(texto_opcao_dica)

        elif opcao_dica == '0':
            print('Distâncias: {}'.format(lista_distancia))
            print('Dicas: {}'.format(lista_dicas))
            palpite = input('Qual seu palpite? ')

    elif palpite not in DADOS.keys():
        print('país desconhecido')
        palpite = input('Qual seu palpite? ')
    palpite = input('Qual seu palpite? ')
if chances == 0:
        print('Você perdeu! O país era {resposta_certa}')
        rodada_nova = input('Jogar novamente? [s|n]')
        if rodada_nova == 's':
            chances = 20
            resposta_certa = random.choice(lista_de_paises)
            print('Um país foi escolhido, tente adivinhar!') 
            print('Você tem {} tentativa(s)'.format(chances))
            palpite = input('Qual seu palpite? ')