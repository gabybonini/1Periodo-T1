                                        #QUESTÃO 1
# Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais, considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.
# Ao usuário do programa serão solicitados o valor total do consumo, em reais, o número total de pessoas e o percentual do serviço prestado, entre 0 e 100

# TODO: Fluxo de exceção:

# verificar se o número total de pessoas é maior do que zero.
# verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100.
# para valores digitados inválidos, devem ser exibidos uma mensagem de erro "Valor inválido" e o programa deve ser interrompido.

#função que substitui pontos por virgula
def formatar_moeda(valor):
    a = '{:,.2f}'.format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    d = c.replace('v','.')
    return d

#tratamento de exceções
try:
    qtde_pessoas = int(input('Por favor, informe o total de pessoas: '))
    consumo = float(input('Informe o valor total do consumo: '))
    percentual = int(input('Informe o percentual do serviço, entre 0 e 100: '))

except (ValueError, TypeError):
    print('Valor inválido!\nRepita o processo novamente.')

except ZeroDivisionError:
    print('Não é possível dividir um numero por zero.')

else:
    floatvalor_total = float(consumo + percentual)
    valor_individual = floatvalor_total / qtde_pessoas

    print(f'O valor total da conta, com taxa de serviço, será de R$ ',formatar_moeda(floatvalor_total))
    print(f'Você informou que pagará ',percentual,'% pela taxa de serviço.')
    print(f'Dividindo a conta por' ,qtde_pessoas,'pessoas, cada pessoa deverá pagar R$',formatar_moeda(valor_individual))

finally:
    print('Volte sempre! Muito obrigado!!')    




