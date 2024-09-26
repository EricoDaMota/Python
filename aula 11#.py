va = int(input('Digite o valor de a: '))
vb = int(input('Digite o valor de b: '))
vc = int(input('Digite o valor de c: '))
delta = (vb ** 2) - 4 * va * vc
if delta == 0:
    print('Não há rizes reais')
elif delta == 0:
    raiz = -vb / (2 * va)
    print(f'Raiz única: {raiz}')
else:
    baspo = (-vb + delta ** 0.5) / (2 * va)
    basne = (-vb - delta ** 0.5) / (2 * va)
    print(22 * '~')
    print(f'\n   {vb}² +- √{delta}')
    print(f'_________________')
    print(f'\n     2 x {va}   ')
    print(f'\nAs raízes são: {baspo} e {basne}')
    print(22 * '~')
