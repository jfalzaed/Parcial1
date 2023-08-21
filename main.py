
import ascensores
#sys es una libreria que utilizamos para terminar el programa en caso de error
import sys
import process

lascensores = []

#creación de los ascensores

#try intenta algo. si pasa un error usa el codigo contenido en exept.
try:
    #pedir el numero de ascensores
    numeroAscensores = int(input("Ingrese el numero de ascensores: "))
    #con el numero de ascensores hacemos un for desde 1 hasta el numero pedido para crear
    #objetos de tipo ascensor con sus respectivos datos.
    for i in range(1, numeroAscensores+1):
        x = ascensores.ascensor(i, 1, False)
        lascensores.append(x)

except ValueError:
    #si pasa algun error(ejem alguien pone una letra) se ejecuta este mensaje
    print("El dato es incorrecto, ingresa un dato válido")
    sys.exit()

try:
    #pedimos el piso 1 y el piso final del edificio
    basePisos = int(input("ingrese el numero de la base del edificio: "))
    topepisos = int(input("ingrese el numero del tope del edificio: "))


except ValueError:
    #error por si ponen algo que no sea un numero
    print("No metiste un numero wachin , pillin aprende a leer")
    sys.exit()


#un ciclo infinito while true que solo termina si lo indicamos con un break
while True:
    #menu de opciones para hacer con el programa
    print ("""Ingresa una de las siguientes opciones: 
    1: Pedir el ascensor de manera manual
    2: Solicitar una simulación (Dummies)
    3: Ocurre una falla en los sitemas del edificio
    4: Mostrar los ascensores que hay en cada piso
    5: ¿Quieres elegir un ascensor específico? Puedes hacerlo!!!
    6: Salir """)

    #pedimos la variable opcion como texto
    opcion = int(input("Ingrese la opción que desea: "))


    if opcion == 1:
        #utilizamos la funcion pedir manual que esta en el archivo process
        #y le pasamos la lista de los ascensores porque la necesita
        process.pedirManual(lascensores, basePisos, topepisos)
    elif opcion == 2:

        #pedimos el numero de datos dummies que quiere el usuario
        ndummies = int(input("ingresa el numero de dummies: "))

        #utilizamos la funcion pedirDummie que esta en el archivo process dandole los parametros
        #que necesita
        process.pedirDummie(basePisos,topepisos,ndummies,lascensores)

    elif opcion == 3:
        for i in range(10):
            lascensores[i].ocupado = False
        #desactivamos los demás ascensores
        for i in range(10, len(lascensores)):
            lascensores[i].ocupado = True
        print("EMERGENCIA!!!! Los primeros 10 ascensores están activos, los demás están desactivados.")


    elif opcion == 6:
        #fin de programa y ejecuta un break para parar el programa
        print("Fin del programa")
        break

    elif opcion == 4:
        process.mostrarAscensoresEnPisos(lascensores, basePisos, topepisos)


    elif opcion == 5:
        try:
            ascensor_elegido = int(input("Ingrese el número del ascensor que prefieres: "))

            if 1 <= ascensor_elegido <= len(lascensores):
                if lascensores[0].ocupado:  #verifica si la opción 3 (primeros 10 ascensores) está activa
                    if ascensor_elegido <= 10:  #verifica si el ascensor está dentro de los primeros 10
                        Ppersona = int(input("Ingrese el número del piso donde está la persona: "))
                        Pdestino = int(input("Ingrese el número del piso donde va la persona: "))
                        process.pedirAscensor(Ppersona, Pdestino, lascensores[ascensor_elegido - 1])
                    else:
                        print("No puedes elegir un ascensor que no esté dentro de los primeros 10 activos.")
                else:
                    Ppersona = int(input("Ingrese el número del piso donde está la persona: "))
                    Pdestino = int(input("Ingrese el número del piso donde va la persona: "))
                    process.pedirAscensor(Ppersona, Pdestino, lascensores[ascensor_elegido - 1])
            else:
                print(f"Elige un número de ascensor válido (1-{len(lascensores)}).")
        except ValueError:
            print("No se ingresó un número válido")

