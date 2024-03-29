# Definición de la clase Ticket
import os.path
import pickle


class Ticket:
    def __init__(self, id, pat, veh, pag, paiscab, dist):
        self.id = id
        self.patente = pat
        self.vehiculo = veh
        self.pago = pag
        self.pais_cab = paiscab
        self.distancia = dist

    def __str__(self):
        pai = Ticket.paisToString(self.pais_cab)
        r = "Id Ticket: {:<10}".format(self.id)
        r += "Patente: {:^10}".format(self.patente)
        r += "Vehículo: {:^5}".format(self.vehiculo)
        r += "Forma de pago: {:<5}".format(self.pago)
        r += "Pais de la cabina: {:<15}".format(pai)
        r += "Distancia desde la última cabina: {:<10}".format(self.distancia)
        return r

    def paisToString(pais_cab):
        paises = ['Argentina ', 'Bolivia ', 'Brasil ', 'Paraguay ', 'Uruguay']
        return paises[pais_cab]

#Menu
def mostrar_menu():
    print('\nMenú de opciones:  -----------------Peajes de Sudamerica 4.0-----------------')
    print("1. Crear el Registro")
    print("2. Cargar datos de un ticket manualmente")
    print("3. Mostrar los datos del Registro")
    print("4. Buscar patente y mostrar sus datos")
    print("5. Buscar codigo de ticket y mostrar sus datos")
    print("6. Mostrar la cantidad de vehículos de cada combinación posible entre tipo de vehículo y país de cabina")
    print("7. Mostrar la cantidad total de vehículos contados por cada tipo de vehículo posible, y la cantidad total de vehículos contados por cada país de cabina posible.")
    print("8. Calcular y mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos")
    print("0. Salir")

#Validadores
# validaciones
def validate_intervalo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('El valor debería estar entre ' + str(inf) + ' y ' + str(sup) + ' : '))
        if n < inf or n > sup:
            print('\n\nError...vuelva a cargarlo')

    return n

def validate(num):
    n = num
    while n <= num:
        n = int(input('Valor mayor que ' + str(num) + ' : '))
        if n <= num:
            print("\n\nError....vuelva a intentarlo")
    return n

def validate_patente(pat):
    long = len(pat)
    for i in range(long):
        if pat[i].isalpha() or pat[i].isdigit():
            return 1
        else:
            print('La patente está mal cargada....solo puede tener dígitos y letras')
            return -1

#Validacion de patentes
def pais_patente(patente):
    if len(patente) == 7:
        if patente[:2].isalpha() and patente[2:5].isdigit() and patente[5:].isalpha():
            pais = 'Argentina'
        elif patente[:3].isalpha() and patente[3:].isdigit():
            pais = 'Uruguay'
        elif patente[:2].isalpha() and patente[2:].isdigit():
            pais = 'Bolivia'
        elif patente[:4].isalpha() and patente[4:].isdigit():
            pais = 'Paraguay'
        elif patente[:3].isalpha() and patente[3:4].isdigit() and patente[4:5].isalpha() and patente[5:].isdigit():
            pais = 'Brasil'
        elif patente[0:1] == " " and patente[1:5].isalpha() and patente[5:].isdigit():
            pais = 'Chile'
        else:
            pais = 'Otro'
    elif len(patente) == 6:
        if patente[0:4].isalpha() and patente[4:].isdigit():
            pais = 'Chile'
        else:
            pais = 'Otro'
    else:
        pais = 'Otro'

    return pais

#----Punto 1-----
def generar_archivo_b(acsv, nom_bin):
    if os.path.exists(acsv):
        lectura = open(acsv,"rt")
        l = lectura.readline() #primera linea
        l = lectura.readline() #segunda linea
        l = lectura.readline() #tercera linea en adelante
        arch_b = open(nom_bin, "wb")
        while l != "":
            datos = l.split(",")
            id = int(datos[0])
            pat = datos[1]
            veh = int(datos[2])
            pag = int(datos[3])
            paiscab = int(datos[4])
            dist = int(datos[5])
            res = Ticket(id, pat, veh, pag,  paiscab,  dist)
            pickle.dump(res, arch_b)
            # proxima linea
            l = lectura.readline()

        arch_b.close()
        lectura.close()

#-------Punto 2-----
# Estructura para carga por teclado
def generarTicket():
    print('Nro de ticket: ')
    id = validate_intervalo(1, 999999999)
    pat = input('Ingrese la patente: ')
    obli = 1  # Condición para forzar el incio del ciclo
    while obli == 1:
        if validate_patente(pat) != -1:
            break
        else:
            pat = input('Vuelva a ingresar la patente: ')
    print('La patente es del país: ')
    print("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")
    veh = validate_intervalo(0, 2)
    print("Ingrese la forma de pago (1: manual, 2: telepeaje): ")
    pago = validate_intervalo(1, 2)
    print("Ingrese el país donde se encuentra la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): ")
    pais = validate_intervalo(0, 4)
    dist = float(input("Ingrese la distancia recorrida desde la última cabina en kilómetros: "))
    return Ticket(id, pat, veh, pago, pais, dist)

