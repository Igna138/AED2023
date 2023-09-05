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


#Estrutura para carga por teclado
def generarTicket():
    id = int(input("Nro de Ticket: "))
    pat = input("Ingrese la patente: ")
    pais_pat = pais_patente(pat)
    veh = int(input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): "))
    pago = int(input("Ingrese la forma de pago (1: manual, 2: telepeaje): "))
    pais = int(input("Ingrese el país donde se encuentra la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): "))
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

    return pais

def cargar_arreglo_texto(fd, v):
    arch = open(fd, "r")
    linea = arch.readline() #Leemos la primera linea
    linea = arch.readline()  # Leemos de la segunda linea para delante
    while linea != "":
        v.append(generarTicketTexto(linea))
        linea = arch.readline()#siguiente linea...
    arch.close()
    return v

def display(v):
    if len(v) == 0:
        print('No hay datos cargados....')
        print()
        return

    print('Listado de tickets')
    for tickets in v:
        print(tickets)
        print()