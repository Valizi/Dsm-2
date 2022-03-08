#     ###################################################################################
# ################### BUSCA SEQUENCIAL ##############################################
# # procura por um valor na lista, partindo do primeiro elemento até o último,
# # Retorna: 

# # a) a posição do elemento, caso ele exista; ou 
# # b) -1 , se o elemento não existir 

nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]

from data.primos import primos #importando outro arquivo py
from time import time # biblioteca de cronometro do python
from data.lista_nomes import nomes
""" 
    Função que implementa a busca sequencial
    Procura por val dentro de lista
"""

def busca_sequencial(val, lista):
    for pos in range(len(lista)):
        # se encontra coincidencia, retorna posição
        if lista[pos] == val: return pos
    return -1 # nada encontrado

# #print(f"Posição de 27: {busca_sequencial(27, nums)}")
# #print(f"Posição de 40: {busca_sequencial(40, nums)}")

# #Buscando números primos
# hora_ini = time()
# print(f"Posição de 1487: {busca_sequencial(1487, primos)}") #tá chamando a função busca_sequencial e usando o parametro 1487, e o outro arquivo
# hora_fim = time() # armazenando 
# print(f"Tempo gasto para buscar 1487: {hora_fim - hora_ini}")
# print(25 * '-')

# hora_ini = time()
# print(f"Posição de 7603: {busca_sequencial(7603, primos)}")
# hora_fim = time()
# print(f"Tempo gasto para buscar 7603: {hora_fim - hora_ini}")
# print(25 * '-')

# hora_ini = time()
# print(f"Posição de 8008: {busca_sequencial(8008, primos)}")
# hora_fim = time()
# print(f"Tempo gasto para buscar 8008: {hora_fim - hora_ini}")
# print(25 * '-')

hora_ini = time()
print(f"Posição de EDUARDO: {busca_sequencial, ('ORKUTILSON', nomes)}")
hora_fim = time()

hora_ini = time()
print(f"Tempo gasto para buscar EDUARDO: {(hora_fim - hora_ini) * 1000}ms")
hora_fim = time()

# hora_ini = time()
# print(f"Posição de Julia: {busca_sequencial, ('Julia', nomes)}")
# hora_fim = time()

# hora_ini = time()
# print(f"Tempo gasto para buscar Julia: {(hora_fim - hora_ini) * 1000}ms")




