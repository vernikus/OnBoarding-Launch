# Comienza agregando el código para crear una lista con los planetas.
platnets = planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

# A continuación, agrega el código para solicitar al usuario un nombre. Debido a que las cadenas distinguen entre mayúsculas y minúsculas en Python, pídale al usuario que use una letra mayúscula para comenzar el nombre del planeta.
planetUser = input('Ingrese un planeta: ')

# Para determinar qué planetas están más cerca que el que ingresó el usuario, debes encontrar dónde está el planeta en la lista. Puedes utilizar index para realizar esta operación. Agrega el código para encontrar el índice del planeta.
planetIndex = planets.index(planetUser)

# Con el índice determinado, ahora puedes agregar el código para mostrar los planetas más cercanos al sol.
print('Aquí están los planetas más cerca que ' + planetUser)
print(planets[0:planetIndex])

#Puedes usar el mismo índice para mostrar planetas más alejados del sol. Sin embargo, recuerda que el índice inicial se incluye cuando usas un slice. Como resultado, tendrás que agregar 1 al valor. Agrega el código para mostrar los planetas más alejados del sol.

print('Aquí están los planetas más cerca que ' + planetUser)
print(planets[planetIndex + 1:])