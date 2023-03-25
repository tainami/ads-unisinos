# Crie um programa que recebe a nota do Grau A e a nota do Grau B pelo teclado e imprime na tela se 
# será necessário ou não realizar o Grau C (considere o sistema de avaliação da Unisinos, 
# sendo o GA valendo 30% e o GB valendo 70%). Caso algum valor informado seja negativo, 
# informe uma mensagem de erro e não realize o cálculo.

nota1 = float(input("Digite sua nota no Grau A: "))
nota2 = float(input("Digite sua nota no Grau B: "))

notaMaxima = (nota1 * 30/100) + (nota2 * 70/100)

if nota1 < 0 or nota2 < 0:
    print("Erro")
elif notaMaxima >= 6:
    print("Não precisa realizar o Grau C")
else:
    print("Precisa realizar o Grau C")
