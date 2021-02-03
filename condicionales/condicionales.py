edad = int(input("Introduce tu edad: "))

if edad > 18:
    print("Eres mayor de edad") #Si se quiere dejar un marcador para recordar que pondremos codigo sin que mande error debemos escribir la palabra "pass"
elif edad < 18: #Respetar la identación es indispensable, ya que de no hacerse Python lanzará un error y no leera el programa
    print("Eres menor de edad")
else:
    print("Tienes 18 años")