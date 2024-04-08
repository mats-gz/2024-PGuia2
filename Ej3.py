#Ej3- Facil

dataExp = {
  "Matias": 18,
  "Joaquin": 17,
  "Vicente": 17
}

edad = dataExp.get("Matias")
print("La edad de Matias es:", edad)

dataExp.update({"Maxi" : 17})
print("Se ha actualizado los valores de la lista", dataExp.items())

dataExp.pop("Vicente")
print("Se ha actualizado los valores y se ha borrado el tercer item", dataExp.items())


#Ej3- Intermedio

inscripAntigua = ["A", "B", "A", "X", "X", "M", "Y", "B", "O", "B"]
frecInscrip = {}

for letra in inscripAntigua:
    if letra in frecInscrip:
        frecInscrip[letra] += 1
    else:
        frecInscrip[letra] = 1

print("La frecuencia de cada letra es:",frecInscrip)


#Ej3 - Dificil

manuscritos = ["Hola", "Hola", "Adios", "Buenas", "Adios", "Nos Vemos", "Hola"]

frecManuscritos = {}

for manuscrito in manuscritos:
    if manuscrito in frecManuscritos:
        frecManuscritos[manuscrito] += 1
    else:
        frecManuscritos[manuscrito] = 1

print("La palabra q mas se repite es:",max(frecManuscritos, key=frecManuscritos.get))

