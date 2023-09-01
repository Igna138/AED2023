#Definicion de la clase Ticket
class Ticket():
    def __init__(self, id, pat, veh, pag, pais, dist):
        self.id = id
        self.patente = pat
        self.vehiculo = veh
        self.pago = pag
        self.pais = pais
        self.distancia = dist

    def __str__(self):
        pai = Ticket.paisToString(self.pais)
        r = "Id Ticket: {:<5}".format(self.id)
        r += "Patente: {:^15}".format(self.patente)
        r += "Vehiculo: {:>5}".format(self.vehiculo)
        r += "Forma de pago: {:<15}".format(self.pago)
        r += "Pais: {:<15}".format(pai)
        r += "Distancia desde la ultima cabina: {:<15}".format(self.distancia)
        return r

    def paisToString(pais):
        paises = ['Argentina ', 'Bolivia ', 'Brasil ', 'Paraguay ', 'Uruguay']
        return paises[pais]

#Opcion si se carga por teclado
def generarTicket():
    id = int(input("Nro de Ticket: "))
    pat = input("Ingrese la patente: ")
    veh = int(input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): "))
    pago = int(input("Ingrese la forma de pago (1: manual, 2: telepeaje): "))
    pais = int(input("Ingrese el país donde se encuentra la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): "))
    dist = float(input("Ingrese la distancia recorrida desde la última cabina en kilómetros: "))
    return Ticket(id, pat, veh, pago, pais, dist)