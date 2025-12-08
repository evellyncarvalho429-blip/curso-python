
import os

#Lista que armazena todos os clientes
lista_de_clientes = [
    {
        "nome": "Ana Silva",
        "idade": 28,
        "email": "ana.silva@example.com",
        "celular": "(11) 91234-5678"
    },
    {
        "nome": "Bruno Marques",
        "idade": 35,
        "email": "bruno.marques@example.com",
        "celular": "(21) 99876-5432"
    },
    {
        "nome": "Carla Ferreira",
        "idade": 42,
        "email": "carla.ferreira@example.com",
        "celular": "(31) 98765-4321"
    },
    {
        "nome": "Diego Rocha",
        "idade": 30,
        "email": "diego.rocha@example.com",
        "celular": "(41) 99555-1122"
    },
    {
        "nome": "Elisa Andrade",
        "idade": 25,
        "email": "elisa.andrade@example.com",
        "celular": "(51) 99111-2233"
    }
]

#Função que limpar a tela
def limpar_tela():
    os.system("cls")

#Fuñção que exibe  o menu na tela
def exibir_menu():
    print("\n=== Menu Principal ===")
    print('[1] - Cadastro de Clientes')
    print('[2] - Listar Clientes Cadastrados')
    print('[3] - Editar Dados de Clientes')
    print('[4] - Excluir um Cliente')
    print('[5] - Sair do Sistema \n')

#Função que volta ao menu principal
def voltar_ao_menu_principal():
    input("\nPressione <Enter> para voltar ao menu inicial...")
    main()

#Função que cadastrar um novo cliente
def cadastrar_novo_cliente():
    try:
        #Chamando a função que limpa a tela
        limpar_tela()
        print("=== CADASTRO DE NOVO CLIENTE ===\n")

        #Solicitando os dados do cliente
        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        email = input("Digite o e-mail do cliente: ")
        celular = input("Digite o celular do cliente: ")

        #Agrupando os dados do clientes
        dados_cliente = {
            'nome': nome,
            'idade': idade,
            'email': email,
            'celular': celular
        }

        #Adicionar a cliente na lista 
        lista_de_clientes.append(dados_cliente)

        #Exibindo mensagem de successo
        print(f"\n O Cliente {nome} foi cadastrado com sucesso!")

    except:
        print("A idade deve ser um número")

    finally:
        #Voltar para o menu principal
        voltar_ao_menu_principal()

#Função que listra todos os clientes cadastrados
def listrar_clientes_cadastrados():
    #chamando a função que limpa a tela
    limpar_tela()
    print("=== LISTA DE CLIENTES CADASTRADOS ===\n")

    #listandoos clientes
    for cliente in lista_de_clientes:
        print(f"Nome: {cliente['nome']} | Idade: {cliente['idade']}  | E-mail: {cliente['email']} | Celular: {cliente['celular']}")
    
    #Voltar para o menu principal
    voltar_ao_menu_principal()

#Função que exclui um cliente cadastrado
def excluir_cliente():

    #Chamando a função que limpa a tela
    limpar_tela()
    print("=== REMOVER CLIENTE ===\n")

    #indice = 0

    #Listando os clientes cadastrados
    for indice, cliente in enumerate (lista_de_clientes):
        print(f"Indicie: {indice} | Nome: {cliente['nome']} | Idade: {cliente['idade']}  | E-mail: {cliente['email']} | Celular: {cliente['celular']}")
        indice += 1
    try:
        #Solicitar ao usuario o indice para remover
        indice = int(input("\nDigite o indice do cliente que deseja remover:  "))

        if indice >= 0 and indice < len (lista_de_clientes):
        #Excluir o cliente escolhido
        cliente_removido = lista_de_clientes.pop(indice)

        print(f"\n Cliente {cliente_removido['nome']} removido com sucesso! ")
        else:
            print("Indice inválido")

    except:
        print("Digite o indice válido")

    finally:
    #Voltar ao menu principal
    voltar_ao_menu_principal()

#Função para editar um usuário
def editar_dados_clientes():
    limpar_tela()
    print("=== EDITAR DADOS DO CLIENTE ===\n")

    #Listando os clientes cadastrados
    for indice, cliente in enumerate (lista_de_clientes):
        print(f"Indicie: {indice} | Nome: {cliente['nome']} | Idade: {cliente['idade']}  | E-mail: {cliente['email']} | Celular: {cliente['celular']}")
        indice += 1

    try:
        #Solicitar ao usuario o indice para remover
        indice = int(input("\nDigite o indice do cliente que deseja editar:  "))

        if indice >= 0 and indice < len(lista_de_clientes):

            #Capeturar os dados do cliente selecionado
            dados_do_cliente = lista_de_clientes[indice]

            #Exibindo os dados do cliente selecionado 
            print(f"\n Editando os dados dos clientes: {dados_do_cliente['nome']} ")

            #Solicitando os novos dados
            novo_nome = input(f"Digite o novo nome: (Atual - {dados_do_cliente['nome']}: ")
            nova_idade = input(f"Digite a nova idade: (Atual - {dados_do_cliente['idade']}: ")
            novo_email = input(f"Digite o novo e-mail: (Atual - {dados_do_cliente['email']}: ")
            novo_celular = input(f"Digite o novo celular: (Atual - {dados_do_cliente['celular']}:")

            #Editar
            dados_do_cliente['nome'] = novo_nome
            dados_do_cliente['idade'] = nova_idade
            dados_do_cliente['email'] = novo_email
            dados_do_cliente['celular'] = novo_celular
            print("\nDados Atualizados com sucesso!")

    except:
        print("Idade ou indice devem ser váçidos")
        
    finally:
    voltar_ao_menu_principal()

#Função Principal do meu programa
def main():
    #Chamar função de limpar a tela
    limpar_tela()
    print("Bem vindo ao Gerenciador de Clientes")

    #Chamar a função que exibe o menu
    exibir_menu()

    #Solicitando uma opção´para o usuario
    opcao = int(input('Escolha uma opção: '))

    #Verificando qual foi a opção escolhida
    if opcao == 1:
        #Abrir o cadastro de um novo cliente
        cadastrar_novo_cliente()

    elif opcao == 2:
        #Abrir a listagem de clientes cadastrados
        listrar_clientes_cadastrados()

    elif opcao == 3:
        #Abrir a edição de clientes
        editar_dados_clientes()

    elif opcao == 4:
        #Abrir a exclusão de um cliente
        excluir_cliente() 
    
    elif opcao == 5:
        exit("Precione <enter> para encerrar o programa... s")

    else:
        print("Opção Inválida!")

#Chamando a função principal
main()