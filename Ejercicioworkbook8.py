porcionesDeFrutas = {'papaya': 5000, 'pera': 2500, 'manzana': 3000, 'durazno': 2500}
porcionesAdicionales = {'queso': 3500, 'crema de leche': 2500, 'galletas': 2500, 'salsas': 1500}
# cree 2 diccionarios con las claves son los ingredientes y los precios son la definicion de esas claves en el diccionario
total_frutas = 0
total_adiciones = 0

for i in range(3):  # Solicitar tres porciones de frutas
    busca = input('Introduce tu porción de fruta {}: '.format(i + 1))
    precio = porcionesDeFrutas.get(busca, None) #busca el precio asignado a las claves
    if precio is not None:
        total_frutas += precio
    else:
        print('No encuentro la porción de fruta "{}"'.format(busca))
        
print('Total porciones de frutas:', total_frutas)

print('Ahora ingresa tus adiciones')
for i in range(3):  # Solicitar tres adiciones
    busca = input('Introduce tu adición {}: '.format(i + 1))
    precio = porcionesAdicionales.get(busca, None)
    if precio is not None:
        total_adiciones += precio
    else:
        print('No encuentro la adición "{}"'.format(busca))

print('Total adiciones:', total_adiciones)

total_general = total_frutas + total_adiciones
print('Total general:', total_general)
