# Utilizando for, crie um programa que imprime a tabuada de um número inteiro digitado pelo usuário.

n1 = int(input("Digite um número: "))

for n2 in range(11):
    print(f"{n1} x {n2} = {n1 * n2}")