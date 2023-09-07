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
    pais_pat = pais_patente(pat)
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
    pais_pat = pais_patente(pat)
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

#Ordena arreglo por codigo
def ordenar_men_may(v):
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i].id > v[j].id:
                v[i], v[j] = v[j], v[i]

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
def carga_arreglo_manual(v):
    print("Ingrese la cantidad de tickets que quiere registrar: ")
    n = validate(0)
    print()

    print("Ingrese datos del ticket: ")
    for i in range(n):
        v.append(generarTicket())

    return v


#opcion3
def display(v):
    if len(v) == 0:
        print('No hay datos cargados....')
        print()
        return

    ordenar_men_may(v)
    print('Listado de tickets')
    for tickets in v:
        print(tickets)
        print()

#Opcion 4

#Opcion 5

#Opcion 6
