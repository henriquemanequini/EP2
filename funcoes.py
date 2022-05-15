#sorteando paises
from math import *
import random 
def sorteia_pais(dicionario):
    lista_paises = []
    for paises in dicionario.keys():
        lista_paises.append(paises)
    return random.choice(lista_paises)
    
#distancia de haversine
def haversine(r, x1, y1, x2, y2):
    d = 2*r*asin(((sin((radians(x2)-radians(x1))/2))**2 + cos(radians(x1))*cos(radians(x2))*(sin((radians(y2)-radians(y1))/2)**2))**(1/2))
    return d

#adicionando em uma lista ordenada
def adiciona_em_ordem(pais, distancia, lista):
    i = 0
    if lista == []:
        lista.append(['{} km -> {}'.format(pais, distancia)])
        return lista
    for paises in lista:
        if paises[0] == pais:
            return lista
        if paises[1] > distancia:
            lista.insert(i, ['{} km -> {}'.format(pais, distancia)])
            break
        i += 1
    return lista
def adiciona_em_ordem(pais,distancia,lista_pais_distancia):
    novo = [pais,distancia]
    i = 0
    if lista_pais_distancia == []:
        lista_pais_distancia.append(novo)    
    if novo not in lista_pais_distancia:
        for paises_distancias in lista_pais_distancia:
            if paises_distancias[1]>distancia:
                lista_pais_distancia.insert(i,novo)
                break
            i+=1
        if distancia > lista_pais_distancia[-1][1]:
            lista_pais_distancia.insert(i,novo)
    return lista_pais_distancia
  

#esta na lista
def esta_na_lista(pais, lista):
    for paises in lista:
        if pais in paises:
            return True
    return False
    
#sorteia letra com restrições
import random 
def sorteia_letra(palavra, restritas):
    palavra = palavra.lower()
    lista_palavra = []
    caracteres_especiais = ['.', ',', '-', ';', ' ']
    sorteada = ''
    ok = False
    for letra in palavra:
        if letra not in lista_palavra and letra not in restritas and letra not in caracteres_especiais:
            lista_palavra.append(letra)
            ok = True
    while ok:
        sorteada = random.choice(lista_palavra)
        ok = False
    return sorteada

def normaliza (base_de_paises):
    base_de_paises_normalizada = {}
    qual_continente = {}
    saida = {}
    for continentes,paises in base_de_paises.items():
        for pais, dados in paises.items():
            dados['continente'] = continentes
            saida[pais] = dados
    return saida

    
