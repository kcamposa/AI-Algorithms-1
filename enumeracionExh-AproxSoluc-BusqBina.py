def enumeracionExhaustiva(objetivo):
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta += 1

    if respuesta**2 == objetivo:
        print(f'La raiz cuadradra de {objetivo} es {respuesta}.')
    else:
        print(f'El {objetivo} no tiene una raíz cuadradra exacta.')

def aproximacionSoluciones(objetivo):
    epsilon = 0.0001 # que tan cerca queremos llegar de la respuesta
    paso = epsilon**2 # que tanto nos vamos ir acercando a cada iteracion
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        #print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raiz cuadradra de {objetivo}')
    else:
        print(f'La raiz cuadradra de {objetivo} es {objetivo}')

def busquedaBinaria(objetivo):
    epsilon = 0.01 
    bajo = 0.0 # limite inferior
    alto = max(1.0, objetivo) # max nos regresa el valor más alto entre dos numeros

    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        #print(f'bajo={bajo} , alto={alto} , respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2

    print(f'La raiz cuadradra de {objetivo} es {respuesta}.')

def menuPrincipal():
    opcion = 1
    while opcion != 0:
        opcion = int(input("""
        1) Enumeración Exhaustiva
        2) Aproximación de soluciones
        3) Busqueda Binaria 
        0) Salir
        Digite el método por el cual desea encontrar una raíz cuadradra: """))
        
        if opcion == 1:
            objetivo = int(input('Digite un numero: '))
            enumeracionExhaustiva(objetivo)
        elif opcion == 2:
            objetivo = int(input('Digite un numero: '))
            aproximacionSoluciones(objetivo)
        elif opcion == 3:
            objetivo = int(input('Digite un numero: '))
            busquedaBinaria(objetivo)
        elif opcion == 0:
            print('La aplicación ha finalizado.')
        else:
            print('La opción indicada no es correta, solo hay 3 opciones.')

menuPrincipal()