#Ej2- Facil

frutas = ("manzana", "lechuga", "pera")

print("Estas son tus frutas:", frutas)

#Ej2- Intermedio

coordenadas = (1, 2)
print("Las coordenadas del lago son:", coordenadas)

#Ej2 -  Dificil

import math

coordenadas_obj = (5, 2)

radio = math.sqrt(coordenadas_obj[0]**2 + coordenadas_obj[1]**2)
#el radio es la raiz cuadrada de la suma de las cordenadas al cuadrado

angulo = math.atan2(coordenadas_obj[1], coordenadas_obj[0])
#el angulo es la tangente de las cordenadas

print("El radio (distancia desde el origen) es: ", radio)
print("Los angulos (en radianes) del objeto es: ", angulo)

