
print("hola gente linda")

# vARIABLES

nombre = "jo"
edad = 35
altura = 2.12
es_docente = False
ciudad = "Vancouver"

# TIPOS DE DATOS

str #esto es un texto
int #esto es un entero
float #esto es un flotante
bool #esto es verdadero o falso


#INPUT
precio = input("escribe un numero : ") #pedir por consola un tipo de dato stren (texto)
int(precio) #convertir a entero el str
precio =+ 10 #el precio sumado + 10 ya que ahora es numero entero
print(precio) 

## CONDICIONALES


#if condicion:
#    codigo 

edad = 20 

if edad >= 18:
    print("puede entrar a la disco")

contador = 0


# WHILE

while contador < 10: #bucle si es true o false
    print(contador)
    contador += 1

while True:
    texto = input("escribe para salir de bucle")

    if texto == "salir":
        break

#FOR

#for elemento in lista
#    codigo

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]



"""for i in range(20):
    print(1)"""
#rango si le paso 4 me genera = 0, 1, 2, 3
#10 = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


numeros = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros)
ordenados = sorted("numeros")
print(ordenados)


