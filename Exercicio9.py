"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""

palavra_secreta = "perfume"

letra_acertada = ""

while True:
    letra_digitada = input("Digite uma Letra: ")

    if len(letra_digitada) < 1:
        print("Digite apenas 1 letra.")
        continue

    if letra_digitada in palavra_secreta:
        letra_acertada += letra_digitada

    palavra_formatada = ""
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letra_acertada:
            palavra_formatada += letra_secreta
        else:
            palavra_formatada += "*"
    
    print(f"Palavra secreta {palavra_formatada}")