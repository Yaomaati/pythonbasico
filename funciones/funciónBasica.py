opcion = int(input("Selecciona alguna de las opciones: (1,2,3): "))

def texto(mensaje):
    print("Hola, bienvenido a mi programa")
    print("Acabas de elegir una opción")
    print("Y esa es: ")
    print(mensaje)



if opcion == 1:
    texto("La primera opción")
elif opcion == 2:
    texto("La segunda opción")
elif opcion == 3:
    texto("La tercera opción")
else:
    print("Error: No elegiste una opción valida")