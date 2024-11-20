"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
lista_de_compras = []

while True:
    print("="*20)
    print("LISTA DE COMPRAS")
    print("="*20)
    print("Selecione uma opção")
    escolha = input("[i]nserir [a]pagar [l]istar: ").lower()
    print("="*20)

    escolhas_possiveis = "ial"

    if escolha not in escolhas_possiveis or len(escolha) > 1:
        os.system("cls")
        print("="*20)
        print("Escolha não disponivel tente novamente")
        print("="*20)
        continue
    
    if escolha == "i":
        item_adicionado = input("Digite o item que deseja adicionar na lista: ").lower()
        if item_adicionado in lista_de_compras:
            print("ITEM JA ADICIONADO NA LISTA TENTE DENOVO")
        else:
            lista_de_compras.append(item_adicionado)
        print("ITEM ADCIONADO A LISTA COM SUCESSO!!!")
    elif escolha == "l":
        print("="*20)
        print("ITENS DA LISTA")
        print("="*20)
        for indice,item in enumerate(lista_de_compras):
            print(indice,item)
    elif escolha == "a":
        item_apagar = input("Digite o item que deseja excluir da lista ").lower()
        if item_apagar in lista_de_compras:
            for indice,item in enumerate(lista_de_compras):
                if item_apagar == item:
                        lista_de_compras.pop(indice)
                        print("ITEM APAGADO DA LISTA COM SUCESSO")
        else: 
            print("item que deseja excluir não esta na lista.")