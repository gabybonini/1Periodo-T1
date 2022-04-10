'''                                  QUESTÃO 4
# A) Crie um programa que ponha a hipótese de Einstein à prova.
# B) Exiba um gráfico da evolução do valor acumulado, tendo como eixo das abscissas o número de períodos e, no eixo das ordenadas o valor acumulado em reais. 
'''

import matplotlib.pyplot as pl

valor = 0
aporte = 0 
periodo = 0
rendimento = 0

def juros(valor):
    for i in range(1,periodos+1):
   
        valor = round((valor+(valor*(rendimento/100))+aporte),2)
        print(f'Após {i} período(s), o montante será de R$ {valor:,}') 

        # Adiciona valores a lista que intregará o eixo Y
        listaValorY.append(valor)
        # Adiciona valores a lista que intregará o eixo X
        listaPeriodoX.append(i)

    # Determinando eixo X e Y do gráfico
    pl.plot(listaPeriodoX, listaValorY)
    pl.plot(label='EVOLUÇÃO DO MONTANTE')
    pl.xlabel('Períodos')
    pl.ylabel('Montante')
    pl.title('Hipótese de Einstein')
    pl.legend(loc='lower right') 
    pl.grid() #Mostra guias
   # pl.savefig('graficoQ4.png') #salva o gráfico
    pl.show() #Mostra o gráfico

valor = float(input(f'Valor do aporte inicial (R$): '))
rendimento = float(input(f'Rendimento por período (%): '))
aporte = float(input(f'Informe o aporte a cada período ($): '))
periodos = int(input(f'Informe o total de períodos: '))

listaPeriodoX = list()
listaValorY   = list()

juros(valor)
