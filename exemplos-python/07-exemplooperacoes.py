
import os

os.system("cls")

#1 passo - Declarar variáveis
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

#2 passo - Processamento
soma = valor1 + valor2
sub = valor1 - valor2
multi = valor1 * valor2
div = valor1 / valor2

#3 passo - Mostra resultado
print(f"Soma: {soma} Sub: {sub} Multi: {multi} Div: {div} ")
