# Crie um programa que permita que o usuário crie sua lista de compras. Primeiramente, 
# solicite que ele informe quantos produtos serão adicionados na lista. 
# Depois disto, peça para que o usuário digite os produtos que ele vai comprar, 
# e armazene em uma lista. Ao final, imprima a lista de compras do usuário.

listaCompras = []
quantidadeItens = int(input("Informe a quantidade de itens: "))

while len(listaCompras) < quantidadeItens:
    listaCompras.append(input("Digite o produto: "))

print("Sua lista:", listaCompras)