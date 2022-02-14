# Función con un informe preciso de la misión. Considera hora de prelanzamiento, tiempo de vuelo, destino, tanque externo y tanque interno

def mission_report(pre_launch_time, tiempoVuelo, destino, tanqueSecundario, tanquePrimario):
    return f"""
    Mision a {destino}
    Tiempo total de viaje: {pre_launch_time + tiempoVuelo} minutos
    Combustible total restante: {tanqueSecundario + tanquePrimario} galones
    """
print(mission_report(14, 51, "Moon", 400000, 600000))

# Escribe tu nueva función de reporte considerando lo anterior

def mission_report(destino, *minutos, **depositoCombustible):
    return f"""
    Mision a {destino}
    Tiempo total de viaje: {sum(minutos)} minutos
    Combustible total restante: {sum(depositoCombustible.values())}
    """
print(mission_report("Moon", 10, 15, 51, primario=600000, secundario=400000))

# Escribe tu nueva función

def mission_report(destino, *minutos, **depositoCombustible):
    reporte = f"""
    Mision a {destino}
    Tiempo total de viaje: {sum(minutos)} minutos
    Combustible total restante: {sum(depositoCombustible.values())}
    """
    for iterator, galones in depositoCombustible.items():
        reporte += f" tanque --> {iterator} {galones} galones\n"
    return reporte
print(mission_report("Moon", 8, 11, 55, primario=600000, secundario=400000))