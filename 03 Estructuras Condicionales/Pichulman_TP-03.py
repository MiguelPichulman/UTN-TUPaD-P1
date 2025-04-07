#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje 
# en pantalla que diga “Es mayor de edad”.
edad = input("Ingrese su edad")
if edad >= 18 :
    print("Es mayor de edad")

#Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje
#  que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota = float(input("ingrese su nota"))
if nota >= 6 :
    print("Aprobado")
else :
    print("Desaprobado")

#Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje
#  "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso
#  del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Ingrese un numero par"))
if numero % 2 == 0 :
    print("Ha ingresado un numero par")
else :
    print("POr favor, ingrese un numero par")

#Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#  Niño/a: menor de 12 años.
#  Adolescente: mayor o igual que 12 años y menor que 18 años.
#  Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#  Adulto/a: mayor o igual que 30 años.
edad = int(input("Ingrese su edad"))
if edad >= 30 :
    print("Adulto/a")
elif edad < 30 and edad >= 18 :
    print("Adulto/a joven")
elif edad < 18 and edad >= 12 :
    print("Ud es un adolescente")
elif edad < 12 and edad >= 0 :
    print("Niño/a")
else:
    pass

#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña
#  de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#  pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar
#  la cantidad de elementos que tiene un iterable tal como una lista o un string.
contrasena = input("Ingrese su contraseña. Debe contener entre 8 y 14 caracteres")
if len(contrasena) >= 8 and len(contrasena) <=14 :
    print("Ha ingresado una contraseña correcta")
else :
    print("Por favor, ingrese una contraseña correcta")

#Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar
#  si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode, median,mean
import random
numeros_aleatorios = [random.randint(1,100) for i in range(50)]
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)
if media == moda and moda == mediana :
    print("Sin sesgo")
elif media > mediana and mediana > moda :
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda :
    print("Sesgo negativo o a la izquierda")
#muestro valores moda, mediana y media
print("moda: ", moda)
print("mediana: ", mediana)
print("media :", media)

#Escribir  un  programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación
#  al final e imprimir el string resultante por pantalla;  en  caso  contrario,  dejar  el  string tal cual lo ingresó el usuario e imprimirlo por pantalla.
frase = input("Ingrese una frase o palabra: ")
if frase[-1] == 'a' :
    frase = frase + '!'
elif frase[-1] == 'e' :
    frase = frase + '!'
elif frase[-1] == 'i' :
    frase = frase + '!'
elif frase[-1] == 'o' :
    frase = frase + '!'
elif frase[-1] == 'u' :
    frase = frase + '!'
print(frase)

#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#  1.   Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#  2.   Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#  3.   Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. 
# Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúscula
nombre = input("Ingrese su nombre: ")
print("Ingrese 1 si quiere su nombre en mayusculas")
print("Ingrese 2 si quiere su nombre en minusculas")
print("Ingrese 3 si quiere su nombre con la primera letra en mayusculas")
seleccion = int(input())
if seleccion == 1 :
    nombre = nombre.upper()
    print(nombre)
elif seleccion == 2 :
    nombre = nombre.lower()
    print(nombre)
elif seleccion ==3 :
    nombre = nombre.title()
    print(nombre)
else :
    print("Seleccione una opcion correcta")

#Escribir  un  programa  que  pida  al  usuario  la  magnitud  de  un  terremoto,  clasifique  la magnitud en una de las siguientes categorías según la escala
#  de Richter e imprima el resultado por pantalla:
# ● Menor que 3: "Muy leve" (imperceptible).
# ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible).
# ● Mayor  o  igual  que  4    y  menor  que  5:  "Moderado"  (sentido  por personas, pero generalmente no causa daños).
# ● Mayor o igual que 5   y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud = float(input("Ingrese la magnitud del terremoto (grados en escala de Richter)"))
if magnitud < 3 :
    print("Muy leve (imperceptible)")
elif magnitud >=3 and magnitud < 4 :
    print("leve (ligeramente perceptible)")
elif magnitud >=4 and magnitud < 5 :
    print("Moderado (sentido por personas pero generalmente no causa daños)")
elif magnitud >=5 and magnitud < 6 :
    print("Fuerte (puede causar daños en estructuras debiles)")
elif magnitud >=6 and magnitud < 7 :
    print("Muy fuerte (puede causar daños significativos)")
elif magnitud >=7 :
    print("Extremo (puede causar graves daños a gran escala)")
else :
    pass

#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.
#  El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("INgrese el Hemisferio en el que se encuentra. N: para Norte / S: para Sur")
mes = input("Ingrese el mes actual: ")
dia = int(input("Ingrese la fecha actual: "))
hemisferio = hemisferio.lower()
mes = mes.lower()
if hemisferio == "n" :
    if mes == "enero" or mes == "febrero" or (mes == "diciembre" and dia >=21) or (mes == "marzo" and dia <=20) :
        print("Invierno")
    elif mes == "abril" or mes == "mayo" or (mes == "marzo" and dia >=21) or (mes == "junio" and dia <=20) :
        print("Primavera")
    elif mes == "julio" or mes == "agosto" or (mes == "junio" and dia >=21) or (mes == "septiembre" and dia <=20) :
        print("Verano")
    elif mes == "octubre" or mes == "noviembre" or (mes == "septiembre" and dia >=21) or (mes == "dicimebre" and dia <=20) :
        print("Otoño")
    else :
        print("fecha invalida")
elif hemisferio == "s" :
    if mes == "enero" or mes == "febrero" or (mes == "diciembre" and dia >=21) or (mes == "marzo" and dia <=20) :
        print("Verano")
    elif mes == "abril" or mes == "mayo" or (mes == "marzo" and dia >=21) or (mes == "junio" and dia <=20) :
        print("Otoño")
    elif mes == "julio" or mes == "agosto" or (mes == "junio" and dia >=21) or (mes == "septiembre" and dia <=20) :
        print("Invierno")
    elif mes == "octubre" or mes == "noviembre" or (mes == "septiembre" and dia >=21) or (mes == "dicimebre" and dia <=20) :
        print("Primaver")
    else :
        print("fecha invalida")