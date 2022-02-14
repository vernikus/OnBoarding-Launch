# Ejercicio : escribe declaraciones if/else/elif
# Para este ejercicio, escribirás una lógica condicional que imprima una advertencia si un asteroide se acerca a la Tierra demasiado rápido. La velocidad del asteroide varía dependiendo de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.
# Un asteroide se acerca, y viaja a una velocidad de 49 km/s.

velocidad = 25
asteroide = 49
if asteroide > velocidad:
    print('Alerta de seguridad mundial, un asteroide se aproxima')
else :
    print('Todo tranquilo, sin amenazas de extinsion')

# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces produce un rayo de luz que se puede ver desde la Tierra. Escribe la lógica condicional que usa declaraciones if, else, y elif para alertar a las personas de todo el mundo que deben buscar un asteroide en el cielo. ¡Hay uno que se dirige a la tierra ahora a una velocidad de 19 km/s!

velocidadDos = 20
asteroideDos = 21
if asteroideDos > velocidadDos:
    print('A toda la poblacion mundial, favor de buscar un asteroide en el cielo')
elif asteroideDos == velocidadDos:
    print('A toda la poblacion mundial, favor de buscar un asteroide en el cielo')
else :
    print('Todo tranqilo, sin amenazas de extinsion')

# Si una pieza de un asteroide que es más grande que 25 metros pero más pequeña que 1000 metros golpeara la Tierra, causaría mucho daño.
# La velocidad del asteroide varía en función de lo cerca que esté del sol, y cualquier velocidad superior a 25 kilómetros por segundo (km/s) merece una advertencia.
# Si un asteroide entra en la atmósfera de la Tierra a una velocidad mayor o igual a 20 km/s, a veces produce un rayo de luz que se puede ver desde la Tierra.

tamanioAsteroide = 25
asteroideGrande = 30
asteroideVelocidad = 50

if asteroideGrande > tamanioAsteroide and asteroideGrande < 1000 or asteroideVelocidad > velocidad :
    print('Alerta de seguridad mundial, un asteroide se aproxima, la tierra puede ser destruida')
    print('Favor de mantener la calma')
elif asteroideVelocidad >= velocidadDos :
    print('A toda la poblacion mundial, favor de buscar un asteroide en el cielo')




