import os.path

from ticket import *

def principal():
    opcion = -1
    flag_1 = False
    archivo_csv= "peajes-tp4.csv"
    vector_teclado=[]
    #vp = cargar_archivo_csv(archivo_csv)
    bin = "peajes.dat"


    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            if not flag_1:
                generar_archivo_b(archivo_csv, bin)
                flag_1 = True
                print("Archivo creado con exito!!")
            else:
                n = input("Esta seguro de crear de nuevo el archivo, se perdera todo lo anterior.. Responda (SI o NO):")
                if n.lower == "si":
                    generar_archivo_b(archivo_csv, bin)
                    break
                else:
                    print("Ok, queda como antes..") #Revisar este print

        elif opcion == 2:
            v =  generarTicket()
            vector_teclado = crear_registro_p2(v)
            agregar_teclado_a_binario(vector_teclado, bin)

        elif opcion == 3:
            mostrar_datos_binario(bin) #Revisar

        elif opcion == 4:
            #p = validar_patente_p4() Revisar validacion
            p = input("ingrese una patente a buscar: ")
            punto4(bin, p)



        elif opcion == 5:
            print('Nro de ticket: ')
            #c = validate_intervalo(1, 999999999) Revisar validaciones
            c = input("Ingrese codigo a buscar: ")
            punto_5(bin, c)
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