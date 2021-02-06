import random


def key_gen(): #Creamos una función que contenga los caracteres necesarios para generar la contraseña usando listas separadas.

    uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lower_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    symbols = ['@','#','€','¿','?','!','$','%','&']
    numbers = ['0','1','2','3','4','5','6','7','8','9']

    characters = uppercase + lower_case + symbols + numbers #Despues concatenamos las listas en un solo bloque y lo asignamos a una variable

    password = [] #Creamos una lista vacía en la cuál almacenaremos la contraseña final

    for i in range(15): #Usando un ciclo flor, asignaremos el largo de la contraseña en 15 caracteres
        random_password = random.choice(characters) #Usaremos el metodo 'random.choice' para que en cada ciclo elija un caracter al azar de toda la lista
        password.append(random_password) #Despues, haremos que el caracter seleccionado sea agregado a la lista con el metodo '.append()'

    password = ''.join(password) #convertimos la lista completa en una cadena de texto
    return password #Y el resultado final será devuelto por la función como la variable password


def run():
    password = key_gen() #Llamamos a nuestra función 'key_gen' para que nos genere la contraseña nueva
    print("Your new password is: " + password) #Y la imprimimos



if __name__ == "__main__":
    run()