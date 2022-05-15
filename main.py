#importando bibliotecas necessárias
from msilib.schema import _Validation_records
import random
from math import *
from dadosnormalizados import DADOS
import funcoes 

#dados e listas necessários
lista_de_paises =[]
lista_distancia = []
lista_dicas = []
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

#inicializando palpite
palpite = input('Qual seu palpite? ')

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
        while opcao_dica not in respostas_dica:
            print ('Opção inválida')
            opcao_dica = input('Escolha sua opção [0|1|2|3|4|5]: ')
        
        if opcao_dica == '1':
            chances -= 3
            
        elif opcao_dica == '2':
            chances -= 2
        
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
            print('Distâncias: \n {}'.format(lista_distancia))
            print('Dicas: \n {}'.format(lista_dicas))
            palpite = input('Qual seu palpite? ')

        print('Distâncias: \n {}'.format(lista_distancia))
        print('Dicas: \n {}'.format(lista_dicas))
        palpite = input('Qual seu palpite? ')

    elif palpite not in DADOS.keys():
        print('país desconhecido')
        palpite = input('Qual seu palpite? ')

    elif palpite == resposta_certa:
        print('*** Parabéns! Você acertou após {} tentativas!'. format(contador_tentativas))
        chances = 0 #isso faz com que saia do while e termine o código

    else: 
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
                for informacoes2, valores2 in dados.items():
                    if informacoes2 == 'geo':
                        for lat_long2, valores_lat_long2 in valores2.items():
                            if lat_long2 == 'latitude':
                                x2 = valores_lat_long2
                            if lat_long2 == 'longitude':
                                y2 = valores_lat_long2
        distancia = funcoes.haversine(raioterra, x1, y1, x2, y2)
        lista_distancia = funcoes.adiciona_em_ordem(palpite, distancia, lista_distancia)

        print('Distâncias: \n {}'.format(lista_distancia))
        print('Dicas: ')

    chances -= 1
    contador_tentativas += 1
    # ao final do jogo, pergunta se o usuário deseja jogar novamente
    # ta perguntando depois de cada palpite novo
    # tem algum jeito de deixar isso fora do while e caso ele queira jogar dnv retornar ao while?
    rodada_nova = input('Jogar novamente? [s|n]')
    if rodada_nova == 's':
        chances = 20
        resposta_certa = random.choice(lista_de_paises)
        print('Um país foi escolhido, tente adivinhar!') 
        print('Você tem {} tentativa(s)'.format(chances))
        palpite = input('Qual seu palpite? ')

    else:
        break
print('Até a próxima!')





{'afeganistao': 
{'area': 652230, 'populacao': 31390200, 'capital': 'Cabul', 'geo': 
{'latitude': 33.93911, 'longitude': 67.709953}, 
'bandeira': {'vermelha': 28, 'laranja': 1, 'amarela': 0, 'verde': 33, 'azul': 0, 'azul claro': 0, 'preta': 33, 'branca': 3, 'outras': 5},
 'continente': 'asia'}}

