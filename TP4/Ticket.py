# Definición de la clase Ticket
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

def generar_archivo_b(vcsv, nom_bin):
    vb= []
    arch_b = open(nom_bin, "wb")
    for p in vcsv:
        pickle.dump(p, arch_b)
    arch_b.close()


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
    return Ticket(id, pat, pais_pat, veh, pago, pais, dist)



#-----punto 3---mostrar todos los datos del archivo binario
def mostrar_datos_binario(nom_bin):
    vp=[]
    arch = open(nom_bin, "rb")
    for i in range(len(nom_bin)):
        vp.append(i)
        print(vp)
    arch.close()





def mostrar(v):
    for p in v:
        print(p)


