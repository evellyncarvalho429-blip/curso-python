
import os

os.system("cls")

print("=== SALVANDO DADOS DO PRODUTO EM UM ARQUIVO ===\n")

nome_produto = input("Digite o nome do produto: ")
fabricante = input("Digie o fabricante: ")
categoria = input("Digite a categoria: ")
preco = float(input("Digite o preço do produto: "))

#Manipulando arquivos
#arquivo = open("produtos.txt", "a", encoding="utf-8")

with open("produto.txt", "a", encoding="utf-8" ) as arquivo:

    #Gravando as informações dentro do arquivo
    arquivo.write(f"Produto: {nome_produto} | Fabricante: {fabricante} | Categoria: {categoria} | Preço: {preco:.2f} \n")

#Não e necessario fechar mas esssa enquanto utilizado
#arquivo.close()

input("Pressione a tecla <Enter> para encerrar...")
