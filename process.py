

#importamos la libreria random para poder sacar numeros random en la funcion dummies
import random

#funcion pedir ascensor
def pedirAscensor(Ppersona, Pdestino, lista):
    #declaramos estas varibles en 0 para utilizarlas despues
    distanciaMenor = 0 #distancia del ascensor mas cercano a la persona
    comparacion = 0 # distancia entre la persona y cada ascensor del for
    id = 0 # id del ascensor con la menor distancia
    #hacemos un for para recorrer la lista de todos los ascensores
    for i in lista:
        #comparamos la distancia de la persona con cada ascensor i...i+1...i+2
        comparacion = abs(Ppersona - i.posicion)
        #condicion si no esta ocupado hacer lo siguiente, si esta ocupado no hace nada
        if not i.ocupado:
            #si es el primer elemento de la lista la distancia menor es la del primer ascensor
            if i == lista[0]:
                #se guarda la distancia y el ascensor
                distanciaMenor = comparacion
                id = i.id
            else:
                #si es cualquier elemento que no sea el primero
                #compara las distancias de cada ascensor i y solo guarda la que sea menor
                #hasta ese momento
                if comparacion < distanciaMenor:
                    distanciaMenor = comparacion
                    id = i.id

    #cambiamos la posicion del ascensor utilizado hacia donde era el destino de la persona
    lista[id-1].posicion = Pdestino
    #se pone que quedo libre
    lista[id-1].ocupado = False

    #print para guardar datos el proceso
    print(distanciaMenor)
    print("Una persona pidió un ascensor desde el piso: " + str(Ppersona) + " hacia: " + str(Pdestino))
    print("El ascensor que se utilizó fue:  " + str(id) + " y quedó en la posición: " + str(lista[id-1].posicion))

#funcion para pedir los datos manuelmente que se utiliza en el main
#función para pedir los datos manualmente que se utiliza en el main
def pedirManual(lista, base, tope):
    try:
        #pedimos los datos de donde está la persona y a dónde quiere ir
        while True:
            Ppersona = int(input("Ingrese el número del piso donde está la persona: "))
            Pdestino = int(input("Ingrese el número del piso donde va la persona: "))

            if base <= Ppersona <= tope and base <= Pdestino <= tope:
                break
            else:
                print(f"Los pisos deben estar en el rango entre {base} y {tope}. Inténtalo nuevamente.")

    except ValueError:
        print("No se ingresó un número válido")
        return
    #con esos datos utilizamos la función pedirAscensor
    pedirAscensor(Ppersona, Pdestino, lista)


#funcion para generar datos aleatorios
def pedirDummie(a, b, numero, lista):

    #pun for que genere el numero de datos que la persona pone en el main
    for _ in range(numero):
        #dato randon de la ubicacion de la persona
        n1 = random.randint(a, b)
        #dato random de a donde quiere ir
        n2 = random.randint(a, b)

        #si los datos son igugales solo se le suma uno al segundo
        if n1 == n2:
            n2 += 1
        #con cada iteracion del for pedimos datos con esos datos random.
        pedirAscensor(n1, n2, lista)

#función para mostrar la lista de ascensores en cada piso
def mostrarAscensoresEnPisos(lista, base, tope):
    for piso in range(base, tope + 1):
        ascensores_en_piso = [ascensor.id for ascensor in lista if ascensor.posicion == piso]
        print(f"Piso {piso}: Ascensores en este piso: {ascensores_en_piso}")
