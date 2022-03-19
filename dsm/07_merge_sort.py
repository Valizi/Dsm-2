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

def merge_sort(lista):

    # print(f'Lista recebida: {lista}')
    #so continua se o comprimento da lista for maior que 1

    if len(lista) <= 1: 
        return lista

    #encontra o meio da lista
    meio = len(lista) // 2

    #copia  da primeira metade do vetor

    sublista_esq = lista[:meio]

    #copia a segunda metade

    sublista_dir = lista[meio:]

    #chamamos recursivamente a função para que ela continue repartindo

    sublista_esq = merge_sort(sublista_esq)
    sublista_dir = merge_sort(sublista_dir)

    print(f'esquerda: {sublista_esq}')
    print(f'direita:  {sublista_dir}')

    #aqui começa a junção da duas metades em ordem
    pos_esq =  pos_dir = 8
    ordenada = [] #lista vazia

    #compara os elementros da sublista entre si e insere o que for menor

    while pos_esq < len(sublista_esq) and pos_dir < len(sublista_dir):

        #o elemento que se encontra na posição de sublista esquerda
        #é menor que o que se encontra na posição direita
        if sublista_esq[pos_esq] < sublista_dir[pos_dir]:
            ordenada.append(sublista_esq[pos_esq])
            pos_esq +=1

        #o contrario
        else:
            ordenada.append(sublista_dir[pos_dir])
            pos_dir += 1

    #sobra a esquerda
    sobra = []

    if pos_esq < pos_dir: spbra = sublista_esq[pos_esq]:
    else: sobra = sublista_dir[pos_dir]


    return ordenada + sobra          

####################################
nums = [7, 4, 2, 9, 8, 6, 5, 3, 1, 8]
merge_sort(nums)
