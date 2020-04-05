# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:29:19 2020

@author: Lucas
"""
from random import randint

arq = open("notas.csv","w")

for i in range(100):
    arq.write('Aluno ' + str(i + 1) + ';' + 
              str(randint(1,10)) + ';' + 
              str(randint(1,10)) + ';' + 
              str(randint(1,10)) +'\n')
arq.close()

nomes = []
medias = []

## Setamos para zero a variavel, para quando for 
## incrementar não somar nulo com a média
media_total = 0
total_alunos = 0

##Lê arquivo
arq = open("notas.csv","r")

## Le o arquivo e calcula as medias
for i in range(100):
    linha = arq.readline()
    nome, nota1, nota2, nota3 = linha.split(";")
    
    media = 3 / ((1 / float(nota1)) + (1 / float(nota2)) + (1 / float(nota3)))

    nomes.append(nome)
    medias.append(media)
    
    media_total = media_total + media
    total_alunos = total_alunos + 1
## Sai do for    
    
## Fecha o arquivo
arq.close()

## Total de alunos definido pela quantidade de registros que leu no arquivo
#total_alunos = len(nomes)

## Calcula média aritmética
media_final = media_total / total_alunos

## Abre o arquivo de médias
arq = open("medias.txt","w")

for i in range(total_alunos):
    arq.write(str(nomes[i]) + ' - ' + str(medias[i]) + '\n')
    
arq.write("\nMédia turma - " + str(media_final))

arq.close()

