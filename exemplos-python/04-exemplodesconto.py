
import os

os.system("cls")

#Declaração de variáveis do tipo real para permitir valores com casas decimais

preco_original = float(input("Digite o preço original do produto: "))

porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))

#Calcular o valor do desconto
valor_desconto = preco_original * (porcentagem_desconto /100)

#Calculando o preço final
preco_final = preco_original - valor_desconto

print(f"Valor do desconto: {valor_desconto} ")
print(f"Preço Final: {preco_final}")