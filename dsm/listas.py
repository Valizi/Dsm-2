
# LISTA EM PYTHON
# LISTA SÃO UMA FORMA DE ARMAZENAR VARIOS VALORES EM UMA UNICA VARIAVEL
# TAIS VALORES PODEM SER DIFERENTES

valores = [1,2,3,4,5,"Cenoura","Batata", True]

#OPERAÇÕES SOBRE LISTA

# 1) Percurso: percorra a lista do primeiro e ultimo elemento fazendo algo com cada um deles, no caso vamos exibior cada um dos elemento com um print

for p in valores:
    print(p)
    
2# Inserindo um novo elemento no final da lista: append()
valores.append("cebola")
valores.append(22)

print('Mostrar todos os valores inseridos: ' ,valores)

#INSERINDO UM NOVO ELEMENTO ESPECIFICANDO A POSIÇÃO DELE NA LISTA: INSERT()
#SÃO 2 PARAMETROS, O 1° É A POSIÇÃO DELE NA LISTA E O 2° E O VALOR A SER INSERIDO
for v in valores :
    print(v)

print ("Após a inserção de 2 valores no fim:", valores)

valores.insert(4, 8) 
valores.insert(0,"chuchu")
print ("Após 2 insert()", valores)
 
print ("Numero de elementos na lista:", len(valores))

ultimo = valores.pop()
print (f"{ultimo} era o ultimo elemento da lista:")
print ("Após remoção do ultimo elemento:", valores)

del valores[7] 
print("Após remoção da posição 7", valores)

del valores[8]
print("Após remoção da posição 8", valores)

valores.remove('cebola')  #remove o valor 17
print("Após a remoção do valor 17", valores)

valores.remove('Batata')
print("Após remoção do valor cenoura", valores)

subvalores = valores[0:7]
subvalores2 = valores[4:10]
print("Subvalores:", subvalores)
print('Subvalores 2:', subvalores2)
print("Valores:", valores)
print("Subvalores de 5 a 9"), valores [5:9]
print("Sublista de 0 até 8:", valores[0:8])
print("Subvalores de 6 até o final ", valores[5:])
