"""
 Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor 
 sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
 escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de 
 Fibonacci e retorne uma mensagem avisando se o número informado pertence ou  não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

"""

[0, 1, 1, 2]

def fibo(num):
    a1 = 0
    a2 = 1

    fibo = [a1, a2]

    for _ in range(13):
        a3 = a1 + a2
        fibo.append(a3)

        a1 = a2
        a2 = a3


    print(fibo)
    if num in fibo:
        return 'O número se encontra na sequencia'
    
    else:
        return 'O número não se encontra na seguencia'


print(fibo(5))