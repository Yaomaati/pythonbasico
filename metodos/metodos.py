#Los metodos son funciones que atienden a un tipo de dato en particular, a un "objeto"
#En el caso de las cadenas de textos hay un par que nos pueden servir.

nombre = "DoNoVaN  "
print("Datos de entrada: " + nombre)


print("Metodo 'upper' convierte un texto en todo mayúsculas: " + nombre.upper())

print("Metodo 'capitalize' solo la letra inicial se vuelve mayúscula: " + nombre.capitalize())

print("Metodo 'strip' elimina los espacios al inicio o al final de la cadena: " + nombre.strip())

print("Metodo 'lower' convierte en minúsculas la cadena de texto: " +nombre.lower())

print("Metodo 'replace' sustituye una letra por otra, aqui cambio las 'o', por letras 'i': " + nombre.replace("o","i"))

#Tambien tenemos los "indices" que se utilizan con corchetes " [] ", y en un principio nos sirven para ubicar la posición de un carácter en una cadena de texto.
#Hay que tomar en cuenta que el "conteo" de los caracteres comienzan a partir del numero cero "0"

print("Indice 0 de mi nombre: " + nombre[0])

print("Indice 3 de mi nombre: " + nombre[3])

print("Indice 5 de mi nombre: " + nombre[5])

#Tambien contamos con "len" que nos devolverá el conteo de caracteres que componen una cadena de texto

len("Donovan") #Aqui contaria la cantidad de caracteres de mi nombre