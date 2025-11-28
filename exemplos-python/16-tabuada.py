
import os

os.system("cls")

print("cls")

print("Exemplos - Calculando a Tabuada")

numero = int(input("Digite um número: "))

#Calcular ou incremento
i = 0
while (i <= 10):
    print(f"{numero} X {i} = {numero*i}")
    i+=1

print("O programa terminou")
input("Pressione a tela <enter> para finalizar...")