
import os

os.system("cls")

print(""" 
██╗███╗░░░███╗░█████╗░
██║████╗░████║██╔══██╗
██║██╔████╔██║██║░░╚═╝
██║██║╚██╔╝██║██║░░██╗
██║██║░╚═╝░██║╚█████╔╝
╚═╝╚═╝░░░░░╚═╝░╚════╝░       """)

resposta = "sim"

while(resposta == "sim"):
    nome = input("Digite seu nome: ")
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = peso / (altura*altura)

    imc_dos_pacientes = ""

    print(f"Olá {nome}, seu IMC é: {round(imc,2)} ")

    #Abaixo do peso
    if imc <= 18.5:
        print("Você está abaixo do peso")
        imc_dos_pacientes = "Abaixo do peso"

    #Peso é normal
    elif imc >= 24.9:
        print("Peso normal")
        imc_dos_pacientes = "Peso normal"

    #Sobrepeso 
    elif imc <= 29.9:
        print("Sobrepeso")
        imc_dos_pacientes = "Sobrepeso"
        
    #Obesidade grau I
    elif imc <= 34.9:
        print("Obesidade Grau I")
        imc_dos_pacientes = "Obesidade Grau I"

    #Obesidade grau II
    elif imc <=39.9:
        print("Obesidade Grau II")
        imc_dos_pacientes = "Obesidade Grau II"

    elif imc >=40:
        print("Obesidade Grau III")
        imc_dos_pacientes = "Obesidade Grau III"

    #Gravar dados dos pacientes
    with open("imc_dos_pacientes.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Nome do Paciente: {nome} \n")
        arquivo.write(f"Peso: {peso}\n")
        arquivo.write(f"Altura: {altura}\n")
        arquivo.write(f"Imc do Paciente: {imc_dos_pacientes}")

        print("Dados salvos com sucesso!")

    resposta = input("Gostaria de executar novamente? sim ou não?:")

    os.system("cls")
    
input("Pressione <Enter> para fechar o programa. ")
