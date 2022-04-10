def impressaoGasto (tipoCusto, percentualMax, custoTipo, rendaMensal):
    valorMax = calcularValorMax(custoTipo, rendaMensal)
    msg = definirDiagnostico(custoTipo, rendaMensal, percentualMax, valorMax)
    print(f'Diagnóstico: Seus gastos totais com {tipoCusto} comprometem {float(valorMax)} de sua renda total. O máximo recomendado é de {percentualMax}%.')

def calcularValorMax(custoTipo, rendaMensal):
    return (custoTipo * 100) / rendaMensal

def calculoNovoValorMax(rendaMensal, percentualMax):
    return (rendaMensal, percentualMax) / 100

def definirDiagnostico(custo, rendaMensal, percentualMax, valorMax):
    valorMax = calcularValorMax(custo, rendaMensal)
    msg = (f'Seus gastos estão dentro da margem recomendada')
    if valorMax > percentualMax:
        msg = (f'Portanto, o máxmo de sua renda comprometida com moradia deveria ser de R$ {float(calculoNovoValorMax(rendaMensal, percentualMax))}')

        return msg

percentualMaxMoradia    = 30
percentualMaxEducacao   = 20
percentualMaxTransporte = 15   

rendaMensal = float(input('Informe sua renda mensal: '))
custoMoradia = float(input('Informe gastos mensais com moradia: '))
custoEducacao = float(input('Informe gastos mensais com educação: '))
custoTransporte = float(input('Informe gastos mensais com transporte: ')) 

print('='*30)
print('DIAGNÓSTICO:')
print('='*30)
impressaoGasto('moradia', percentualMaxMoradia, custoMoradia, rendaMensal)
impressaoGasto('educação', percentualMaxEducacao, custoEducacao, rendaMensal)
impressaoGasto('transporte', percentualMaxTransporte, custoTransporte, rendaMensal)

