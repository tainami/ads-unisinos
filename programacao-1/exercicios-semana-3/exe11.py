# Utilizando while, crie um programa que solicita para o usuário que ele digite 10 valores inteiros. Ao final, imprima a soma de todos os valores digitados. 


valores = []

while len(valores) < 10:
    valores.append(int(input("Digite um número: ")))
    
print("\nA soma é", sum(valores))
