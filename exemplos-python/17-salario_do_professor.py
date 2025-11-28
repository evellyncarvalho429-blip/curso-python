
import os

os.system("cls")

print("Exemplo com While - Salário do Professor")

resposta = "Sim"

while(resposta == "Sim"):
   print("Qual é o seu níve: \n 1 - Nível 1 \n 2 - Nível 2 \n 3 - Nível 3")
    
   nivel = input("Informe o seu nível: ")



   qtd_aulas = int(input("Qual é sua qtd de aulas por semana: "))

   if nivel == "1":
       
     salario = (qtd_aulas * 12) 
   elif nivel == "2":
    salario = (qtd_aulas * 17) * 4
   elif nivel == "3":
    salario = (qtd_aulas * 25) * 4
   else:
    print("O nível digitado é invalido!")

   #Saída
   print(f"O seu salário será: {salario}")

   resposta = input("Deseja executar novamente? (sim ou não): ")

input("Precione <Enter> para finalizar")