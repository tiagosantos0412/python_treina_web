from cliente import Cliente
from pessoa import Pessoa

#Criando listas globais
Lista_pessoa = list()
Lista_passagem = list()
Lista_assentos_disponiveis = list(range(1, 43))  # Assentos numerados de 1 a 42

#Criando uma estrutura de repetição para exibir o menu
while True:
    print(100 * "=")
    print(" =                  Sistema de passagens - Terminal rodoviário de Santo André                      =")
    print(100 * "=")
    print(100 * "-")
    print("1. Cadastrar Pessoa | 2. Emitir Passagem | 3. Listar Pessoas | 4. Listar Passageiros | 5. Sair")
    print(100 * "-")
    opcao = int(input("Escolha uma opção.....: "))
    if opcao == 1:
        # Cadastro de uma pessoa
        nome = input("NOME: ")
        idade = int(input("IDADE: "))
        rg = input("RG: ")
        cpf = input("CPF: ")
        cep = input("CEP: ")
        rua = input("RUA: ")
        bairro = input("BAIRRO: ")
        cidade = input("CIDADE: ")
        estado = input("ESTADO: ")

        # Crie uma instância da classe Pessoa
        pessoa = Pessoa(nome, idade, rg, cpf, cep, rua, bairro, cidade, estado)

        # Adicione a instância da pessoa à lista de pessoas
        Lista_pessoa.append(pessoa)

    elif opcao == 2:
        # Escolha uma pessoa já cadastrada
        if not Lista_pessoa:
            print("Não há pessoas cadastradas.")
        else:
            print("Pessoas cadastradas:")
            for i, p in enumerate(Lista_pessoa):
                print(f"{i + 1}. {p.nome}")

            pessoa_selecionada = int(input("Escolha o número da pessoa: "))
            if 1 <= pessoa_selecionada <= len(Lista_pessoa):
                pessoa = Lista_pessoa[pessoa_selecionada - 1]

                p_viacao = input("VIAÇÃO: ")
                p_cidade_origem = input("ORIGEM: ")
                p_cidade_destino = input("DESTINO: ")
                p_data_ida = input("IDA: ")
                p_data_volta = input("VOLTA: ")
                # Mostrar apenas assentos disponíveis
                print("Assentos disponíveis:")
                for assento in Lista_assentos_disponiveis:
                    print(assento)
                assento_escolhido = int(input("Escolha um assento disponível: "))
                if assento_escolhido in Lista_assentos_disponiveis:
                    # Remover o assento escolhido da lista de asentos disponíveis
                    Lista_assentos_disponiveis.remove(assento_escolhido)
                    p_assento = assento_escolhido

                    # Crie uma instância da classe Cliente usando os atributos da pessoa
                    cliente = Cliente(pessoa, p_viacao, p_cidade_origem, p_cidade_destino, p_data_ida, p_data_volta, p_assento)
                    # Adicione a instância do cliente à lista
                    Lista_passagem.append(cliente)
                else:
                    print("Assento escolhido não está disponível!")
            else:
                print("Número de pessoa inválido.")
    elif opcao == 3:
        for pessoa in Lista_pessoa:
            print(pessoa)
    elif opcao == 4:
        for passagem in Lista_passagem:
            print(passagem)
    else:
        break