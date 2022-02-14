# Agrega el código para crear un nuevo diccionario denominado 'planet'. 
planet = {
    'name' : 'Mars',
    'moons': 2
}

# Muestra el nombre del planeta y el número de lunas que tiene. 
print(planet['name']) 
print(planet['moons'])

planet['circunferencia'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(planet['circunferencia'])

# Imprime el nombre del planeta con su circunferencia polar.
print(f'{planet["name"]} tiene una circunferencia de {planet["circunferencia"]["polar"]}')
