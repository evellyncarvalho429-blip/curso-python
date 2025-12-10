
import os

os.system("cls")

print("""
██████████████████████████████████████████
█▄─▄─▀█─▄▄─█▄─▄███▄─▄▄─█─▄─▄─█▄─▄█▄─▀█▀─▄█
██─▄─▀█─██─██─██▀██─▄█▀███─████─███─█▄█─██
▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▀            """)

resposta = "sim"

while(resposta == "sim"):

    os.system("cls")

    #Declarando variáveis
    nome = input("Digita seu nome:")
    nota1 = float(input("Digite sua primeira nota:"))
    nota2 = float(input("Digite sua segunda nota: "))
    nota3 = float(input("Digita sua terceira nota: "))

    #Calculado média
    media = (nota1 + nota2 + nota3) / 3

    situacao_do_aluno = ""

    #Mostrando a média
    print(f"Sua média foi {round(media,2)}")

    #Verificando se o aluno está aprovado
    if media>= 7:
        print("Aprovado")
        situacao_do_aluno = "Aprovado"

    elif media>= 4:
        print("Em recuparação")
        situacao_do_aluno = "Recuperação"

    else:
        print("Reprovado")
        situacao_do_aluno = "Reprovado"

    #Gravar os dados dos alunos
    with open("notas_dos_alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Narquivo.writeome do Aluno: {nome} \n")
        arquivo.write(f"Nota01: {nota1}\n")
        arquivo.write(f"Nota02: {nota2}\n")
        arquivo.write(f"Nota03: {nota3}\n")
        arquivo.write(f"Média do aluno: {media}\n")
        arquivo.write(f"Situação do Aluno: {situacao_do_aluno}\n")
        arquivo.write("===================================================")

        print("Dados salvos com sucesso!")

    resposta = input("Gostaria de executar novamente? sim ou não?:")

    os.system("cls")

input("Pressione qualquer <Enter> para fechar o programa.")
