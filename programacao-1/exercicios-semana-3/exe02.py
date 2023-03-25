# Crie um programa que recebe dois valores inteiros A e B pelo teclado 
# e imprime o valor de A dividido por B. Entretanto, se o valo de B for 0, 
# imprima uma mensagem de erro e não faça a divisão. 

valorA = int(input("Digite o primeiro valor: "))
valorB = int(input("Digite o segundo valor: "))

def somaValores(A, B):
    if B != 0:
        print("Resultado da divisão:", A / B)
    else: 
        print("Erro")

somaValores(valorA, valorB)
