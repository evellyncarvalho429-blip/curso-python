
import os

os.system("cls")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura*altura)

print(f"Seu IMC é: {round(imc,2)} ")