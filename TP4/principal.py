import os.path

from Ticket import *

def principal():
    opcion = -1
    flag_1 = False
    archivo_csv= "peajes-tp4.csv"
    vp = cargar_archivo_csv(archivo_csv)
    bin = "peajes.dat"


    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            generar_archivo_b(vp, bin)
            print("Archivo creado con exito!!")



        elif opcion == 2:
            generarTicket()

        elif opcion == 3:
            mostrar_datos_binario(bin) #Revisar

        elif opcion == 4:
            pass

        elif opcion == 5:
            pass

        elif opcion == 6:
            pass

        elif opcion == 7:
            pass

        elif opcion == 8:
            pass

        elif opcion == 0:
            print("-----FIN DEL PROGAMA-----")

        else:
            print("\tOpcion invalida...por favor vuelva a cargar otra opcion..")

if __name__ == '__main__':
    principal()