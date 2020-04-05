# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 19:32:11 2020

@author: Lucas
"""
alunos=['Maria', 'Joao', 'Mateus']
print(alunos)

# O programa cria um arquivo chamado disciplina.txt 
# modo w c(write) indica que os dados serão gravados
#CRIAR UM ARQUIVO
arq= open ("disciplina.txt","w")

arq.write('Universidade de Caxias do Sul\n')
arq.write('Área do Conhecimento de Ciências Exatas e Engenharias\n')
arq.write('Disciplina: Tópicos Especiais em Computação\n')

#'fecha' o arquivo indicando que ele não será mais utilizado
arq.close()

#LER UM ARQUIVO
arq= open("disciplina.txt","r")
texto = arq.read()
print(texto)
arq.close()
#################################################################

arq= open("notas.csv","w")

arq.write('Claudia;7;7;7;7\n')
arq.write('Fabio;6;6;6;6\n')
arq.write('Marcos;9;9;9;9\n')
arq.write('Patricia;8;8;8;8\n')
arq.close()

##Lê arquivo
arq= open("notas.csv","r")
#texto = arq.read()
#print(texto)
#arq.close()

linha = arq.readline()
#print(linhaprint(type(linha))

nome,nota1,nota2,nota3,media = linha.split(";")

print("Nome: ",nome)
print("Nota 1 :",nota1)
print("Nota 2 :",nota2)
print("Nota 3 :",nota3)
print("Media :",media)
arq.close()

print(type(nome))
print(type(nota1))
print(type(nota2))

print(float(nota1)+float(nota2))

print("Nome: ",nome)
print("Nota 1 :",nota1)
print("Nota 2 :",nota2)
print("Nota 3 :",nota3)

arq.close()



