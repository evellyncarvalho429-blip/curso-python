import os

os.system("cls")

# #Definindo uma constante do python
# TAXA_CAMBIO = 5.50

# quantia_dolar = float(input("Digite o valor em dólares: "))
# TAXA_CAMBIO = float(input("Digite a taxa de cambio: "))
# valor_em_real = quantia_dolar * TAXA_CAMBIO
# print(f"O v alor convertido em reais é: R$ {valor_em_real:.2f}")

#Exemplo de criação de listas
numeros = [1,2,3,4,50]
nomes = ["Joaquim", "Maria", "Ana"]


print(nomes[0]) #Joaquim
print(nomes[1])
print(nomes[2])

print("Lista inicial")
print(nomes)

print("------------------------------------------------")

#Alterando um elemento da lista
nomes[0] = "Carlos"
print(f"Nome da posição 0: {nomes[0]}")

#Adicionar um novo elemento no final da lista
nomes.append("Roberval")
nomes.append("Ricardo")

#Adicionando um elemendo em uma posição  especifica da lista
nomes.insert(1, "Fernanda")


print(f"Listas Atualizada! ")
print(nomes)

#Removendo o elemento da posição 3 (Maria) da Lista
del nomes[3]

print("Lista atualizada após a remosção da Ana")
print(nomes)

#Removendo e retornando o elemento no indice 2
nome_removido = nomes.pop(2)
print(f"O nome removido foi: {nome_removido}")
print("Lista Atulizada após o POP")
print(nomes)

#Apagar os elmentos da lista
nomes.clear()
print("")