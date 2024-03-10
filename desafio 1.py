INDICE = 13
SOMA = 0
K = 0

def imprimir(SOMA, K, INDICE):
    while K < INDICE:

        K = K + 1;
        print(SOMA, K, INDICE)
        SOMA = SOMA + K;

        
    print(SOMA)

imprimir(SOMA, K, INDICE);


