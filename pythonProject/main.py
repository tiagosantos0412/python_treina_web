from cachorro import Cachorro
from gato import Gato
from dono import Dono

Lista_cachorro = list()
Lista_gato = list()

while True:
    print(90*"-")
    print("1. Cadastrar usuário | "
          "2. Cadastrar cachorro | "
          "3. Cadastrar gato | "
          "4. Listar cachorros\n"
          "5. Listar gatos | "
          "6. Brincar cachorros | "
          "7. Brincar gatos | "
          "8. Sair")
    print(90*"-")
    opcao = int(input("Escolha uma opção...: "))
    global dono
    if opcao == 1:
        nome_usuario = input("Digite o nome do usuário: ")
        dono = Dono(nome_usuario)
    elif opcao == 2:
        nome_cachorro = input("Digite o nome do cachorro: ")
        idade_cachorro = input("Digite a idade do cachorro: ")
        cor_cachorro = input("Digite a cor do cachorro: ")
        raca_cachorro = input("Digite a raca do cachorro: ")
        qtd_brinquedos = input("Digite a quantidade de brinquedos do cachorro: ")
        cachorro = Cachorro(nome_cachorro, idade_cachorro, cor_cachorro, raca_cachorro, qtd_brinquedos, dono=dono)
        Lista_cachorro.append(cachorro)
    elif opcao == 3:
        nome_gato = input("Digite o nome do gato: ")
        idade_gato = input("Digite a idade do gato: ")
        cor_gato = input("Digite a cor do gato: ")
        raca_gato = input("Digite a raca do gato: ")
        qtd_bolinhas = input("Digite a quantidade de bolinhas do gato: ")
        gato = Gato(nome_gato, idade_gato, cor_gato, raca_gato,  qtd_bolinhas, dono=dono)
        Lista_gato.append(gato)
    elif opcao == 4:
        for cachorro in Lista_cachorro:
            print(cachorro)
    elif opcao == 5:
        for gato in Lista_gato:
            print(Lista_gato)
    elif opcao == 6:
        for cachorro in Lista_cachorro:
            print(cachorro.brincar())
            if cachorro.felicidade >= 6:
                print(cachorro.emitir_som())
    elif opcao == 7:
        for gato in Lista_gato:
            print(gato.brincar())
            if gato.felicidade >= 6:
                print(gato.emitir_som())
    else:
        break