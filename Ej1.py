#Ej1-Facil#

monedas = [20, 45, 12, 55, 32]

sumMonedas = sum(monedas)
promMonedas = sumMonedas / len(monedas)
mayorMonedas = max(monedas)

print("La suma de todas las monedas es:", sumMonedas, ", su promedio es:", promMonedas, "y la mayor de todas es:", mayorMonedas)


#Ej1-Intermedio#

cantCristal = int(input("Ingresar cantidad de cristales:"))
aux = 0
cristales = []

while(aux < cantCristal):
    cristal = input("Ingrese el cristal:")
    cristales.append(cristal)
    aux += 1

def cristalesIguales (cristales):
    auxCris = []
    for i in cristales:
        if i not in auxCris:
            auxCris.append(i)

    return auxCris

print("Su lista de cristales sin elementos repetidos es:", cristalesIguales(cristales))



#Ejercicio1 - Dificil#

mon1 = [4, 72, 39, 99, 1]
mon2 = [10, 50, 56, 48]

def monedasConjunto(mon1, mon2):
    for i in mon1:
        mon2.append(i)

    return mon2
     
print("Las listas de valores de monedas unidas se verian asi:", monedasConjunto(mon1, mon2))