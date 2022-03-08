
''' Função para calcular o indice de massa corporea IMC'''
#def imc(peso, altura):
   # return (peso / altura ** 2)
    
#print(f"peso: 89, altura: 1.75, IMC: {imc(89, 1.75)}")

#p = float(input ("Qual o peso?"))
#a = float(input ("Qual a altura?"))
#i = imc (p, a) #chama a funcao

#print(f"Peso: (p), altura: (a), IMC: {i:.3f}")

'''funcao que calcula a area de uma forma geometrica especificada'''

def calcular_area(base, altura, forma):
    if forma == "R": #retangulo
     return base * altura
    elif forma == "T": #triangulo
     return base * altura / 2
    elif forma == "E": #Elipse
     return (base / 2) * (altura / 2) * 3.1416 #numero pi
    else: #forma desconhecida
     return None
     '''exemplos de chamada da funcao calcular area'''
print(f"retangulo 15x25: {calcular_area(15, 25, 'R')}")
print(f"triangulo 12x16: {calcular_area(12, 16, 'T')}")
print(f"elipse    10x20: {calcular_area(10, 20, 'E')}")
      
      