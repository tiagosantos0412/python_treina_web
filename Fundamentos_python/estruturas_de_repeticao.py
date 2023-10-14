print("Estruturas de repetição")
##print("Calculo da tabuada \nDigite um número")
#numero = int(input())

#for i in range(0, 11):
#    resultado = numero * i
#    print(f'{numero} x {i} = {resultado}')
#else:
#    print(f'A tabuada do {numero} foi realizada com sucesso!')

print("CADASTRO DE USUÁRIOS")
usuarios = []

while True:
    print("Cadastre o código do usuário:")
    codigo_usuario = int(input())

    print("Cadastre o nome do usuário:")
    nome_usuario = input()

    print("Cadastre o email do usuário:")
    email = input()

    # Criar um dicionário para armazenar as informações do usuário
    usuario = {
        "codigo": codigo_usuario,
        "nome": nome_usuario,
        "email": email
    }

    usuarios.append(usuario)

    print("Deseja continuar? (s/n)")
    controle = input()
    if controle.lower() != "s":
        break

print("Usuário(s) cadastrado(s) com sucesso!")

# Exibir todos os usuários
for usuario in usuarios:
    print(f"Código: {usuario['codigo']}, Nome: {usuario['nome']}, Email: {usuario['email']}")