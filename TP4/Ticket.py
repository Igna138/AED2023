# Definición de la clase Ticket
import io
import os.path
import pickle


class Ticket:
    def __init__(self, id, pat, veh, pag, paiscab, dist):
        self.id = id
        self.patente = pat
       # self.pais = pais
        self.vehiculo = veh
        self.pago = pag
        self.pais_cab = paiscab
        self.distancia = dist

    def __str__(self):
        pai = Ticket.paisToString(self.pais_cab)
        r = "Id Ticket: {:<10}".format(self.id)
        r += "Patente: {:^10}".format(self.patente)
        #r += "País: {:^10}".format(self.pais)
        r += "Vehículo: {:^5}".format(self.vehiculo)
        r += "Forma de pago: {:<5}".format(self.pago)
        r += "Pais de la cabina: {:<15}".format(pai)
        r += "Distancia desde la última cabina: {:<30}".format(self.distancia)
        return r

    def paisToString(pais_cab):
        paises = ['Argentina ', 'Bolivia ', 'Brasil ', 'Paraguay ', 'Uruguay']
        return paises[pais_cab]


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

#----Punto 1 ---
def cargar_archivo_csv(nom):
    vr = []
    arch = open(nom, "rt")
    arch.readline()
    arch.readline()
    linea = arch.readline()
    while linea != "":
        vec_linea = linea.split(",")
        id = int(vec_linea[0])
        pat = vec_linea[1]
        veh = int(vec_linea[2])
        pag = int(vec_linea[3])
        paiscab = int(vec_linea[4])
        dist = int(vec_linea[5])
        res = Ticket(id, pat, veh, pag, paiscab, dist)
        vr.append(res)
        linea = arch.readline()
    arch.close()
    return vr

def generar_archivo_b(acsv, nom_bin):
    lectura = open(acsv,"rt")
    lectura.readline()
    l=lectura.readline()
    arch_b = open(nom_bin, "wb")
    for l in lectura:
        pickle.dump(l, arch_b)
    arch_b.close()
    lectura.close()


#-------Punto 2 ---- Carga por teclado y validaciones
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

    return pais

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
    pais_pat, _ = pais_patente(pat)  # Se usa el "_" para ignorar el segundo valor que retorna la funcion
    print("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")
    veh = validate_intervalo(0, 2)
    print("Ingrese la forma de pago (1: manual, 2: telepeaje): ")
    pago = validate_intervalo(1, 2)
    print("Ingrese el país donde se encuentra la cabina (0: Argentina, 1: Bolivia, 2: Brasil, 3: Paraguay, 4: Uruguay): ")
    pais = validate_intervalo(0, 4)
    dist = float(input("Ingrese la distancia recorrida desde la última cabina en kilómetros: "))
    res =  Ticket(id, pat, veh, pago, pais, dist)
    return res

def crear_registro_p2(v):
    vr = []
    vr.append(v)
    return vr

def agregar_teclado_a_binario(v, bin):
    if not os.path.exists(bin):
        print('Primero debe generar el archivo!')
        return
    agg = open(bin, "a+b")
    for res in v:
        agrega = ""
        agrega += v.id + (v.pat) + str(v.veh) + str(v.pag) + str(v.paiscab) + str(v.dist)
        agrega += "\n"
        agg.write(agrega)
    agg.close()


#-----punto 3---mostrar todos los datos del archivo binario
def mostrar_datos_binario(nom_bin):
    if not os.path.exists(nom_bin):
        print('Primero debe generar el archivo!')
        return
    else:
        dat = open(nom_bin, 'rb')
        size = os.path.getsize(nom_bin)
        while dat.tell() < size:
            ticket = pickle.load(dat)
            if ticket[-1] == '\n':
                ticket = ticket[:-1]
            campo = ticket.split(",")
            patente = campo[1]
            print(f"{ticket} -- La patente pertenece a :", pais_patente(patente))

        dat.close()

#-----PUNTO4
def validar_patente_p4():
    pat = input('Ingrese la patente: ')
    obli = 1  # Condición para forzar el incio del ciclo
    while obli == 1:
        if validate_patente(pat) != -1:
            break
        else:
            pat = input('Vuelva a ingresar la patente: ')

def punto4(nom_bin, p):
    if not os.path.exists(nom_bin):
        print('Primero debe generar el archivo!')
        return
    else:
        cont = 0
        dat = open(nom_bin, 'rb')
        size = os.path.getsize(nom_bin)
        while dat.tell() < size:
            ticket = pickle.load(dat)
            campo = ticket.split(",")
            patente = campo[1]
            if p == patente:
                print(ticket)
                cont += 1

        dat.close()
        print("Se registraron ", cont, "archivos con esa patente")

def punto_5(nom_bin, c):
    if not os.path.exists(nom_bin):
        print('Primero debe generar el archivo!')
        return
    else:
        dat = open(nom_bin, 'rb')
        size = os.path.getsize(nom_bin)
        while dat.tell() < size:
            ticket = pickle.load(dat)
            campo = ticket.split(",")
            codigo = campo[0]
            if c == codigo:
                print(ticket)
                break
        dat.close()

def mostrar(v):
    for p in v:
        print(p)


