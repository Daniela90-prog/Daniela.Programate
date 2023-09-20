palabra1 = input("Digite la primera palabra que desee: ")
palabra2 = input("Digite la segunda palabra que desee: ")
palabra3 = input("Digite la tercera palabra que desee: ")
Diccionario = [palabra1, palabra2, palabra3]
letraQueDeseas = input("Digite la letra de las palabras que comiencen con: ")
for palabra in Diccionario:
    if palabra[0].lower() == letraQueDeseas:
       print("las palabras que comienza con la letra deseada son:")
       print(palabra)
else:
    print("no hay palabras para mostrar")