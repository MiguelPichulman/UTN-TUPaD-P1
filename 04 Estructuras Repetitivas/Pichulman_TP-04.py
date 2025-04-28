#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# # (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range (0,101):
    print (i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la
# cantidad de dígitos que contiene.
numero = input("Ingrese un numero: ")
digitos=0
for i in numero:
    digitos = digitos+1
print("el numero ", numero, "tiene ",digitos)

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos
#  valores dados por el usuario, excluyendo esos dos valores.
numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero"))
if numero1>numero2:
    max = numero1
    min = numero2
else:
    max = numero2
    min = numero1
suma = 0
for i in range (min+1,max):
    suma = suma + i
print(suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia.
#  El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
suma = 0
while True:
    numero = int(input("Ingrese un numero. Si ingresa 0, finaliza : "))
    suma = suma + numero
    if numero == 0:
        break
print("la suma de todos los numero ingresados es: ",suma)

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
#  Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_random = random.randint(0,9)
intento = 0
while True:
    adivina = int(input("Adivina el numero.....: "))
    if adivina == numero_random:
        print("adivinaste en ",intento, "intentos!!!")
        break
    else:
        intento = intento + 1
        print("proba de nuevo :)")
print("FIN")

#6) Desarrolla un programa que imprima en pantalla todos los números pares
#  comprendidos entre 0 y 100, en orden decreciente.
for i in range(100,-2,-2):
    print(i)

#7) Crea un programa que calcule la suma de todos los números
# comprendidos entre 0 y un número entero positivo indicado por el usuario.
numero = int(input("Ingrese un numero: "))
suma=0
for i in range (0,numero+1):
    print(i)

#8)Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, 
# cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes
# usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).
limite = 5
par = 0
impar = 0
positivos = 0
negativos = 0
for i in range (0,limite):
    numero = int(input("Ingrese numeros enteros"))
    if (numero % 2) == 0:
        par = par +1
    else:
        impar = impar + 1
    if numero >= 0 :
        positivos = positivos +1
    else:
        negativos = negativos +1
print("ha ingresado ",par," numeros pares")
print("ha ingresado ",impar," numeros impares")
print("ha ingresado ",positivos," numeros positivos")
print("ha ingresado ",negativos," numeros negativos")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule
#  la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero 
# debe poder procesar 100 números cambiando solo un valor).
limite = 100
suma = 0
for i in range (0,limite):
    numero = int(input("Ingrese numeros enteros"))
    suma = suma + numero
print("la media de los numeros ingresados es ",(suma/limite))

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario.
#  Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = input("Ingrese un numero: ")
cantidad_digitos = len(numero)
nuevo_numero = ""

for i in range(cantidad_digitos-1, -1, -1):
    nuevo_numero = nuevo_numero +numero[i]
print(nuevo_numero)