def agregar_teclado_a_binario(a ,bin):
    if not os.path.exists(bin):
        print('Primero debe generar el archivo!')
        return
    agg = open(bin, "ab")
    pickle.dump(a, agg)
    agg.close()

#-----punto 3-----
def mostrar_datos_binario(nom_bin):
    # validacion
    if not os.path.exists(nom_bin):
        print('Primero debe generar el archivo!')
        return
    dat = open(nom_bin, 'rb')
    size = os.path.getsize(nom_bin)
    while dat.tell() < size:
        ticket = pickle.load(dat)
        patente = ticket.patente
        print(f"{ticket} -- La patente pertenece a :", pais_patente(patente))

    dat.close()

#-----Punto 4-----
def punto4(nom_bin):
    #validacion
    if not os.path.exists(nom_bin):
        print('Primero debe generar el archivo!')
        print()
        return

    pat = input('Ingrese la patente: ')
    while True:
        if validate_patente(pat) != -1:
            break
        else:
            pat = input('Vuelva a ingresar la patente: ')

    cont = 0
    dat = open(nom_bin, 'rb')
    size = os.path.getsize(nom_bin)
    while dat.tell() < size:
        ticket = pickle.load(dat)
        if pat == ticket.patente:
            print(ticket)
            cont += 1

    dat.close()
    print("Cantidad de registros que se encontraron con esa patente: ", cont)

#----Punto 5-----
def punto_5(nom_bin):
    if not os.path.exists(nom_bin):
        print('Primero debe generar el archivo!')
        print()
        return

    print('Nro de ticket: ')
    c = validate_intervalo(1, 999999999)
    dat = open(nom_bin, 'rb')
    band = False
    size = os.path.getsize(nom_bin)
    while dat.tell() < size:
        ticket = pickle.load(dat)
        if c == ticket.id:
            print(ticket)
            band = True
            break
    if not band:
        print("No existe ese codigo de ticket en el archivo")
    dat.close()

#----Punto 6-----
def cargar_matriz(nom_bin):
    if not os.path.exists(nom_bin):
        print('Primero debe generar el archivo!')
        print()
        return

    dat = open(nom_bin, 'rb')
    size = os.path.getsize(nom_bin)
    mat = [[0] * 5 for i in range(3)]
    while dat.tell() < size:
        ticket = pickle.load(dat)
        fila = ticket.vehiculo
        columna = ticket.pais_cab
        mat[fila][columna] += 1
    dat.close()
    return mat

def mostrar_matriz(mat):
    print("Resultados")
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] != 0:
                print("Del tipo:", i, "-  Pais:", j, "hay: ", mat[i][j])
    print()

#-----Punto 7-----
def punto_7(mat):
    if mat == None:
        print('Primero debe generar la matriz!')
        print()
        return

    print("Totales por tipo de vehículo")
    for f in range(len(mat)):
        ac = 0.
        for c in range(len(mat[f])):
            ac += mat[f][c]
        print("Tipo:", f, " - Cantidad:", ac)
    print()

    print("Totales por países de cabinas")
    for c in range(len(mat[f])):
        ac = 0
        for f in range(len(mat)):
            ac += mat[f][c]
        print("País:", c, " - Cantidad:", ac)
    print()

#-----Punto 8-----
def calculo_promedio(nom_bin):
    # verificar si el archivo existe
    if not os.path.exists(nom_bin):
        print('Primero debe generar el archivo!')
        print()
        return

    cont1 = acum1 = promedio = 0
    # abrir el archivo para leer
    dat = open(nom_bin, "rb")

    # recorrer
    size = os.path.getsize(nom_bin)
    while dat.tell() < size:
        ticket = pickle.load(dat)
        cont1 += 1
        acum1 += ticket.distancia
    promedio = round(acum1 / cont1, 2)
    print("El promedio de distancia recorrida es: ", promedio)
    return promedio

def punto_8(nom_bin, promedio):
    vec = []
    # verificar si el archivo existe
    if not os.path.exists(nom_bin):
        print('Primero debe generar el archivo!')
        print()
        return

    # abrir el archivo para leer
    dat = open(nom_bin, "rb")

    # recorrer
    size = os.path.getsize(nom_bin)
    while dat.tell() < size:
        ticket = pickle.load(dat)
        datos_nuevo = Ticket(ticket.id, ticket.patente, ticket.vehiculo, ticket.pago, ticket.pais_cab, ticket.distancia)
        if promedio < datos_nuevo.distancia:
            add_in_order(vec, datos_nuevo)

    # cerrar el archivo
    dat.close()

    #mostrar vector
    for i in vec:
        print(i)

def add_in_order(vec, ticket):
    n = len(vec)
    pos = n
    iz = 0  # primer elemento del vector
    de = n - 1  # ultimo elemento del vector

    while iz <= de:
        # buscar el valor central
        c = (iz + de) // 2
        if vec[c].distancia == ticket.distancia:
            pos = c
            break
        elif ticket.distancia < vec[c].distancia:
            # mover a la izquierda
            de = c - 1
        else:
            # mover a la derecha
            iz = c + 1
    # ajuste de indice en la inserción
    if iz > de:
        pos = iz

    vec[pos:pos] = [ticket]

