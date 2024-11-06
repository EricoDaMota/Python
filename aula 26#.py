lista = []
for valor in range(1,6):
    valor = int(input("Digite um valor: "))
    lista.append(valor)
print(f'\nMenor valor = {min(lista)}')
print(f'Maior valor = {max(lista)}')
print(f'Soma da lista = {sum(lista)}')
print("\nFim do código...")