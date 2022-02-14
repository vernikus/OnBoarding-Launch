from datetime import date
# sum = 1 + 2
# print(sum)
# print('hello world')

# variables
sum = 1 + 2 # 3
product = sum * 2
print(product)

# tipo de datp
distancia_a_alfa_centauri = 4.367
print(type(distancia_a_alfa_centauri))
# fechas

print(date.today())

# convertir datos a string
print('Hoy es '+ str(date.today()))
# guardar datos del usuario

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

# convertir datos string a numeros enteros 
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
# antepones int para que la cadena sea convertida a un numero entero o flotante
print(int(first_number) + int(second_number))