
import os

os.system("cls")

print("""
██████████████████████████████████████████
█▄─▄─▀█─▄▄─█▄─▄███▄─▄▄─█─▄─▄─█▄─▄█▄─▀█▀─▄█
██─▄─▀█─██─██─██▀██─▄█▀███─████─███─█▄█─██
▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▀            """)

#Declarando variáveis
nome = input("Digita seu nome:")
nota1 = float(input("Digite sua primeira nota:"))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digita sua terceira nota: "))

#Calculado média
media = (nota1 + nota2 + nota3) / 3

#Mostrando a média
print(f"Sua média foi {round(media,2)}")

#Verificando se o aluno está aprovado
if media>= 7:
    print("Aprovado")

elif media>= 4:
    print("Em recuparação")

else:
    print("Reprovado")

input("Pressione qualquer <Enter> para fechar o programa.")