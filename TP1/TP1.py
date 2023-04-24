# Ingreso de datos
patente = input("Ingrese la patente del vehículo: ")
tipo_vehiculo = int(input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): "))
forma_pago = int(input("Ingrese la forma de pago (1: manual, 2: telepeaje): "))
pais = int(input("Ingrese el país donde se encuentra la cabina (0: Argentina, 1: Brasil, 2: Bolivia, 3: Paraguay, 4: Uruguay): "))
distancia = float(input("Ingrese la distancia recorrida desde la última cabina en kilómetros: "))

# Validación de la patente
if len(patente) == 7:
    es_patente_valida = True
else:
    es_patente_valida = False

# Cálculo del importe básico
if pais == 1:
    importe_base = 400
elif pais == 2:
    importe_base = 200
else:
    importe_base = 300

if tipo_vehiculo == 0:
    importe_base *= 0.5
elif tipo_vehiculo == 2:
    importe_base *= 1.6


# Aplicación del descuento por telepeaje
if forma_pago == 2:
    importe_final = importe_base * 0.9
else:
    importe_final = importe_base

# Cálculo del valor promedio pagado por kilómetro recorrido
if distancia != 0:
    valor_promedio_por_kilometro = importe_final / distancia
else:
    valor_promedio_por_kilometro = importe_final

# Impresión de resultados
print()
if es_patente_valida:
    if pais == 0:
        print("El vehículo es de Argentina")
    elif pais == 1:
        print("El vehículo es de Brasil")
    elif pais == 2:
        print("El vehículo es de Bolivia")
    elif pais == 3:
        print("El vehículo es de Paraguay")
    elif pais == 4:
        print("El vehículo es de Uruguay")
else:
    print("El vehículo es de otro pais")


print("El importe básico a pagar por el vehículo es:", importe_base)
print("El valor final del ticket es:", importe_final)
print("El valor promedio pagado por kilómetro recorrido es:", valor_promedio_por_kilometro)
