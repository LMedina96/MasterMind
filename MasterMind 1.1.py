import random
import sqlite3

def generador(a, b):

    cadena = random.randrange(a, b)
    return cadena

#Dificultad
def inicio():
    nivel = None

    while nivel != "1" and nivel != "2" and nivel != "3":
        print("Escoja el nivel de dificultad: ")
        print("Escriba '1' Para el primer nivel (3 digitos)")
        print("Escriba '2' Para el segundo nivel (4 digitos)")
        print("Escriba '3' Para el tercer nivel (5 digitos)")
        nivel = input()
        if nivel != "1" and nivel != "2" and nivel != "3":
            print("Por favor ingrese una de las tres opciones.")

    if nivel == "1":
        vidas = 10
        nrand1 = 100
        nrand2 = 999
    elif nivel == "2":
        vidas = 7
        nrand1 = 1000
        nrand2 = 9999
    elif nivel == "3":
        vidas = 5
        nrand1 = 10000
        nrand2 = 99999

    return nrand1, nrand2, vidas, nivel

def comparacion(numgen, v, niv):
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
                v += 1
    if listum == lisnumgen:
        print("Has adivinado el numero!")
        
        score(niv, v, numgen)

        input()
        exit()
    else:
        descontar_vidas(v)

    return listum

def descontar_vidas(v):
    print("\nTe quedan {} vidas".format(v))
    if v == 0:
        print("Perdiste :(")
        quit()

def score(niv, vid, cod):
    db = sqlite3.connect("HighScore.db")
    cursor = db.cursor()

    print("¡Felicidades! Ingrese su apodo")
    nom = input()

    cursor.execute("INSERT INTO 'Nivel {}' VALUES ('{}', {}, {})".format(niv, nom, vid, cod))

    #cursor.execute("CREATE TABLE 'Nivel 1' ('Apodo' TEXT, 'Vidas' INTEGER, 'Numero' INTEGER)")
    #cursor.execute("CREATE TABLE 'Nivel 2' ('Apodo' TEXT, 'Vidas' INTEGER, 'Numero' INTEGER)")
    #cursor.execute("CREATE TABLE 'Nivel 3' ('Apodo' TEXT, 'Vidas' INTEGER, 'Numero' INTEGER)")

    db.commit()
    db.close()

print("¡Bienvenidos a Master Mind!")
print("El objetivo del juego es sencillo, un numero sera generado aleatoriamente según el nivel de dificultad que escoja.\nSe le pedirá ingresar un numero y si corresponde el mismo numero en el lugar exacto al numero generado se le mostrata un mensaje de acierto.\nUna vez que acierte todos los numeros ¡ganara!\n")

n1, n2, vida, nivel = inicio()
ngenerado = generador(n1, n2)
while ngenerado != comparacion:
    vida -= 1

    comparacion(ngenerado, vida, nivel)