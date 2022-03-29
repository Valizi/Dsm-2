#Um dicionario é uma estrutura de dados fornecida pela linguagem Python
#capaz de armazenar multiplos valores em uma unica variavel, por meio
#de pares de chave-valor

pessoa = {
    #nome é a chave
    #gervasio é o valor
    "nome": "Gervasio Gomes Garcia",
    "sexo": "M",
    "idade": 69,
    "peso": 76,
    "altura": 1.77
}

print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")


imc = pessoa["peso"]/ pessoa["altura"] ** 2
print(f"IMC: {imc}")

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo":'R' #retangulo
}

forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo":'T' #triangulo
}

forma3 = {
    "base": 5,
    "altura": 3,
    "tipo":'E' #elipse
}

forma4 = {
    "base": 18,
    "altura": 5,
    "tipo":'R' # Tipo não reconhecido
}
#forma geometrica completamente anomala
forma5 = {
    "legume": "batata",
    "fruta": "jabuticaba",
    "tipo":'T' # Tipo não reconhecido
}

#Inserindo as formas em uma lista para percorrer com for
lista_formas =[forma1, forma2, forma3, forma4, forma5]

# Função qeu calcula a area de uma forma de acordo com a base, a altura e o tipo

from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R":
        return forma["base"] * forma["altura"]
    elif forma["tipo"] == "T":
        return forma["base"] * forma["altura"] / 2
    elif forma["tipo"] == "E":
        return (forma["base"] /2 ) * (forma["altura"] / 2) * pi
    else:
        
        raise Exception("Erro: Tipo de forma não reconhecido")

for i in range(0, len(lista_formas) ):
    print("-" * 30)
    print(f"Calculando área da forma{i + 1}:")
    print(f"Tipo: {lista_formas[i]['tipo']}; base: {lista_formas[i]['base']}; altura: {lista_formas[i]['altura']}; AREA: {calcular_area(lista_formas[i])}")
     
        