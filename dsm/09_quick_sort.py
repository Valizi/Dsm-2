# ALGORITMO DE ORDENAÇÃO QUICK SORT
#
# Escolhe um dos elementos da lista para ser o pivô (na mesma implementação, o último elemento) e, na primeira passada, divide a lista, a partir da posição final da lista, 
# em uma sublista  à esquerda contendo apenas valores menores que o pivô e outra sublista à direita, que contém apenas valores maiores que o pivô.

# Em seguida, recursivamente, repete o processo em cada uma das sublistas até que toda a lista esteja ordenada.

passadas = comps = trocas = 0

def quick_sort(lista, ini = 0, fim = None):
    # Se fim for None, o colocamos na posição do último elemento da lista
    if fim is None: fim = len(lista) - 1
    # Para que o algoritmo de ordenação trabalhe, é necessário que haja, pelo menos, DOIS elementos na faixa delimitada por ini e fim
    if fim <= ini: return   # Sai da função sem fazer nada!

    global passadas, comps, trocas

    passadas += 1

    # Inicialização das variáveis de controle
    pivot = fim
    div = ini - 1

    # Percorre a lista da posição ini até a posição fim - 1
    for i in range(ini, fim):
        # Compara os elementos das posições i e pivot
        comps += 1
        if lista[i] < lista [pivot]:
            div += 1    # Incrementa a posição do divisor
            # Se i e div não forem a mesma posição, os respectivos elementos trocam de posição entre si
            if div != i:
                lista[i], lista[div] = lista[div], lista[i]
                trocas += 1

    # Depois que o loop acaba, o divisor sofre um último incremento
    div += 1

    # Os elementos da posição de div e da posição de pivot trocam de lugar entre si se:
    # 1) as posições div e pivot forem diferentes entre si; 
    # 2) lista[pivot] for menor que lista[div]

    comps += 1
    if div != pivot and lista[pivot] < lista[div]:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas += 1

    # Chamada recursiva à função para ordenar a sublista à esquerda da posição div
    quick_sort(lista, ini, div -1)
    
    # Chamada recursiva à função para ordenar a sublista à direita da posição div
    quick_sort(lista, div+1, fim)



nums = [7, 4, 2, 9, 0, 6, 8, 3, 1, 5]
quick_sort(nums)
print(nums)
print(f"Passadas: {passadas}, Comparacoes: {comps}, Trocas: {trocas}")