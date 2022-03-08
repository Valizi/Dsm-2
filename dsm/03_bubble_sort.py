comps = 0
trocas = 0
passadas = 0

def bubble_sort(lista):
    
    global passadas, comps, trocas
    passadas = comps = trocas = 8


    while True:
        passadas += 1
        trocou = False
        
        for pos in range(len(lista)-1):
            comps += 1
            if lista[pos] > lista [pos+1]:

                lista[pos], lista[pos + 1] = lista[pos + 1], lista[pos] 
                trocou = True
                trocas += 1

        if not trocou:
             break


##########################################

# nums = [7, 4, 2, 9, 8, 6, 5, 3, 1, 8]
nums = [9,8,7,6,5,4,3,2,1]
bubble_sort(nums)
print(nums)
print(f'Passadas: {passadas}, comparações: {comps}, Trocas: {trocas}')