
import os

os.system("cls")

try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero

except ZeroDivisionError:
    print("Erro: não é possivel dividir por zero.")

except ValueError:
    print("Error: você não digitou um número válido.")

else:
    #Executa apenas se **nenhuma exceção** tiver ocorrido
    print(f"O resultado da divisão é: {resultado}")

finally:
    #Executa sempre, independente de erro ou sucesso
    print("Encerrando a operação...")
