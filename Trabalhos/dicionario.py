# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:50:35 2020

@author: Lucas
"""


#Os dicion�rios associam chaves a valores.
x = {'Christopher Brooks': 'brooksch@umich.edu', 'Bill Gates': 'billg@microsoft.com'}
x['Christopher Brooks'] # Recupere um valor usando o operador de indexa��o

x['Kevyn Collins-Thompson'] = None
x['Kevyn Collins-Thompson']

#Itere sobre todas as chaves:
for name in x:
    print(name)

for name in x.keys():
    print(name ,'-', x[name])

#Iterar sobre todos os valores:
for email in x.values():
    print(email)

#Itere sobre todos os itens da lista:
for name, email in x.items():
    print(name)
    print(email)