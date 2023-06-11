FD = "peaje25.txt"

# Consigna 1
def idioma_esp_por(linea):
    if "PT" in linea:
        idioma = "Portugués"
    else:
        idioma = "Español"

    return idioma

# Consigna 2
def veh_proc():
    pass

# Consigna 3
def imp_tot():
    pass

# Consigna 4
def cant_patente():
    pass

# Consigna 5
def import_total_final():
    pass

# Consigna 6
def otro_pais():
    pass

# Consigna 7
def dist_prom():
    pass

# Programa principal
def test():
    # Aqui se muestran los resultados y prints del script

    # Se abre el archivo
    arch = open(FD, "r")
    linea = arch.readline()

    # Punto 1
    idioma = idioma_esp_por(linea)

    #Punto 2
    linea = arch.readline() # Leemos de la segunda linea para adelante

    while linea != "":
        patente = linea[0:7]
        tipo = int(linea[7])
        forma_pago = int(linea[8])
        pais = int(linea[9])
        distancia = int(linea[10:13])





    # Se cierra el archivo
    arch.close()

    # Visualizacion de resultados...
    print('(r1) - Idioma a usar en los informes: ', idioma)

    print()
    #print('(r2) - Cantidad de patentes de Argentina:', carg)
    #print('(r2) - Cantidad de patentes de Bolivia:', cbol)
    #print('(r2) - Cantidad de patentes de Brasil:', cbra)
    #print('(r2) - Cantidad de patentes de Chile:', cchi)
    #print('(r2) - Cantidad de patentes de Paraguay:', cpar)
    #print('(r2) - Cantidad de patentes de Uruguay:', curu)
    #print('(r2) - Cantidad de patentes de otro pais;', cotr)

    print()
    #print('(r3) - Importe acumulado total de importes finales: ', imp_acu_total)

    print()
    #print('(r4) - Primera patente del archivo: ', primera, '- Frecuencia de aparicion: ', cpp)

    print()
    #print('(r5) - Mayor importe final cobrado:', mayimp, ' - Patente a la que se cobró ese importe: ', maypat)

    print()
    #print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')

    print()
    #print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas:', prom, '\bkm')

if __name__ == "__main__":
    test()