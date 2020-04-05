# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
## 1) Na teoria de Sistemas define-se elemento mínimax de uma matriz, o menor elemento da linha
## em que se encontra o maior elemento da matriz. Escrever um script em python que lê uma matriz
## A(10,10) e determina o elemento mínimax desta matriz, escrevendo a matriz A e a posição do
## elemento mínimax
import numpy as np

a = np.array([[12,16,22,3,4,5,6,74,8,91], 
              [4,35,6,7,4,5,0,4,25,94], 
              [3,8,9,10,11,23,77,54,55,11],
              [20,1,2,3,4,51,66,7,8,9], 
              [4,5,56,7,4,0,8,4,75,9], 
              [3,83,9,10,11,23,77,42,55,47],
              [0,1,52,37,4,98,7,8,99,1], 
              [14,78,66,67,4,5,8,4,5,9],  
              [3,8,9,10,11,23,70,44,55,41],
              [4,5,6,7,4,55,8,42,5,95]])
print(a)

x = a.argmax()
        
print('\n O valor máximo desta matriz é =',a.max(), 'e se encontra na posição',x)

minmax=(a[6,0:10])
x = minmax.argmin()
resp = minmax.min()
print(minmax)
print('\n O valor mínimax desta matriz é =',resp, 'e se encontra na posição',x)