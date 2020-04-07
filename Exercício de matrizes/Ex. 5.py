# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 22:18:19 2020

"""

# **Desenvolva um script em python que cadastre os acidentes. O script deverá utilizar uma matriz
# 13X12. As linhas representaram as causas do acidente e as colunas os meses que os acidentes ocorreram:

# ** A tabela será atualizada pelos dados informados pelo usuário. O script deverá solicitar a
# quantidade de acidentes, o código da causa do acidente e o mês em que este acidente ocorreu:

# O script deverá desconsiderar causas de acidentes que não estejam na tabela ou meses
# inválidos. Caso um dos dados informados não for correto, este acidente não poderá ser atualizado.
# Se a causa e o mês do acidente forem informados corretamente, a matriz deverá ser atualizada
# colocando a quantidade de acidentes na célula correta da matriz (código é a linha da matriz e o mês
# a coluna da matriz).

# O script encerrará a leitura de valores quando o valor 0 for digitado no código do acidente.
# Esse valor não poderá ser contabilizado na matriz.
# Após todos os dados serem lidos e armazenados na matriz, eles devem ser gravados em um
# arquivo chamado “mortes.csv”.
# Antes de encerrar, o script deverá mostrar na tela:
# • a descrição (nome) dos tipos de acidentes que não ocorreram durante o ano.
# • a descrição (nome) e a quantidade de ocorrências do acidente que mais ocorreu no ano.

import numpy

nomes = [" 1 - Esmagamento",
         " 2 - Queda em altura",
         " 3 - Afogamento",
         " 4 - Choque objetos",
         " 5 - Soterramento",
         " 6 - Atropelamento",
         " 7 - Electrocussão",
         " 8 - Explosão",
         " 9 - Queda de nível",
         "10 - Intoxicação",
         "11 - Queda de pessoas",
         "12 - Outras formas",
         "13 - Em averiguação"]

# Matriz de acidentes
acidentes = []

# Inicializa acidentes
for i in range(len(nomes)):
    acidentes_mes = []

    for j in range(12):
        acidentes_mes.append(0)

    acidentes.append(acidentes_mes)

print(acidentes)

continua_acidente = 1

texto_sair = "(Informe ZERO para sair)"
texto_divisor = "##############################################"

while continua_acidente == 1:  # Mudar para tamanho da matriz 'a' que é 13
    print(texto_divisor)
    print("OLA GABI, BEM VINDA AO ACIDENTADUS")
    print(texto_divisor)
    for j in range(len(nomes)):
        print(nomes[j])

    print(texto_sair)

    codigo = int(input("Informe o código do acidente:"))

    # Código ZERO sai da opção
    if(codigo == 0):
        print(texto_divisor)
        print("Programa encerrado com sucesso!")
        continua_acidente = 0
    else:
        # Codigo 1 equiva a posição 0, por isso diminui 1
        codigo = codigo - 1

        continua_mes = 1

        # Lista dos acidentes por mes

        # Recebe os meses
        while continua_mes == 1:
            mes = 0
            grava_mes = 1

            print(texto_divisor)
            print(texto_sair)
            mes = int(input("Informe o número do mês do acidente:"))

            # Quando digitado 0, sai do input de meses
            if(mes == 0):
                continua_mes = 0
                grava_mes = 0

            # Se o mes for inválido
            if(mes < 0 or mes > 12):
                print(texto_divisor)
                print("Mês inválido")
                grava_mes = 0

            # Se for valido, grava o mes na matriz
            if(grava_mes > 0):
                # Mes 1 equivale a posição 0, por isso diminui 1
                mes = mes - 1

                print(texto_divisor)
                qtde = int(input("Informe a quantidade de acidentes:"))

                print(codigo)
                print(mes)
                acidentes[codigo][mes] = qtde

print(acidentes)


print(texto_divisor)
print("SETORES SEM ACIDENTES:")
print(texto_divisor)

# Gravar no arquivo
arquivo = open("mortes.csv", "w")

# For para percorrer os acidentes
for i in range(len(acidentes)):
    # Inicializa a linha, para poder concatenar
    linha = ""
    quantidade_acidentes = 0

    # For para percorrer os meses
    for j in range(len(acidentes[i])):
        quantidade_acidentes = quantidade_acidentes + acidentes[i][j]

        # Se for o ultimo mes, não coloca ponto e virgula
        if j == len(acidentes[i]):
            linha = linha + str(acidentes[i][j])
        else:
            linha = linha + str(acidentes[i][j]) + ';'

    if(quantidade_acidentes == 0):
        print(nomes[i])

    # Concatena a quebra de linha e grava no arquivo
    linha = linha + '\n'
    arquivo.write(linha)

# Finaliza o arquivo
arquivo.close()

print(texto_divisor)
print("SETOR COM MAIS ACIDENTES:")
print(texto_divisor)

maior_valor = 0
posicao = 0

for i in range(len(acidentes)):
    array_numpy = numpy.array(acidentes[i])
    total = array_numpy.sum()

    if(total > maior_valor):
        maior_valor = total
        posicao = i

print(nomes[posicao] + " - " + str(maior_valor) + " acidentes")
