print(30 * '~')
print('Atividade de voto obrigatório')
print(30 * '~')
idade = int(input('Digite a sua idade: '))
if idade <= 15:
    print('Voto recusado')
elif idade > 113:
    print('A sua idade esta fora do intervlo esperado')
elif idade >= 16 and idade < 18 or idade >= 65:
    print('O seu voto é facultativo')
elif idade >= 18:
    print('Voto obrigatório')