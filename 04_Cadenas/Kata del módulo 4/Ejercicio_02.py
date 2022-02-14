from numpy import place


name = 'Luna'
gravity = 0.00162 # in kms
planet = 'Tierra'

# Primero, crea un título para el texto. Debido a que este texto trata sobre la gravedad en la Tierra y la Luna, úsalo para crear un título significativo. Utiliza las variables en lugar de escribi
titulo = f'La gravedad entre la {planet} y la {name}'.title()
#print(titulo)

# Ahora crea una plantilla de cadena multilínea para contener el resto de la información. En lugar de usar kilómetros, debes convertir la distancia a metros multiplicando por 1,000.

plantilla = f"""{'-'*80} 
Nombre del planeta: {planet} 
Gravedad en {name}: {gravity * 1000} m/s2 
"""
#print(plantilla)

# Finalmente, usa ambas variables para unir el título y los hechos.

plantillaCompleta = f"""{titulo} 
{plantilla} 
""" 
#cprint(plantillaCompleta)

# Ahora usa información de una luna diferente para ver si la plantilla todavía funciona.

planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'

plantilla = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""
#print(plantilla)

# La salida no muestra información sobre Marte. Todavía muestra información sobre la Luna. Esto sucede porque las cadenas f están ansiosas en su evaluación, por lo que las variables una vez asignadas no se pueden reasignar. Para evitar este problema, vuelva a hacer la plantilla para utilizar .format():

nuevaPlantilla = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
# Debido a que .format() no permite expresiones, la gravedad en Ganímedes es incorrecta. Asegúrese de que la operación se realiza fuera de la plantilla de formato e imprima de nuevo para ver el resultado de trabajo.

print(nuevaPlantilla.format(nombre=nombre, planeta=planeta, gravedad=gravedad * 1000))
