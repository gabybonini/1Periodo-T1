#                                       QUESTÃO 2
#Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:
#Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
#Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
#Não tem direito a voto (menor de 16 anos).

# TODO: Fluxo de exceção: 
#O programa deve verificar se a idade da pessoa é maior do que zero.

def eleitor_idade(idade):
    #verifica voto facultativo.
    if (idade >= 16 and idade <18) or (idade >= 70):
        print(f'O seu direito de votar é faculdativo.') 

    #verifica voto obrigatório.
    elif idade >= 18 and idade < 70:
        print(f'O seu voto é obrigatório.')

    else:
        print(f'Você não tem direito ao voto.')  
        print('Compareça a uma junta eleitoral quando completar 16 anos!') 

idade = int(input('Informe sua idade: ')) 

if idade > 0:
    eleitor_idade(idade)

else:
    print('Idade inválida')
