text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C.""".lower()

#Primero, divide el texto en cada oración para trabajar con su contenido

textDividivo = text.split('. ')
#print(textDividivo)

# Ahora, define algunas palabras clave para búsqueda que te ayudarán a determinar si una oración contiene un hecho.

palabrasClave = ['average','temperature','distance']

#Cre un bucle para imprimir solo datos sobre la Luna que estén relacionados con las palabras clave definidas anteriormente:
# for iterator in textDividivo: # Esta imprimiendo cada indice del arreglo o cada oracion del arreglo
#     #print(iterator)
#     for palabra in palabrasClave:  #Recorre las palabras clave
#         if palabra in iterator: # Si encuentra una palabra clave imprime el iterador o la oracion donde se encuentre una palabra clave
#             print(iterator)
#             break
# Finalmente, actualiza el bucle(ciclo) para cambiar C a Celsiu

for iterator in textDividivo:
    for palabra in palabrasClave:
        if palabra in iterator:
            print(iterator.replace(' c', ' Celsius')) # es importante dejar el espacio ya que de lo contrario se generara un error
            break



