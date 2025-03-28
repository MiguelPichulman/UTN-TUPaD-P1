##########################
# Pichulman Miguel Angel #
# 29036686               #
##########################
# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("HolaMundo!")
print("------------------")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
# realizar la impresión por pantalla.
nombre= input("Ingrese su nombre: ")
print(f"Hola {nombre}!")
print("------------------")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
# la impresión por pantalla.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
print("------------------")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
radio = float(input("Ingrese el radio de un de un circulo: "))
area = 3.14159 * radio * radio
perimetro = 2 * 3.14159 * radio
print(f"El area del circulo es {area}")
print(f"El perimetro del circulo es {perimetro}")
print("------------------")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"los segundos ingresados equivalen a {horas} horas ")
print("------------------")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.
numero = int(input("Ingrese un numero entero: "))
print(f"1 x {numero} = {1*numero}")
print(f"2 x {numero} = {2*numero}")
print(f"3 x {numero} = {3*numero}")
print(f"4 x {numero} = {4*numero}")
print(f"5 x {numero} = {5*numero}")
print(f"6 x {numero} = {6*numero}")
print(f"7 x {numero} = {7*numero}")
print(f"8 x {numero} = {8*numero}")
print(f"9 x {numero} = {9*numero}")
print(f"10 x {numero} = {10*numero}")
print("------------------")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1 = int(input("Ingrese un numero entero distinto de cero: "))
numero2 = int(input("Ingrese otro numero entero distinto de cero: "))
print(f"la suma es: {numero1 + numero2}")
print(f"la division: {numero1 / numero2}")
print(f"la multiplicacion es: {numero1 * numero2}")
print(f"la resta es: {numero1 - numero2}")
print("------------------")

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. 
altura = float(input("Ingrese su altura: "))
peso = float(input("Ingrese su peso: "))
imc = peso / (altura ** 2 )
print(f"Su IMC es: {imc}")
print("------------------")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.
celsius = float(input("Ingrese un atemperatura en grados Celsius: "))
fahrenheit = 9/5 * celsius + 32
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenhheit")
print("------------------")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.
numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
numero3 = float(input("Ingrese otro numero mas: "))
print(f"El promedio es : {float(numero1+numero2+numero3)/3}")
print("------------------")