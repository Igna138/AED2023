#Definicion de la clase Ticket
class Ticket():
    def __init__(self, id, pat, pais, veh, pag, paiscab, dist):
        self.id = id
        self.patente = pat
        self.pais = pais
        self.vehiculo = veh
        self.pago = pag
        self.pais_cab = paiscab
        self.distancia = dist

    def __str__(self):
        pai = Ticket.paisToString(self.pais_cab)
        r = "Id Ticket: {:<10}".format(self.id)
        r += "Patente: {:^10}".format(self.patente)
        r += "Pais: {:^10}".format(self.pais)
        r += "Vehiculo: {:^5}".format(self.vehiculo)
        r += "Forma de pago: {:<5}".format(self.pago)
        r += "Pais de la cabina: {:<15}".format(pai)
        r += "Distancia desde la ultima cabina: {:<30}".format(self.distancia)
        return r

    def paisToString(pais_cab):
        paises = ['Argentina ', 'Bolivia ', 'Brasil ', 'Paraguay ', 'Uruguay']
        return paises[pais_cab]

#validaciones
def validate_intervalo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('El valor deberia estar entre ' + str(inf) + ' y ' + str(sup) + ' : '))
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
            continue
        else:
            print('La patente esta mal cargada....solo puede tener digitos y letras')
            return -1
    return

#Estrutura para carga por teclado
def generarTicket():
    print('Nro de ticket: ')
    id = validate_intervalo(1, 999999999)
    pat = input('Ingrese la patente: ')
    obli = 1 #Condicion para forzar el incio del ciclo
    while obli == 1:
        if validate_patente(pat) != -1:
            break
        else:
            pat = input('Vuelva a ingresar la patente: ')
    print('La patente es del pais: ')
    pais_pat, _ = pais_patente(pat) #Se usa el "_" para ignorar el segundo valor que retorna la funcion
    print("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")
    veh = validate_intervalo(0, 2)
    print("Ingrese la forma de pago (1: manual, 2: telepeaje): ")
    pago = validate_intervalo(1, 2)
    print("Ingrese el país donde se encuentra la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): ")
    pais = validate_intervalo(0, 4)
    dist = float(input("Ingrese la distancia recorrida desde la última cabina en kilómetros: "))
    return Ticket(id, pat, pais_pat, veh, pago, pais, dist)

#Estructura carga por archivo
def generarTicketTexto(linea):
    id = int(linea[0:10])
    pat = linea[10:17]
    pais_pat, _ = pais_patente(pat)
    veh = int(linea[17:18])
    pago = int(linea[18:19])
    pais = int(linea[19:20])
    dist = float(linea[20:23])
    return Ticket(id, pat, pais_pat, veh, pago, pais, dist)

#Identificador de patentes
def pais_patente(patente):
    if len(patente) == 7:
        if patente[:2].isalpha() and patente[2:5].isdigit() and patente[5:].isalpha():
            pais = 'Argentina'
            cod = 0
        elif patente[:3].isalpha() and patente[3:].isdigit():
            pais = 'Uruguay'
            cod = 1
        elif patente[:2].isalpha() and patente[2:].isdigit():
            pais = 'Bolivia'
            cod = 2
        elif patente[:4].isalpha() and patente[4:].isdigit():
            pais = 'Paraguay'
            cod = 3
        elif patente[:3].isalpha() and patente[3:4].isdigit() and patente[4:5].isalpha() and patente[5:].isdigit():
            pais = 'Brasil'
            cod = 4
        elif patente[0:1] == " " and patente[1:5].isalpha() and patente[5:].isdigit():
            pais = 'Chile'
            cod = 5
        else:
            pais = 'Otro'
            cod = 6
    elif len(patente) == 6:
        if patente[0:4].isalpha() and patente[4:].isdigit():
            pais = 'Chile'
            cod = 5
        else:
            pais = 'Otro'
            cod = 6
    else:
        pais = 'Otro'
        cod = 6

    return pais, cod

#Ordena arreglo por codigo
def ordenar_men_may(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]

#Calculo del importe total
def imp_tot(pais, tipo, pago):
    importe_final = 0
    # Pais de la cabina de peaje
    if pais == 2:
        importe_base = 400
    elif pais == 1:
        importe_base = 200
    else:
        importe_base = 300
    # Tipo de vehiculo
    if tipo == 0:
        importe_base *= 0.5
    elif tipo == 2:
        importe_base *= 1.6

    # Aplicación del descuento/cargo por telepeaje
    if pago == 2:
        importe_final = int(importe_base * 0.9)
    else:
        importe_final = int(importe_base)

    return importe_final

