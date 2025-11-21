
import os 

os.system("cls")

#1 passo - Declarar variávais
valor_total = float(input("Digite valor total: "))
porcentagem = float(input("Digite a porcentagem a ser calculada: "))

#2 passo - Processamento
valor_parte = valor_total * (porcentagem / 100)

#3 passo - Mostra resultado
print(f"o valor a parte é de: {valor_parte} ")