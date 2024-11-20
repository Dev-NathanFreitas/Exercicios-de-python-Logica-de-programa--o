"""
Neste exercicio pedimos para o usuário digitar dois numeros para assim utilizarmos a estrutura de conparação if, elif e else para ver qual valor é maior menor ou igual
"""

primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

primeiro_valor_float = float(primeiro_valor)
segundo_valor_floar = float(segundo_valor)

if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor=} é maior que {segundo_valor=}")
elif primeiro_valor == segundo_valor:
    print(f"{primeiro_valor=} é igual a {segundo_valor=}")
else:
    print(f"{segundo_valor=} é maior que {primeiro_valor=}")