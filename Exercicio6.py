"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input("Que horas são? ")
try:
    hora_float = float(hora_str)
    if (hora_float >= 0) and (hora_float <= 11):
        print("BOM DIA !!!!")
    elif (hora_float >= 12) and (hora_float <= 17):
        print("BOA TARDE!!!")
    elif (hora_float >= 18) and (hora_float <= 23):
        print("BOA NOITE!!!")
    else:
        print("Numero digita invalido, tente novamente.")
except:
    print("Digite uma hora correta")
