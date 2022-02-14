# Función para leer 3 tanques de combustible y muestre el promedio
def reporte(tanquePrimario, tanqueSecundario, tanqueEmergencia):
    promedio = (tanquePrimario + tanqueSecundario + tanqueEmergencia) / 3
    return f"""Reporte de combustible:
    Promedio: {promedio}%
    Tanque primario: {tanquePrimario}%
    Tanque secundario: {tanqueSecundario}%
    tanque de emergencia: {tanqueEmergencia}% 
    """

# Llamamos a la función que genera el reporte print(funcion(tanque1, tanque2, tanque3))
print(reporte(50, 30, 90))

# Función promedio 
def promedio(values):
    total = sum(values)
    number_of_items = len(values)
    return total / number_of_items
promedio([80, 85, 81])

# Actualiza la función
def reporte(tanquePrimario, tanqueSecundario, tanqueEmergencia):
    return f"""Reporte de combustible:
    Promedio: {promedio([tanquePrimario, tanqueSecundario, tanqueEmergencia])}%
    Tanque primario: {tanquePrimario}%
    Tanque secundario: {tanqueSecundario}%
    tanque de emergencia: {tanqueEmergencia}% 
    """
print(reporte(60, 10, 99))