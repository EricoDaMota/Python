def par(x):
    return x % 2 == 0

def par_ou_impar(x):
    if par(x):
        return 'par'
    else:
        return 'impar'
    
valor = 0
while valor != 's':
    valor = input('Digite um valor ou "s" para sair: ')
    if valor != 's':
        print(par_ou_impar(int(valor)))  # Corrigido aqui
    else:
        print('Fim do programa')