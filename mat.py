import math




print(math.pi)




numero = 2567

raiz = math.sqrt(numero)
print(raiz)

numero1 = 1
numero2 = 2
resultado = numero + numero1
print(resultado)

## tipos de datos 2
# LO QUE MÁS VAMOS A UTILIZAF EN PYTHON

## listas
lista = [1, 2, 3, 4, 5, 6]  ##cuando una variable lleva corchetes es una lista
##
diccionario = {"key":"value"} #
##

#COMPLEMENTARIOS
##sets
sets=(1, 2, 3, 4, 5, 6) #Utiliza la misma llave que el diccionrio pero el formato es distinto
##tuplas
tuplas = (1, 2, 3, 4, 5, 6) #Una vez creado no se puede modificar



##listas

frutas = ["manzana", "naranja", "sandia", "frutilla", [1,2,3,4]]
    #index    0         1          2           3           4        = posicion
    #        -5        -4         -3          -2          -1

frutas[3] = "kiwi"
frutas[0] = "algo"
frutas[4] = [] #lista vacia

""" print(frutas[2])
print(frutas[1])
print(frutas[0])
print(frutas[5][4][0]) """

print(frutas[-1]) #Para imprimir el último elemento de la lista

#print(dir(frutas)) #Para conocer las funciones

#append
frutas.append("melon")  #agrega un ítema al final de la lista
print(frutas)

##remove
frutas.remove("manzana") 

print(frutas)


personas = ["mara", "dona"]

for i in personas:
    print(i) 

##diccionario


##Cuando hablamos de orientación de objeto, hablamos sobre clases
#clase y objeto
#lapiz
"""marca:pilot
color:negro
tamaño:10cm
material:metal

rayar
escribir
dibujar
pintar"""

