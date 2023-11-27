print("Operadores Matemáticos")
print("Digite o valor do primeiro número... :")
numero_1 = int(input())
int(numero_1)
print("Digite o valor do segundo número...: ")
numero_2 = int(input())
int(numero_1)
resultado = 0
print("Escolha a operação desejada")
print("+ SOMA | - SUBTRAÇÃO | * MULTIPLICAÇÃO | / DIVISÃO")
operador = input()

match operador:
    case "+":
        resultado = numero_1 + numero_2
        print(f' {numero_1} + {numero_2} = {resultado}')
    case "-":
        resultado = numero_1 - numero_2
        print(f' {numero_1} - {numero_2} = {resultado}')
    case "*":
        resultado = numero_1 * numero_2
        print(f' {numero_1} x {numero_2} = {resultado}')
    case "/":
        resultado = numero_1 / numero_2
        print(f' {numero_1} / {numero_2} = {resultado}')
    case _:
        print("Operador inválido")
