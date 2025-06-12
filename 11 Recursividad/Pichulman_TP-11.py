#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y
# mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario
#funcion
def factorial(numero):
    if numero==0:
        return 1
    elif numero ==1:
        return 1
    else:
        return numero * factorial(numero-1)
#principal
numero=int(input("Ingrese un numero: "))
for i in range (1,numero+1):
    print(factorial(i))

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
#funcion
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)
#principal
numero=int(input("ingrese un numero: "))
for i in range(numero):
    print(f"F({i}) = {fibo(i)}")

#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.
#funcion
def potencia(n,m):
    if m==0:
        return 1
    else:
        return n*potencia(n,m-1)
#principal
base=2
exponente=5
print(f"{potencia(base,exponente)}")

#4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal
# y devuelva su representación en binario como una cadena de texto
def binario(n):
    if n<2:
        return str(n)
    else:
        return binario(n//2) + str(n%2)
#principal
n=10
print(f"{binario(n)}")


#5)Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto
# sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
#fucion
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

#programa
palabra = input("ingrese una plabra para ver si es un palidromo: ")
print(es_palindromo(palabra))

#6)Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero
# positivo y devuelva la suma de todos sus dígitos.
#funcion
def suma_digitos(n):
    if n<=9:
        return n
    else:
        return n%10 + suma_digitos(n//10)
#programa
numero = int(input("ingrese un numero: "))
print(suma_digitos(numero))


#7)Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques,
# en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel
# con un solo bloque.
#funcion
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)
#principal
cantidad = int(input("ingrese la cantidad de niveles de su piramide: "))
print(contar_bloques(cantidad))

#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número
#  entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese
# dígito dentro del número.
#funcion
def contar_digito(numero,digito):
    if numero<10 and numero>=0:
        if numero == digito:
            return 1
        else:
            return 0
    else:
        if numero%10 == digito:
            repite=1
        else:
            repite=0
        return repite + contar_digito(numero//10,digito)
#programa
numero=int(input("ingrese un numero entero mayor que cero: "))
digito=int(input("ingrese el digito a buscar: "))
print(f"el numero {digito} se repite {contar_digito(numero,digito)} veces")