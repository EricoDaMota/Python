numero = int(input('Digite um número: '))
primo = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        primo += 1

if primo == 2:
    print(f'O número {numero} é primo.')
else:
    print(f'O número {numero} não é primo.')