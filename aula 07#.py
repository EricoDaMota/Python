print(21 * '~')
print('|Calculadoura de imc|')
print(21 * '~')
peso = float(input('Digite  seu peso: '))
altura = float(input('Digite o sua altura: '))
imc = peso / (altura ** 2)
print('O valor do seu imc é {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc < 24.9:
    print('Peso normal')
elif imc < 34.9:
    print('Sobrepeso')
elif imc > 34.9:
    print('Acima do peso')
