lista = [7, 4, 2, 6, 8, 3, 9, 1, 5, 8]

# #acha o meio da lista

# meio = len(lista) // 2

# #fatiamento de lista

# metade1 = lista[0:meio]
# metade2 = lista[meio:]

# print(f'Meio: {meio}')
# print(f'lista: {lista}')
# print(f'metade 1 {metade1}')
# print(f'metade 2: {metade2}')


####### fatiamento de lista###############


#Algoritimo de ordenação merge sort

# #No processo de ordenação, esse algoritimo 'desmonta' o vetor original
# contendo n elementos até obter  n vetores de apenas um elemtento cada um.
# em seguida, usando a tecnica de mesclagem (merge), 'remonta' o vetor,
# dessa vez com os elementos ja em ordem
import tracemalloc
from nomes_desord import nomes
from time import time
divs = 0
juncoes =0 
comps = 0
def merge_sort(lista):
    global divs, juncoes, comps

    # print(f"Lista recebida: {lista}")

    # Só continua se o comprimento da lista for maior que 1
    if len(lista) <= 1: return lista

    # Encontra a posição do meio da lista
    meio = len(lista) // 2

    # Cópia da primeira metade do vetor
    sublista_esq = lista[:meio]
    # Cópia da segunda metade do vetor
    sublista_dir = lista[meio:]
    divs +=1
    # Chamamos recursivamente a função para que ela continue
    # repartindo cada uma das sublistas em metades
    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    # AQUI COMEÇA A JUNÇÃO DAS DUAS METADES DA LISTA, ORDENADAMENTE
    pos_esq = pos_dir = 0
    ordenada = []   # Lista vazia

    # Compara os elementos da sublista entre si e insere na
    # lista ordenada o que for menor
    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):
        # O elemento que se encontra na posição da sublista esquerda
        # é menor que o que se encontra na posição da sublista direita
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            ordenada.append(sublista_esq[pos_esq])
            pos_esq += 1
        # O contrário
        else:
            ordenada.append(sublista_dir[pos_dir])
            pos_dir += 1

    # Verificação da sobra
    sobra = []

    # Sobra à esquerda
    if pos_esq < pos_dir: sobra = sublista_esq[pos_esq:]
    # Sobra à direita
    else: sobra = sublista_dir[pos_dir:]
    juncoes +=1
    # O resultado final é a concatenação da lista ordenada
    # com a sobra
    return ordenada + sobra

###############################################################
divs = juncoes = comps = 0
#nums = [7, 4, 2, 9, 0, 6, 5, 3, 1, 8]
nums =[9,8,7,6,5,4,3,2,1,0]
resultado = merge_sort(nums)
print(resultado)


divs = juncoes = comps = 0
hora_ini= time()
tracemalloc.start()
nomes_ord= merge_sort(nomes)
mem_atual, mem_pico = tracemalloc.get_tracemalloc_memory()
hora_fim= time()
print(nomes_ord[:100])
print(f"tempo gasto para ordenar:{(hora_fim - hora_ini) * 1000}")
print(f"Divisoes:{divs}, comparações:{comps}, juncoes:{juncoes}")

