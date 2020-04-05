# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:18:28 2020

@author: Gessica Grolli
""" 

#CRIANDO E ACESSANDO LISTAS
vet = [11,22,33,44,55]
print (vet)
# Resposta: [11, 22, 33, 44, 55]
print (vet[0])
# Resposta: [11]
print (vet[1])
# Resposta: [22]
print (vet[2])
# Resposta: [33]
print (vet[5])
# Resposta: list index out of range
for x in range(0,5,1):
    print(vet[x])
# Resposta: [11, 22, 33, 44, 55]
for x in range(4,-1,-1):
    print(vet[x])
# Resposta: [55,44,33,22,11] 
    
#SE UM INCDICE POSSUI UM VALOR ENGATIVO, ELE CONTA AO CONTRÁRIO A PARTIR DO FINAL DA LISTA
    print(vet[-4])
# Resposta: [22]
    print(vet[-3])
# Resposta: [33] 
    print(vet[-2])
# Resposta: [44] 
engenharias=['Ambiental','Automotiva','Civil','Alimentos','Computação','Controle e Automação','Materiais','Produção','Elétrica','Eletrônica','Mecânica','Química']
print (engenharias[0])
# Resposta: Ambiental
print (engenharias[5])
# Resposta: Controle e Automação
for fruta in ["banana","abacaxi","laranja"]:
    print('Eu gosto de comer ' + fruta + 's!')
# Resposta:Eu gosto de comer bananas!
          #Eu gosto de comer abacaxis!
          #Eu gosto de comer laranjas!
lista=[]
print(lista)
# Resposta: []
print(vet,engenharias,lista)
# Resposta: [11, 22, 33, 44, 55] ['Ambiental', 'Automotiva', 'Civil', 'Alimentos', 'Computação', 'Controle e Automação', 'Materiais', 'Produção', 'Elétrica', 'Eletrônica', 'Mecânica', 'Química'] []

#COMPRIMENTO DE UMA LISTA
print(len(vet))
# Resposta: 5
print(len(engenharias))
# Resposta: 12
print(len(lista))
# Resposta: 0
for i in range(0,len(engenharias),1):
    print('Curso de ', engenharias[i])
# Resposta: Curso de  Ambiental
            # Curso de  Automotiva
            # Curso de  Civil
            # Curso de  Alimentos
            # Curso de  Computação
            # Curso de  Controle e Automação
            # Curso de  Materiais
            # Curso de  Produção
            # Curso de  Elétrica
            # Curso de  Eletrônica
            # Curso de  Mecânica
            # Curso de  Química

#CONCATENAÇÃO E MULTIPLICAÇÃO
a=[1,2,3]
b=[4,5,6]
c= a+b
print(c)
# Resposta: 37
a=[100]
print(a)
a=a*4
print(a)
# Respostas: [100]
            #[100, 100, 100, 100]
b=[3,5,7,9]
print(b)
b=b*3
print(b)
# Respostas: [3, 5, 7, 9]
            #[3, 5, 7, 9, 3, 5, 7, 9, 3, 5, 7, 9]

#VERIFICANDO A EXISTÊNCIA DE ITENS EM UMA LISTA
print ('Computação' in engenharias)
# Resposta: True
print ('xxxx' in engenharias)
# Resposta: False

#VALORES MÍNIMOS,MÁXIMO E SOMA
numeros = [14,55,67,89,88,10,21,5]
print(min(numeros))
# Resposta: 5
print(max(numeros))
# Resposta: 89
print(sum(numeros))
# Resposta: 349

#FATIAMENTO E TROCA DE ITENS DE LISTAS
lista=['a','b','c','d','e','f']
print(lista[1:3])
# Resposta: ['b', 'c']
print(lista[:4])
# Resposta: ['a', 'b', 'c', 'd']
print(lista[3:])
# Resposta:['d', 'e', 'f']
print(lista[:])
# Resposta:['a', 'b', 'c', 'd', 'e', 'f']
lista=['a','b','c','d','e','f','g','h','i']
a=lista[4:7]
print (a)
# Resposta: ['e', 'f', 'g']
b=lista[:4]
print (b)
# Resposta: ['a', 'b', 'c', 'd']
c=lista[3:]
print (c)
# Resposta: ['d', 'e', 'f', 'g', 'h', 'i']
fruta=["banana","abacaxi","laranja"]
print(fruta)
# Resposta:['banana', 'abacaxi', 'laranja']
fruta[0]='abacate'
print(fruta)
# Resposta:['abacate', 'abacaxi', 'laranja']
fruta[-1]='tangerina'
print(fruta)
# Resposta:['abacate', 'abacaxi', 'tangerina']
lista=['a','b','c','d','e','f']
lista[1:3]=['x','y']
print(lista)
# Resposta:['a', 'x', 'y', 'd', 'e', 'f']
lista[1:3]=[]
print(lista)
# Resposta:['a', 'd', 'e', 'f']
lista= ['a', 'd', 'f']
print(lista)
# Resposta:['a', 'd', 'f']
lista[1:1]=['b','c']
print(lista)
# Resposta:['a', 'b', 'c', 'd', 'f']
lista[4:4]=['e']
print(lista)
# Resposta:['a', 'b', 'c', 'd', 'e', 'f']

#MÉTODOS DAS LISTAS
#append() - adicionar 1(UM) novo alemento ao final da lista
livros=['Java','SqlServer','Delphi','Python']
print(livros)
# Resposta:['Java', 'SqlServer', 'Delphi', 'Python']
livros.append('Android')
print(livros)
# Resposta:['Java', 'SqlServer', 'Delphi', 'Python', 'Android']

#insert()  - adicionar um elemento em determinada posição
livros.insert(0,'Oracle')
print(livros)
# Resposta:['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android']

#extend(lista) - Acrescenta os elementos (VÁRIOS) da lista ao final de uma lista já existente
livros.extend(['Django','C#'])
print(livros)
# Resposta:['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android', 'Django', 'C#']

#pop() - remove o último da lista ou de um determinado item(infomrando a posição do elemento na lista).
#Como resultado da operação, mostra o item removido
print(livros)
# Resposta:['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Android', 'Django', 'C#']
print(livros.pop())
# Resposta:C#
print(livros.pop( 1))
# Resposta:Java

#Remove(elemento) - remove a primeira ocorrência do elemento passado como parâmetro
print(livros)
# Resposta:['Oracle', 'SqlServer', 'Delphi', 'Python', 'Android', 'Django']
livros.remove('Python')
print(livros)
# Resposta:['Oracle', 'SqlServer', 'Delphi', 'Android', 'Django']

#sort() - ordena a lista em ordem crescente para números e em ordem lexicográfica para strings
#reverse() - inverte as posições dos elementos
#count() - retorna o número de ocorrência do elemento passado como parâmetro

livros = ['Oracle', 'Java', 'SqlServer', 'Delphi', 'Python', 'Oracle']
livros.reverse()
print(livros)
# Resposta:['Oracle', 'Python', 'Delphi', 'SqlServer', 'Java', 'Oracle']

livros.sort()
print(livros)
# Resposta:['Delphi', 'Java', 'Oracle', 'Oracle', 'Python', 'SqlServer']

print(livros.count('Oracle'))
# Resposta:2

#index(elemento) - retorna o índice da primeira ocorrência de elemento na lista
print(livros.index('Python'))
# Resposta: 4


















