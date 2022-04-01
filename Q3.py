#Em um concurso de fantasias, os jurados precisam digitar os nomes dos 5 participantes e suas respectivas notas, variando de 0 até 10. Crie uma função que leia os nomes dos participantes e, ao final, apresente apenas o nome e a nota do vencedor.

 # TODO: Fluxo de exceção: 
#O programa deve verificar se a nota da pessoa é maior ou igual a zero e menor ou igual a dez.

def fantasia(participantes):
    for vencedor in range(participantes):
        nome = input(f'Nome do participante: ')
        nota = float(input('Nota do participante: '))
        while nota < 0 or nota > 10:
            nota = float(input('Nota inválida. Deve estar entre 0 e 10.\nNota do participante: '))

        if vencedor==0:
            nome_vencedor = nome
            nota_vencedor = nota
        elif nota > nota_vencedor:
            nome_vencedor = nome
            nota_vencedor = nota
    
    print(f"O(A) vencedor(a) foi: {nome_vencedor}, com a nota {nota_vencedor}.")

# Chama a função
fantasia(5)


