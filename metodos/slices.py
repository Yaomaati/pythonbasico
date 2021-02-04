#Los slices nos sirven para manipular la cadena de texto a partir de los indices

nombre="Pancrasio"

print("Imprimiendo el indice '3' de Pancrasio: " + nombre[3])

print("Imprimiendo el slice '0:3' de Pancrasio: " + nombre[0:3]) #Esto nos separa la cadena desde el inicio hasta un sitio ANTES de la posición "3", recordando que nuestro conteo comienza en 0

print("Imprimiendo el indice '3' de Pancrasio: " + nombre[:3])#Cumple la misma función que el anterior, ya que por default toma el espacio vació como el inicio de la cadena

print("Imprimiendo del indice '3' en adelante de Pancrasio: " + nombre[3:])#En éste caso el punto de inicio sería el '3' y al no haber un parametro final, seguirá hasta terminar la cadena

print("Imprimiendo Pancrasio usando slices de 2 en 2: " + nombre[0::2])#Aqui marca el conteo del inicio hasta el final de la cadena, pero haciendo saltos del tamaño marcado en el tercer parametro

print("Imprimiendo Pancrasio del inicio al final usando slices: " + nombre [::-1])#Esto hará un conteo de los caracteres de manera regresiva, es decir, mostrará el nombre al revéz