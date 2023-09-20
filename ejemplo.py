while True:
    respuesta = input("¿Quieres continuar? (sí/no): ").lower()
    
    if respuesta == "no":
        print("Saliendo del ciclo.")
        break
    
    elif respuesta != "sí":
        print("Respuesta no válida. Por favor, responde con 'sí' o 'no'.")
