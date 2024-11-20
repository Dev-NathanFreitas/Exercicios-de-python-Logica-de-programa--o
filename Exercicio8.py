""" Calculadora com while """
while True:
    numero1_str = input("Digite um numero: ")
    numero2_str = input("Digite outro numero: ")
    operador = input("Digite o operador (+-/*): ")
    numeros_validos = None

    try:
        num_1_float = float(numero1_str)
        num_2_float = float(numero2_str)
        numeros_validos = True
    except Exception as error: # consigo capturar o erro
        numeros_validos = None
        print(error)

    if numeros_validos is None:
        print("Um dos numeros não é valido")
        continue

    operadores_permitidos = "+-/*"

    if operador not in operadores_permitidos:
        print("Operador digitado invalido")
        continue
    if len(operador) > 1:
        print("Digite apenas um operador")

    if operador == "+":
        soma = num_1_float + num_2_float
        print(f"{num_1_float} + {num_2_float} = {soma}")
    elif operador == "-":
        subtracao = num_1_float - num_2_float
        print(f"{num_1_float} - {num_2_float} = {subtracao}")
    elif operador == "*":
        multiplicacao= num_1_float * num_2_float
        print(f"{num_1_float} * {num_2_float} = {multiplicacao}")
    elif operador == "/":
        divisao = num_1_float / num_2_float
        print(f"{num_1_float} / {num_2_float} = {divisao}")
    else:
        print("Digite um operador correto")

    sair = input("Quer sair? [s]im: ").lower().startswith("s")
    
    if sair is True:
        break