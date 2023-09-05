from ticket import *

def principal():
    FD = "peajes-tp3.txt"
    tickets = []
    opc = 0
    while opc != 10:
        print('\nMenu de opciones:  -----------------Peajes de Sudamerica 3.0-----------------')
        print('1. Crear el arreglo de registros desde un archivo .txt')
        print('2. Cargar por teclado los datos de un ticket al arreglo')
        print('3. Mostrar todos los registros del arreglo, ordenados por código de ticket (de menor a mayor)')
        print('4. Buscador de patentes por pais')
        print('5. Buscador de codigo de ticket para invertir el codigo de pago')
        print('6. Determinar la cantidad de vehículos de cada país que pasaron por las cabinas, contando también los vehículos que no son de ninguno de los siete paises básicos')
        print('7. Determinar el importe acumulado por pagos de tickets, por cada uno de los posibles tipos de vehiculo')
        print('8. Determinar y mostrar cuál fue el tipo de vehículo con mayor monto acumulado y porcentaje representa ')
        print('9. Calcular y mostrar la distancia promedio desde la última cabina recorrida entre todos los vehículos del arreglo, e informar cuántos de los vehículos recorrieron una distancia mayor a ese promedio.')
        print('10. Salir')
        print()

        opc = int(input('Elija una de las opciones:\t'))

        if opc == 1:
            #Validacion
            if len(tickets) == 0:
                cargar_arreglo_texto(FD, tickets)
            else:
                opc2 = input("Esta seguro de esta operacion? Se eliminara todo contenido del arreglo y se sobreescribira con el del archivo (Elija SI o NO): ")
                if opc2.lower() == "si":
                    tickets = []
                    cargar_arreglo_texto(FD, tickets)

        elif opc == 2:
            pass

        elif opc == 3:
            display(tickets)

        elif opc == 4:
            pass

        elif opc == 5:
            pass

        elif opc == 6:
            pass

        elif opc == 7:
            pass

        elif opc == 8:
            pass

        elif opc == 9:
            pass

        elif opc == 10:
            print('-----FIN DEL PROGRAMA-----')

if __name__ == '__main__':
    principal()