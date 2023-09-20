print("Juega y programa")
print("¡Hola! ¡Bienvenidos! Te presento el juego donde aprenderás a programar con ejercicios que te ayudarán a mantener tu aprendizaje cada día.")
print("Comencemos.")
print("Las únicas reglas son: todas tus respuestas deben ingresarse en minúsculas y tienes un máximo de 2 intentos por pregunta.")
nombreDeUsuario = input("Ingresa tu nombre: ")   
def iniciar_juego():   
    print("Tengo una pregunta.")    
    intento = 0
    maxintentos = 2    
    while intento < maxintentos:
        respuesta = input("¿Estás listo? (sí/no): ")        
        if respuesta == "si":
            print("Ok, puedes continuar.")
            return True
        elif respuesta == "no":
            print("Respuesta incorrecta.")
            return False
        else:
            print("Respuesta incorrecta") 
            intento +=1
        print("Agotaste tus intentos. El juego termina.")
        return False

# Llamamos a la función creada para inciar la lección 1
if iniciar_juego():
    intento = 0
    maxintentos = 2   #número maximo de intentos
    print("Lección 1")
    print("Phyton es un lenguaje de alto nivel de programacón el cual es utilizado para desarrollar aplicaciones de todo tipo como por ejemplo : Netflix, Spotify, instragram, entre otros.")
    while intento < maxintentos:
        print("Reto lección No.1 Elige la opción correcta")
        print("a) " "Phyton es un lenguaje de alto nivel de programacón el cual es utilizado para desarrollar aplicaciones de todo tipo.")
        print("b) " " Phyton es un juego acción")
        respuesta1 = input("¿Cuál es la respuesta correcta? (a/b): ")
        if respuesta1 == "a":
            print("Respuesta correcta. ¡Bien hecho!")
            break  # Se rompe el ciclo si la respuesta es correcta
        elif respuesta1 == "b":
            print("Respuesta incorrecta, inténtalo de nuevo.")
            intento += 1
        else:
            print("Respuesta incorrecta, por favor, elige 'a' o 'b'.")
    if intento == maxintentos:
        print("Agotaste tus intentos. El juego termina.")
else:
    print("El juego ha terminado.")

# Llamamos a la función creada para iniciar la lección 2 
if iniciar_juego():
    intento = 0
    maxintentos =  2   #número maximo de intentos
    print("Lección 2 tipos de variables")
    print("nombre = Diana #string.str , los textos van entre comillas.")
    print(" números = 25 #el formato de números siempre sera int ")
    print("decimal = 45,9  # el formato de números decimales es float.")
    print(" Reto lección No.2 Elige la opción correcta ")
    print("tenemos el tipo de variable longitud_del_ camino = 45.9")
    while intento < maxintentos:
        enunciado1 = print("¿Cúal es el tipo de variable correcto? (a/b): ")
        print("a) " "float")
        print("b) " "str")
        respuesta1 = input("coloque aqui su respuesta (a/b): ")
        if respuesta1 == "a":
            print("Respuesta correcta. ¡Bien hecho! ")
            break  # Se rompe el ciclo si la respuesta es correcta
        elif respuesta1 == "b":
            print("Respuesta incorrecta")
            intento +=1
        else:
            print("Respuesta incorrecta")
    if intento == maxintentos:
        print("Agotaste tus intentos. El juego termina.")
else:
    print("El juego ha terminado.")

# Llamamos a la función creada para iniciar la lección 2 
if iniciar_juego():
    intento = 0
    maxintentos =  2   #número maximo de intentos
    print("Lección 3 Condicionales if , elif y else")
    print("El condicional (if) se utiliza cuando se cumple condicion, adicional viene acompañado de (elif) para establecer otro punto de comparación y (else) es la negación de dichas condiciones.")
    print("Reto lección No.3 Compila y diviertete")
    print("Instrucciones: Abre tu navegador de preferencia y copia y pega el siguiente link:(https://replit.com/~ )crea un perfil y ¡Comencemos a compilar!")
    print("Vas seleccionar la opción create repl // luego escoges el template de phyton y das click en template.")
    print("Ahora procede a copiar y pegar el siguiente código: (numero1 = 5 , numero2 = 10 , if)numero1 > numero2: , print(si el número era mayor)else: print(si, el número era menor)")
    print("Ten en cuenta: Cada cariable, el condicional if, else y print debe ocupar una linea cada uno, ademas recuerda que los print deben ir entre comillas")
    print("Al momento de ejecutar el codigo, De acuerdo a las siguientes opciones presentadas a continuación")
    while intento < maxintentos:
        enunciado1 = print("Responda ¿Cuál es el print correcto?(a/b): ")
        print("a) " "si el número era menor")
        print("b) " "si el número era mayor")
        respuesta1 = input("coloque aqui su respuesta (a/b): ")
        if respuesta1 == "a":
            print("Perfecto  haz ganado este primer módulo de programación Felicitaciones ")
            break  # Se rompe el ciclo si la respuesta es correcta
        elif respuesta1 == "b":
            print("Respuesta incorrecta")
            intento +=1
        else:
            print("Respuesta incorrecta")
    if intento == maxintentos:
        print("Agotaste tus intentos. El juego termina.")
else:
    print("El juego ha terminado.")