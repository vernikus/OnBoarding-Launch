planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Añade el código para determinar el número de lunas.
moons = planet_moons.values()
#print(planet_moons.values())
planets = len(planet_moons.keys())
#print(planet_moons.keys())


# Agrega el código para contar el número de lunas. 
total_moons = 0
for iterator in moons:
    total_moons = total_moons + iterator

promedio = total_moons / planets
print(promedio)
