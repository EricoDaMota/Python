km = float(input('Digite os quilometros rodados pelo veículo: '))
day = int(input('Digite os dias de locação: '))
preco = (km * 60) + (day * 0.15)
print(f'O valor da locação foi: {preco:.2f}')