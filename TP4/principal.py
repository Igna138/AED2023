from ticket import *

def principal():
    opcion = -1
    flag_1 = False
    archivo_csv = "peajes-tp4.csv"
    bin_arch = "peajes.dat"

    while opcion != 0:
        mostrar_menu()
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            if not flag_1:
                generar_archivo_b(archivo_csv, bin_arch)
                flag_1 = True
                print("Archivo creado con exito!!")
            else:
                n = input("Esta seguro de crear de nuevo el archivo, se perdera todo lo anterior.. Responda (SI o NO):")
                if n.lower() == "si":
                    generar_archivo_b(archivo_csv, bin_arch)
                    print("El archivo cambio !")
                else:
                    print("Ok, queda como antes..")


        elif opcion == 2:
            a = generarTicket()
            agregar_teclado_a_binario(a, bin_arch)

        elif opcion == 3:
            mostrar_datos_binario(bin_arch)

        elif opcion == 4:
            punto4(bin_arch)

        elif opcion == 5:
            punto_5(bin_arch)

        elif opcion == 6:
            mat = cargar_matriz(bin_arch)
            if mat != None:
                mostrar_matriz(mat)

        elif opcion == 7:
            mat = cargar_matriz(bin_arch)
            if mat != None:
                punto_7(mat)

        elif opcion == 8:
            prom = calculo_promedio(bin_arch)
            punto_8(bin_arch, prom)

        elif opcion == 0:
            print("-----FIN DEL PROGAMA-----")

        else:
            print("\tOpcion invalida...por favor vuelva a cargar otra opcion..")

if __name__ == '__main__':
    principal()