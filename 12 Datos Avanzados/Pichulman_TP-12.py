#1) Dado el diccionario precios_frutas
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
#Añadir las siguientes frutas con sus respectivos precios:
# Naranja = 1200
# Manzana = 1500
# Pera = 2300
precios_frutas={"banana": 1200, "anana": 2500, "melon": 3000, "uva":1450}
precios_frutas["naranja"]=1200
precios_frutas["manzana"]=1500
precios_frutas["pera"]=2300
print(precios_frutas)


#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# Banana = 1330
# Manzana = 1700
# Melón = 2800
precios_frutas={"banana": 1200, "anana": 2500, "melon": 3000, "uva": 1450, "naranja": 1200, "manzana": 1500, "pera": 2300}
precios_frutas["banana"]=1330
precios_frutas["manzana"]=1700
precios_frutas["melon"]=2800
print(precios_frutas)



#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.
precios_frutas={'banana': 1330, 'anana': 2500, 'melon': 2800, 'uva': 1450, 'naranja': 1200, 'manzana': 1700, 'pera': 2300}
lista_precios=list(precios_frutas.keys())
print(lista_precios)


#4) Escribí un programa que permita almacenar y consultar números telefónicos.
# Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# Luego, pedí un nombre y mostrale el número asociado, si existe.
listado={}
for i in range(2):
    nombre=input(f"ingrese el nombre del contacto telefonico {i+1}: ")
    telefono=int(input(f"ingrese el numero de telefono del contacto {nombre}: "))
    listado[nombre]=telefono
buscar=input(f"ingrese el contacto a buscar: ")
if buscar in listado:
    print(f"{buscar}, si se encuentra en los contactos: {listado[buscar]}")
else:
    print(f"{buscar}, no se encuentra en los contactos")

#5) Solicita al usuario una frase e imprime:
# Las palabras únicas (usando un set).
# Un diccionario con la cantidad de veces que aparece cada palabra.
frase=input("ingrese una frase: ")
frase=frase.lower().split()
palabras_unicas=set(frase)
print(frase)
print(palabras_unicas)
cantidad={}
for palabra in frase:
    if palabra in cantidad:
        cantidad[palabra]+=1
    else:
        cantidad[palabra]=1
print(cantidad)

#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = input(f"Ingrese 3 notas separadas por comas para {nombre}: ")
    tupla_notas = tuple(map(float, notas.split(',')))
    alumnos[nombre] = tupla_notas

print("Promedios de los alumnos: ")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}:{promedio:.2f}")

#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
# Sets de estudiantes que aprobaron cada parcial
import random
parcial1 = set(random.sample(range(100,110,7)))
parcial2 = set(random.sample(range(100,110,7)))


ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# Estudiantes que aprobaron solo uno de los dos (diferencia simetrica)
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", solo_uno)

# Estudiantes que aprobaron al menos uno (union)
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# agenda
agenda = {("lunes", "9:00"): "Reunión con proveedores",("martes", "14:30"): "Clase de programación",("viernes", "18:00"): "Entrega de proyecto"}

# Consulta de evento
dia = input("Ingrese un dia: ")
hora = input("Ingrese una hora (por ejemplo 9:00): ")

clave = (dia, hora)

if clave in agenda:
    print("actividad programada:", agenda[clave])
else:
    print("no hay actividades para ese dia y hora.")



#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
#diccionario donde:
# Las capitales sean las claves.
# Los países sean los valores.
# diccionario original: países → capitales
paises_a_capitales={"Argentina": "Buenos Aires","Francia": "París","Italia": "Roma","Brasil": "Brasilia"}

# Nuevo diccionario: capitales → países
capitales_a_paises = {}
for pais, capital in paises_a_capitales.items():
    capitales_a_paises[capital] = pais

print("Diccionario invertido:")
print(capitales_a_paises)
