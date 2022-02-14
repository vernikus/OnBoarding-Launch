# Exploremos cómo podemos crear un programa que pueda calcular la distancia entre dos planetas. Comenzaremos usando dos distancias de planetas: Tierra (149.597.870 km) y Júpiter (778.547.200 km).

tierra = 149597870
jupiter = 778547200

# Con los valores obtenidos, es el momento de añadir el código para realizar la operación. Restarás el primer planeta del segundo para determinar la distancia en kilómetros. A continuación, puedes convertir la distancia del kilómetro en millas multiplicándola por 0.621.

resultado = (jupiter - tierra) * 0.621
print(resultado)
