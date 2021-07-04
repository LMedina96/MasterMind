import random

def generador(a, b):
    cadena = random.randrange(a, b)
    return cadena

#Dificultad
def inicio():

    print("Escoja el nivel de dificultad: ")
    print("Escriba '1' Para el primer nivel (3 digitos): ")
    print("Escriba '2' Para el segundo nivel (4 digitos): ")
    print("Escriba '3' Para el tercer nivel (5 digitos): ")
    nivel = input()

    if nivel == "1":
        nrand1 = 100
        nrand2 = 999
    elif nivel == "2":
        nrand1 = 1000
        nrand2 = 9999
    elif nivel == "3":
        nrand1 = 10000
        nrand2 = 99999

    return nrand1, nrand2

def comparacion(numgen):
    listum = []
    lisnumgen = []
    print("Escriba el numero que piense que se genero: ")
    num = input()
    strnumgen = str(numgen)
    for i in num:
        listum.append(i)
    for n in strnumgen:
        lisnumgen.append(n)

    #Comparar digito por digito
    for j in range(len(num)):
        for k in range(len(strnumgen)):
            if num[j] == strnumgen[j] and j == k:
                print("has acertado el numero: {} en la posición {}".format(strnumgen[j], j + 1))
    if listum == lisnumgen:
        print("Has adivinado el numero!")
        input()
        exit()

    return listum

    
n1, n2 = inicio()
ngenerado = generador(n1, n2)
while ngenerado != comparacion:
    comparacion(ngenerado)