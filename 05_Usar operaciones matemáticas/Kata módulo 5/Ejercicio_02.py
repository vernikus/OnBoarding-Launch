# Usando input, agrega el código para leer la distancia del sol para cada planeta, considerando 2 planetas.15

planetaUno = input('Ingresar la distancia del primer planeta en unidades de KM: ')
planetaDos = input('Ingresar la distancia del segundo planeta en unidades de KM: ')

# Debido a que input devuelve valores de cadena, necesitamos convertirlos en números. Para nuestro ejemplo, usaremos int
planetaUno = int(planetaUno)
planetaDos = int(planetaDos)

# Con los valores almacenados como números, ahora puedes agregar el código para realizar el cálculo, restando el primer planeta del segundo. Debido a que el segundo planeta podría ser un número mayor, usarás abs para convertirlo a un valor absoluto. También agregarás el código para mostrar el resultado en millas multiplicando la distancia del kilómetro por 0.621

resultadoKm = planetaDos - planetaUno
print(resultadoKm)

resultadoMillas = resultadoKm * 0.621
print(abs(resultadoMillas))