# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:25:57 2020

@author: Lucas
"""


#Matrizes - listas de listas

R = int(input('numero de linhas:'))
C = int(input('numero de colunas:'))

matrix = []

for i in range (R): #Para percorrer linhas
    a =[]
    #print(R,i)
    
    for j in range (C): #Para percorrer colunas
        print("coluuna",j)
        a.append(int(input()))
    matrix.append(a)
    
    print(matrix)
    
#Impressão da matrix
    
    for i in range(R):
        for j in range(C):
            print(matrix[i][j],end=' ')
        print()
        
#Impressão da matrix (substitui j por i) na hora de imprimir
    
    for i in range(R):
        for j in range(C):
            print(matrix[j][i],end=' ')
        print()