#Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”.
# Llamar a esta función desde el programa principal.
#funcion
def hola_mundo():
    print("Hola Mundo!")

#programa_principal
hola_mundo()

#Crear  una  función  llamada  saludar_usuario(nombre)  que  reciba como parámetro un nombre y
#devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá
#  devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.
#funcion
def saludar_usuario(nombre):
    print(f"Hola { nombre }, bienvenido!")

#programa_principal
saludar_usuario(input("ingrese su nombre: "))

#Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros
#e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y
#  llamar a esta función con los valores ingresados.
#funcion
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}.")

#programa_principal
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

#Crear dos funciones: calcular_area_circulo(radio) que reciba el ra- dio como parámetro y devuelva el área del círculo.
#  Calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar
#  el radio al usuario y llamar ambas funciones para mostrar los resultados.
#funciones
def calcular_area_circulo (radio):
    area= (3.1416 * radio *radio)
    return area

def calcular_perimetro_circulo(radio):
    perimetro=(3.1416*radio)
    return perimetro

#programa_principal
radio=float(input("ingrese el radio:"))
print("El area del circulo es: ", calcular_area_circulo(radio))
print("El perimetro del circulo es: ",calcular_perimetro_circulo(radio))


#Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva
# la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
#funcion
def segundos_a_horas(segundos):
    horas=float(segundos/3600)
    return horas

#programa_principal
segundos=int(input("ingrese la cantidad de segundos: "))
print("la cantidad de segundos: ", segundos, "equivalen a ", segundos_a_horas(segundos), "horas.")


#Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de
#  multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
#funcion
def tabla_de_multiplicar(numero):
    for i in range(1,11):
        print(f"{i}x{numero} = {i*numero}")

#programa_principal
tabla_de_multiplicar(int(input("ingrese un numero: ")))


#Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla
# con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
#funcion
def operaciones_basicas(a, b):
    """Realiza suma, resta, multiplicación y división entre dos números."""
    resultados = [a + b, a - b, a * b, a / b ]
    return resultados

# Ejemplo de uso
a=int(input("Ingrese un numero: "))
b=int(input("ingrese otro numero: "))
resultados = operaciones_basicas(a, b)
operaciones = ["Suma", "Resta", "Multiplicación", "División"]
for op, resultado in zip(operaciones, resultados):
    print(f"{op}: {resultado}")

#Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros,
#  y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar
#  el resultado con dos decimales.
#funcion
def calcular_imc(peso, altura):
    imc=peso/(altura**2)
    return imc

#programa_principal
peso=float(input("Ingrese su peso en Kg: "))
altura=float(input("Ingrese su altura en metros: "))
print("Su indice de masa corporal es: " , round(calcular_imc(peso,altura),2))


#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su
# equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
#funciom
def celsius_a_fahrenheit(celsius):
    fah=(celsius*9/5)+32
    return fah

#programa_principal
celsius=float(input("Ingrese una temperatura en grados Celsius: "))
print(f"{celsius} grados Celsius equivalen a {celsius_a_fahrenheit(celsius)} grados Fahrenheit")

#Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio
#  de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
#funcion
def calcular_promedio(a,b,c):
    promedio=(a+b+c)/3
    return promedio

#programa_principal
x=float(input("Ingreseun numero: "))
y=float(input("Ingreseun numero: "))
z=float(input("Ingreseun numero: "))
print(f"El promedio de los numeros ingresados es : {calcular_promedio(x,y,z)}")