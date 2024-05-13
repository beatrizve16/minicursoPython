#Faça um programa que receba 5 valores e Adicionar esses valores na lista e depois mostrarr a quantidade de valores armazenado na lista e imprimir a lista
# Cria uma lista vazia para armazenar os valores
numeros = []

for i in range(5):
    num = float(input("Digite um numero:"))
    numeros.append(num)

quantidade = len(numeros)
print("Quantidade de numeros na lista:" , quantidade)

print("numeros na lista:")
for num in numeros:
    print(num)
