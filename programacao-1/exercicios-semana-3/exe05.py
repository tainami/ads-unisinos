# Crie um programa que solicita que o usuário digite uma letra e imprime na tela se a letra é uma vogal ou uma consoante.

letraQualquer = input("Digite uma letra: ")
letra = letraQualquer.upper()

if len(letra) > 1 or not letra.isalpha():
    print("Não é uma letra")
elif letra == "A" or letra == "E" or letra == "I" or letra == "O" or letra == "U":
    print(letra, "é uma vogal")
else:
    print(letra, "é uma consoante")