#Opcion 1
def cargar_arreglo_texto(fd, v):
    arch = open(fd, "r")
    linea = arch.readline() #Leemos la primera linea
    linea = arch.readline()  # Leemos de la segunda linea para delante
    while linea != "":
        v.append(generarTicketTexto(linea))
        linea = arch.readline()#siguiente linea...
    arch.close()
    return v

#Opcion 2
def carga_arreglo_manual(v, bandera):
    print("Ingrese la cantidad de tickets que quiere registrar: ")
    n = validate(0)
    print()

    print("Ingrese datos del ticket: ")
    bandera = False
    for i in range(n):
        v.append(generarTicket())
    return v, bandera

#opcion3
def display(v, bandera):
    if len(v) == 0:
        print('No hay datos cargados....')
        print()
        return

    ordenar_men_may(v)
    bandera = True
    print('Listado de tickets')
    for tickets in v:
        print(tickets)
        print()
    return bandera

#Opcion 4
def busqueda_por_patente(v):
    p = input("ingrese la patente a buscar: ")
    x = int(input("ingrese la cabina a buscar: "))
    for i in range(len(v)):
        if p == v[i].patente and x == v[i].pais_cab:
            return v[i]
    return -1

#Opcion 5
def busqueda_por_codigo(v, bandera):
    n = len(v)
    izq, der = 0, n - 1
    t = int(input("Ingrese el código de ticket a buscar:  "))
    if bandera:
        while izq <= der:
            c = (izq + der) // 2
            if v[c].id == t:
                if v[c].pago == 1:
                    v[c].pago = 2
                else:
                    v[c].pago = 1
                return v[c]

            elif t > v[c].id:
                izq = c + 1
            else:
                der = c - 1
        return -1
    else:
        for i in range(len(v)):
            if v[i].id == t:
                if v[i].pago == 1:
                    v[i].pago = 2
                else:
                    v[i].pago = 1
                return v[i]
        return -1

#Opcion 6
def cont_veh(v):
    if len(v) == 0:
        print('No hay datos cargados....')
        print()
        return

    cont = [0] * 7
    for i in range(len(v)):
        _, pos = pais_patente(v[i].patente)
        cont[pos] += 1

    print("--------Cantidad de vehiculos de cada pais que pasaron por las cabinas--------")
    print("Cantidad de Argentina: ", cont[0])
    print("Cantidad de Uruguay: ", cont[1])
    print("Cantidad de Bolivia: ", cont[2])
    print("Cantidad de Paraguay: ", cont[3])
    print("Cantidad de Brasil: ", cont[4])
    print("Cantidad de Chile: ", cont[5])
    print("Cantidad de Otros paises:", cont[6])

#Opcion 7
def import_acumulado(v):
    if len(v) == 0:
        print('No hay datos cargados....')
        print()
        return

    cont = [0] * 3
    for i in range(len(v)):
        final = imp_tot(v[i].pais_cab, v[i].vehiculo, v[i].pago)
        if v[i].vehiculo == 0:
            cont[0] += final
        elif v[i].vehiculo == 1:
            cont[1] += final
        else:
            cont[2] += final

    print('----------------Pagos acumulados por cada tipo de vehiculo---------------')
    print('Importe acumulado para las motocicletas: $', cont[0])
    print('Importe acumulado para las autos: $', cont[1])
    print('Importe acumulado para las camiones: $', cont[2])

    return cont

#Opcion 8
def mayor_total(cont):
    if len(cont) == 0:
        print('No hay datos cargados....')
        print()
        return

    n = cont[0] + cont[1] + cont[2]
    if cont[0] > cont[1] and cont[0] > cont[2]:
        print('El tipo de vehiculo con mayor monto acumulado es la motocicleta y es de $', cont[0])
        porc = round((cont[0] * 100) / n, 2)
        print(' Porcentaje que representa este monto sobre los montos totales: ', porc, '%')
        return
    elif cont[1] > cont[2]:
        print('El tipo de vehiculo con mayor monto acumulado son los autos y es de $', cont[1])
        porc = round((cont[1] * 100) / n, 2)
        print(' Porcentaje que representa este monto sobre los montos totales: ', porc, '%')
        return
    else:
        print('El tipo de vehiculo con mayor monto acumulado son los camiones y es de $', cont[2])
        porc = round((cont[2] * 100) / n, 2)
        print(' Porcentaje que representa este monto sobre los montos totales: ', porc, '%')
        return

#Opcion 9
