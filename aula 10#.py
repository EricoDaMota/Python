ciga = int(input('Digite quantos cigarros você fuma por dia: '))
anos = int(input('Quantos anos você fuma: '))
fm = anos * 365 * (ciga * 10)
dias = (fm / 60) / 24
print(f'Você perdeu {dias:.2f} de vida')
