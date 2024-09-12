idade = int(input('Digite a sua idade: '))
if idade <= 15:
    print('Voto recusado')
elif idade >= 16 and idade >= 65:
    print('O seu voto é facultativo')
elif idade >= 18:
    print('Voto obrigatório')
else:
    print('A sua idade esta fora do intervalo esperado')
