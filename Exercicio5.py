"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

print("="*20)
print(f'{"PAR OU IMPAR": >16}')
print("="*20)
numero_str = input("Digite um numero inteiro: ")
print("="*20)
try:
    numero_int = int(numero_str)
    resto_da_divisao= numero_int % 2 

    if resto_da_divisao == 0:
        print("O numero digitado é PAR")
    else:
        print("O numero digitado é IMPAR")
except:
    print("Digite um numero inteiro.")
