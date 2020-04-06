# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 20:43:29 2020

"""

import numpy as np

matriz_producao = [["1 - Laminadoras"    ],
                   ["2 - Extrusoras"     ],
                   ["3 - Impressoras"    ],
                   ["4 - Termoformagem 1"],
                   ["5 - Termoformagem 2"]]

matriz_scrap = [["1 - Laminadoras"    ],
                ["2 - Extrusoras"     ],
                ["3 - Impressoras"    ],
                ["4 - Termoformagem 1"],
                ["5 - Termoformagem 2"]]

matriz_geral = []
linha = []

for i in range(len(matriz_producao)):
                   
    print (matriz_producao[i][0])
    
    linha = []
    
    for j in range(12):

        print('Mes:', (j+1))
        producao = int(input("Digite a producao mensal: "))
        scrap = int(input("Digite o percentual de scrap mensal: "))
        
        pecas = producao * (scrap / 100) 
        linha.append(pecas)
        
    matriz_geral.append(linha)
        
array = np.array(matriz_geral)
    
for i in range(len(array)):
    print('Média anual de scrap do setor ', matriz_producao[i][0], ' é de ', array[i].mean(),
          ' com desvio padrão de ', array[i].std())
    


            

        