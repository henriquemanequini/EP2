import random
from math import *
from dadosnormalizados import DADOS
from funcoes import *

#dados e listas necessários
lista_de_paises =[]
lista_distancia = []
lista_dicas = []
mostrador_dicas = []
lista_letras_capital = []
dicionario_cores = {'- Cores da bandeira': []}
dicionario_capital = {}
mercado = 'Mercado de Dicas \n ---------------------------------------- \n 1. Cor da bandeira  - custa 4 tentativas \n 2. Letra da capital - custa 3 tentativas \n 3. Área             - custa 6 tentativas \n 4. População        - custa 5 tentativas \n 5. Continente       - custa 7 tentativas \n 0. Sem dica \n ----------------------------------------'

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
    
    elif palpite == 'dica':
        # a cada rodada de dica, as opcoes do jogador diminuem
        # CASO 1: primeira vez pedindo dicas
        if mostrador_dicas == []:
            print(mercado)
            opcao_dica = input('Escolha sua opção [0|1|2|3|4|5]: ')
            respostas_dica = ['0','1','2','3','4','5']

            while opcao_dica not in respostas_dica:
                print ('Opção inválida')
                opcao_dica = input('Escolha sua opção [0|1|2|3|4|5]: ')

            if opcao_dica == '1':
                if chances < 4:
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
                                            print(' - Cores da bandeira:{0}'.format(cor))
                                            lista_dicas.append(dicionario_cores)
                                            mostrador_dicas.append(cor)
                                            
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
                                lista_dicas.append('- Letras da capital: {0}'.format(letra_escolhida))
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
                                print('-População: {}'.format(f))
                                lista_dicas.append('-População: {}'.format(f))

            elif opcao_dica == '5':
                chances -= 6
                # acessando o continente
                for nome_pais, caracteristicas in DADOS.items():
                    if nome_pais == palpite:
                        for a, b in caracteristicas.items():
                            if a == 'continente':
                                lista_dicas.append('-Continente: {}'.format(b))
                                print('-Continente: {}'.format(b))
                
            elif opcao_dica == '0':
                print('Dica: ')
                palpite = input('Qual seu palpite? ')

            print('Distâncias: \n {}'.format(lista_distancia))
            print('Dicas: \n {}'.format(lista_dicas))
            palpite = input('Qual seu palpite? ')

        if mostrador_dicas != []:
            if cor in mostrador_dicas: