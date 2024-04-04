print("----------------------------")
print(" VENDA DE MAÇÃS DO TERCEIRÃO")
print("----------------------------")

print ('''
-------- TABELA --------
Até 12 Maçãs: R$0,30
Acima de 12 Maças: R$0,25
------------------------
''')

quantidade_macas = int(input("Quantas maçãs você deseja comprar?"))

if quantidade_macas <= 12:
    preco = 0.30 * quantidade_macas

elif quantidade_macas > 12:
    preco = 0.25 * quantidade_macas

valor_final = quantidade_macas * preco

print("--------------------------------")
print(f"O preço final ao comprar {quantidade_macas} maças será R${preco}")

