"""C) Desenvolva uma função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos.
A função deve receber, como entrada, o nome de um país, e exibir o gráfico para todo o período listado na tabela.
O gráfico deve conter os valores do PIB no eixo das ordenadas (vertical) e os anos no eixo das abscissas (horizontal)
 """
import csv
import matplotlib as pl


with open('PIBsmodelo.csv','r', encoding='utf8') as arquivo:
    dados = csv.reader(arquivo)
    pibs = list(dados)
    #rolutos = pibs
    print(pibs)
    
#def graficoPib(PIBsmodelo):
    indicePais = list()
    indicePibs = list()
    pais = 0
    arquivo = pibs.split() #! split não funciona
    rotulos = pibs.pop(0)
    rotulos = rotulos.split(',')

    for j in pibs:
        listapibs = j.split(',')
        indicePibs.append(listapibs)

    indicePais.pop(15) #remove item vazio em países

    if pais in indicePais:
       paises = indicePais.index(pais)
       eixoY = list()
       for j in (indicePais[paises]): # 'for' irá colocar país escolhido no eixo Y 
           j = float (j) 
           eixoY.append(j)

       eixoX = pibs
       eixoX.pop(0) #retira palavra País, deixndo somente os anos.
       pl.plot(eixoX, eixoY) 
       pl.title(pais)
       pl.xlabel('Anos')
       pl.ylabel('PIB em trilhões de U$$')
       pl.show()
    else:
        print('País não disponível.')  






#pais = input('Informe um país: ')