
#! Sei que a questão 5 (A, B, C) não era mais obrigatória, fiz para adquirir conhecimento, não consegui termina-la no prazo final, contudo irei apresentar a solução até onde eu consegui fazer, contendo alguns(vários) erros de lógica. 

""" A) Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB de um país para um 
determinado ano. O programa solicita ao usuário o nome do país e o ano desejado. Caso o país solicitado ou 
o ano não sejam válidos, o programa deve informar, na saída, a mensagem: País não disponível ou Ano não disponível
a depender do tipo de dado não encontrado. Exemplo de saída do programa:
Informe um país: Brasil
Informe um ano entre 2013 e 2020: 2020
PIB Brasil em 2020: US$2.35 trilhões."""

import csv
import numpy

ano =list() 
pais = list()
indicePibs = list()
paises = list()
#abre o arquivo 
with open('PIBsmodelo.csv','r', encoding='utf8') as arquivo:
    dados = csv.reader(arquivo)
    pibs = list(dados)
    rotulos = pibs #cria lista de rotulos (paises/anos) remove primeiro item que se refere a países e deixa só os valores dos pibs.
    #rotulos = rotulos.split(',')
    #print(pibs)


    pais = input('Informe um país: ')
    ano  = int(input('Informe um ano entre 2013 e 2020: '))

    for x in pibs:
        listapibs = x.append(pibs) #gera lista
        #paises.append(listapibs[0]) #cria lista
        indicePibs.append(listapibs) #faz alinhamento de listas

    if pais in paises:    
        #print('passou aqui')
        indicePais = paises.index(pais) #pega indice do pais desejado.
    else:
        print('País não disponível.')

    if ano in rotulos:
        indiceAno = rotulos.index(ano)
    else:
        print('Ano não disponível.')

    if pais in paises and ano in rotulos:
        print(f'PIB {indicePais} em {ano}: U$$ {[indicePibs][indicePais][indiceAno-1]} trilhões.')





