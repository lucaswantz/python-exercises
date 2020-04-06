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

linha = []
matriz = []

matrizresultado = []

i = 1

while i == 1:
    x = int(input("Digite o número da máquina:"))

    continua = 1

    if x < 0:
        print("Valor negativo! A leitura dos dados foi encerrada.")
        continua = 0
        i = 0
       
    for n in range(len(matriz)):
        if matriz[n][0] == x: #testar a variável
            print("Máquina já informada!")
            continua = 0

    if continua == 1:
        linha.append(x)
        for s in range (3): #Mudar para 15
            print("Digite Ruído",s)
            linha.append(int(input()))
        matriz.append(linha)
        linha = []         
    
for i in range(len(matriz)):
    qtde = 0
    total = 0
    
    for j in range(len(matriz[i])):        
        # Na coluna zero tem o codigo maquina
        if j > 0:
            qtde += 1
            total += matriz[i][j]
            
    media = total / qtde
            
    if media >= 85:
        linha = [] 
        # Codigo da maquina
        linha.append(matriz[i][0])
        # Media dos ruidos
        linha.append(media)
        
        if len(matrizresultado) > 0:
            for k in range(len(matrizresultado)):
                if matrizresultado[k][1] < media:
                    matrizresultado.insert(k, linha)        
        else:
            matrizresultado.append(linha)
    
    
for i in range(len(matrizresultado)):
    print('Máquina ', matrizresultado[i][0], ' com nível de ruído ', matrizresultado[i][1], 'dB.')
