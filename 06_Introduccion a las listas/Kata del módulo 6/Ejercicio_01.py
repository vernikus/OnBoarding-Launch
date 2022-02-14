# En primer lugar, crea una variable denominada planets. Agrega los ocho planetas (sin Plutón) a la lista. A continuación, muestra el número de planetas.

platnets = planets = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
print('En el sistema solar tenemos', len(planets), 'planets')

#Agrega a Plutón a la lista que creaste. Luego muestra tanto el número de planetas como el último planeta de la lista.
planets.append('Plutón')
print(planets[-1], 'este es el último planeta')
