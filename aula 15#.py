n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
oper = int(input('Digite a operação desejada soma(1), subtração(2), multiplicação(3), divisão(4), potenciação(5), sair do programa(6): '))
if oper == 1:
    print(f'{n1} + {n2} = {n1 + n2}')
elif oper == 2:
    print(f'{n1} - {n2} = {n1 - n2}')
elif oper == 3:
    print(f'{n1} x {n2} = {n1 * n2}')
elif oper == 4:
    print(f'{n1} / {n2} = {n1 / n2}')
elif oper == 5:
    print(f'{n1} ** {n2} = {n1 ** n2}')
elif oper == 6:
    exit
else:
    print('Digite uma operação válida')