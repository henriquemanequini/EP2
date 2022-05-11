#sorteando paises
from math import *
import random 
from dadosnormalizados import DADOS

def sorteia_pais(DADOS):
    lista_paises = []
    for paises in DADOS.keys():
        lista_paises.append(paises)
    resposta_certa = random.choice(lista_paises)
    return resposta_certa
