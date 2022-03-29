#classe é uma estrutura que representa conjuntamente dados e algoritimos
#uma classe é como uma forma de bolo
#com o qual se pode criar diferentes  "bolos" (objetos)
#variando os ingredientes (dados) e o "modo de fazer" (algoritimos)
#Apesar dessa variação , as objetos criados 
#a partir da classe sempre terão o formato determinado por

from math import pi

class FormaGeometrica:

    #Uma classe pode ter, dentro de si, tanto dados quanto
    #funcoes  (estas representando os algoritimos). Uma função
    #especial, chamada __init__, é chamada sempre que um novo objeto é criado
    #a partir da classe

    def__init__(self,base, altura, tipo):
        self.base = Base
        self.altura = Altura
        self.tipo = Tipo



#################################################################

forma1 = FormaGeometrica(12,7,"R")
forma2 = FormaGeometrica(7.5,8.2,"T")

print(f"forma1: base {forma1.base}, altura {forma1.altura}, tipo {forma1.tipo}")
print(f"forma2: base {forma2.base}, altura {forma2.altura}, tipo {forma2.tipo}")