print("****************************************************************************")
print("*                    COMPANHIA DE VIAGENS JC                               *")
print("****************************************************************************")
clientes = []
passagem = []


#Função para realizar o cadastro do cliente
def cadastro():
    contador = 0
    print("Nome completo: ")
    nome = input()
    print("Idade: ")
    idade = int(input())
    print("RG: ")
    rg = input()
    print("CPF: ")
    cpf = input()
    print("Rua: ")
    rua = input()
    print("Bairro: ")
    bairro = input()
    print("Cidade: ")
    cidade = input()
    print("Estado: ")
    estado = input()

    # Criar um dicionário para armazenar as informações do cliente
    cliente = {
        "nome": nome,
        "idade": idade,
        "rg": rg,
        "cpf": cpf,
        "rua": rua,
        "bairro": bairro,
        "cidade": cidade,
        "estado": estado,
        "contador": contador
    }
    clientes.append(cliente)
    menu()


#Função para verificar a idade do passageiro
def verificar_idade(clientes):
    idade = clientes['idade']
    idade = int(idade)
    if 16 <= idade < 18:
        mensagem = (
            f"O passageiro {clientes['nome']} tem {idade} anos e será necessário uma autorização dos responsáveis para viajar")
    elif idade >= 18:
        mensagem = "Imprimindo passagem..."
    return mensagem
#Função para realizar a compra da passagem
def emitir_passagem(clientes):
    for cliente in clientes:
        passageiro = cliente['nome']
        idade = cliente['idade']
        print("Data de ida: ")
        data_ida = input()
        print("Data de volta: ")
        data_volta = input()
        print("Cidade de origem: ")
        cidade_origem = input()
        print("Cidade de destino: ")
        cidade_destino = input()
        print("Poltrona: ")
        poltrona = input()
        observacao = verificar_idade(cliente)

        compra = {
            "passageiro": passageiro,
            "idade": idade,
            "data_de_ida": data_ida,
            "data_de_volta": data_volta,
            "cidade_de_origem": cidade_origem,
            "cidade_de_destino": cidade_destino,
            "poltrona": poltrona,
            "observacao": observacao
        }
        passagem.append(compra)

    imprimir_passagem(passagem)

#Função para imprimir a passagem comprada
def imprimir_passagem(passagem):
    for p in passagem:
        print(f"Viação JC\n"
              f"Passageiro.....: {p['passageiro']}\n"
              f"Idade..........: {p['idade']}\n"
              f"Data da ida....: {p['data_de_ida']}\n"
              f"Data da volta..: {p['data_de_volta']}\n"
              f"Origem.........: {p['cidade_de_origem']}\n"
              f"Destino........: {p['cidade_de_destino']}\n"
              f"Poltrona.......: {p['poltrona']}\n"
              f"Observação.....: {p['observacao']}")


#Função para conferir os dados cadastrados
def consulta(clientes):
    for clientes in clientes:
        print(f"Nome: {clientes['nome']}, Idade: {clientes['idade']}, RG: {clientes['rg']}, CPF: {clientes['cpf']},"
              f"Rua: {clientes['rua']}, Bairro: {clientes['bairro']}, Cidade: {clientes['cidade']}, Estado: {clientes['estado']}")
    menu(clientes)

#Menu ou função principal do programa
def menu():

    print("Escolha o módulo desejado... 1: Cadastro | 2: Emitir passagem | 3: Consultar | 4: Sair")
    opcao = int(input())
    if opcao == 1:
        cadastro()
    elif opcao == 2:
        emitir_passagem(clientes)
    elif opcao == 3:
        consulta(clientes)
    elif opcao == 4:
        print("Saindo do sistema")
    else:
        print("Opção inválida!")

menu()