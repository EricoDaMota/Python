Alunos = [] 
Notas = []
for i in range(1,6):
    nome = (input("Digite o nome do aluno: "))
    Alunos.append(nome)
    nota = float(input("Digite a sua nota: "))
    Notas.append(nota)
print("\n----------REGISTRO DOS ALUNOS----------\n")
for i in range(5):
    print(f"{Alunos[i]} = {Notas[i]}")
print("\nFim do código...")
