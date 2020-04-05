# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 17:43:49 2020

@author: Géssica  
"""

#2) Escreva um script em python que ordene em ordem crescente os elementos de cada linha de uma
#matriz M[6,6] de inteiros.

import random

matriz = [] 
linha = [] 

while len(matriz) != 5:
    x = random.randint(0,99) # Utilizei random para adicionar os valores
    linha.append(x) # Adiciono x à linha
    if len(linha) == 5: # Se a quantidade de elementos for igual à quantidade de colunas
        matriz.append(linha) # Adiciono a linha à matriz
        linha.sort()
        linha = [] # E zero a "linha" para adicionar outra à matriz

print(matriz)

