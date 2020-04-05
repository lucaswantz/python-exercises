# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:54:05 2020
@author: Gessica
"""

#3) Uma empresa está preocupada com o nível de ruído de suas máquinas e precisa verificar quais
#máquinas excedem a 85 dB ( valor máximo permitido pelas Normas Regulamentadoras brasileiras).

#Faça um script que lê o código de uma máquina e quinze medições de ruído desta máquina,

#armazenando estes valores em uma matriz (coluna 1 – código da máquina colunas 2 a 11 – medida do ruído. 

#O script não deverá permitir a entrada de códigos de máquinas iguais e deverá encerrar a
#leitura dos dados quando valor negativo for informado no código da máquina.

#Após, deve calcular a média dos ruídos de cada máquina, armazenando em uma segunda
#matriz o código da máquina e a média de ruído das máquinas que possuírem ruído superior a 85dB.

#Mostrar um relatório das máquinas que ultrapassaram os 85db, em ordem decrescente de ruído.
#No final, o script deverá apresentar um relatório com o seguinte formato:

linha=[]
matriz = []
for i in range (2):
    x = int(input("Di9gite o número da máquina:"))
    
    for n in range(i):
        if x == 999: #testar a variável
            print("Máquina já informada!")
            
        elif x < 0:
            print("Valor negativo! A leitura dos dados foi encerrada.")
   # else:
    linha.append(x)
    for s in range (3): #Mudar para 15
        print("Digite Ruído",s)
        linha.append(int(input()))
    matriz.append(linha)
    linha = [] 

print('test',matriz)

for i in range (R): #Para percorrer linhas
    a =[]
    #print(R,i)
    
    for j in range (C): #Para percorrer colunas
        print("coluuna",j)
        a.append(int(input()))
    matrix.append(a)
    
    print(matrix)
    
    
  
linhab = []
for i in range (2):
    matrizb = matriz[i][0]
    print('test2',matrizb)
    linhab.append(matrizb)
    for j in range (3): #Mudar para 15
        matrizb = matriz[0][j]
        linhab.append(matrizb)
    matrizb.append(linhab)
    linhab = []

