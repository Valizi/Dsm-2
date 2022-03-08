from data.primos import primos
from data.lista_nomes import nomes
from time import time
#contador de comparações
comps = 0



def busca_binaria(lista, val):
    #"global" indica que estamos usando variavel que foi declarada fora da função
    global comps
    comps = 0
    ini = 0 #posição inicial da lista
    fim = len(lista) - 1 #posição final da lista

    while ini <= fim:
        meio = (ini + fim)// 2  #meio da lista


    #1º caso o valor na posição do meio da lista correspondente ao valor buscado;
    #  ENCONTRAMOS E retornamos a posição entrada (meio)

        if val == lista[meio]:
            comps += 1
            return meio

    #2º caso o valor de busca é maior que o valor no meio da lista

        elif val > lista[meio]:
            ini = meio + 1 

    # 3º  o valor de busca é menor que o valor do meio da lista

        else:
            fim = meio - 1 
    #val não exite na lista 
    return -1
#buscando numeros  primos
# hora_ini = time()
# print(f"Posição de 1487: {busca_binaria(primos ,1487)}")
# hora_fim = time ()
# print(f"Tempo gasto para buscar 1487:{hora_fim - hora_ini}")

# hora_ini = time ()
# print(f"Posição de 7683: {busca_binaria(primos,7603)}")
# hora_fim  = time ()
# print(f"Tempo gasto para buscar 7603:{hora_fim - hora_ini}")

# hora_ini = time ()
# print(f"Posição de 8008: {busca_binaria(primos,8008)}")
# hora_fim  = time ()
# print(f"Tempo gasto para buscar 8008:{(hora_fim - hora_ini)* 1000} ms")
hora_ini = time()
print(f"Posição de ORKUTILSON: {busca_binaria(nomes, ('ORKUTILSON'))}")
hora_fim = time()

hora_ini = time()
print(f"Tempo gasto para buscar ORKUTILSON: {(hora_fim - hora_ini) * 1000}ms")
hora_fim = time()

hora_ini = time()
print(f"Posição de FAUSTO: {busca_binaria(nomes, ('FAUSTO'))}")
hora_fim = time()

hora_ini = time()
print(f"Tempo gasto para buscar FAUSTO: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ZYON: {busca_binaria(nomes, ('ZYON'))}")
hora_fim = time()

hora_ini = time()
print(f"Tempo gasto para buscar ZYON: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ZULEICA: {busca_binaria(nomes, ('ZULEICA'))}")
hora_fim = time()

hora_ini = time()
print(f"Tempo gasto para buscar ZULEICA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Tempo gasto para buscar : {(hora_fim - hora_ini) * 1000}ms")



