"""
5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""

def inverte(string_):
    indice = len(string_) - 1
    lista = []
    nova_palavra = ""

    for letra in string_:
        lista.append(letra)
        
    while indice >= 0:
        nova_palavra += lista[indice]
        indice -= 1

    print(nova_palavra)

inverte("ovo")
inverte("ana")
inverte("TUDO")