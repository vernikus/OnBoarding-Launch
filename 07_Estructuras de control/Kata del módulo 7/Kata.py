# Comienza agregando dos variables, una para la entrada del usuario, con el nombre new_planet, y otra variable para la lista de planetas, denominada planets.

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Ingrese el nuevo planeta: ') 
    print(planets)

    
                                            ###PARTE DOS DE LA KATA ###

for iterator in planets :
        print(iterator)
        