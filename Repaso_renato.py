import random
import csv

# Paso 1: Asignar sueldos aleatorios
def asignar_sueldos(empleados):
    sueldos = {empleado: random.randint(300000, 2500000) for empleado in empleados}
    return sueldos

# Paso 2: Clasificar sueldos
def clasificar_sueldos(sueldos):
    menores = {}
    medios = {}
    superiores = {}
    
    for empleado, sueldo in sueldos.items():
        if sueldo < 800000:
            menores[empleado] = sueldo
        elif sueldo <= 2000000:
            medios[empleado] = sueldo
        else:
            superiores[empleado] = sueldo
    
    return menores, medios, superiores

# Paso 3: Ver estadísticas
def ver_estadisticas(sueldos):
    sueldos_lista = list(sueldos.values())
    max_sueldo = max(sueldos_lista)
    min_sueldo = min(sueldos_lista)
    promedio = sum(sueldos_lista) // len(sueldos_lista)
    
    return max_sueldo, min_sueldo, promedio

# Paso 4: Reporte de sueldos
def reporte_sueldos(sueldos):
    reporte = {}
    for empleado, sueldo in sueldos.items():
        descuento_salud = sueldo * 7 // 100
        descuento_afp = sueldo * 12 // 100
        sueldo_liquido = sueldo - descuento_salud - descuento_afp
        reporte[empleado] = {
            "Sueldo Base": sueldo,
            "Descuento Salud": descuento_salud,
            "Descuento AFP": descuento_afp,
            "Sueldo Líquido": sueldo_liquido
        }
    return reporte

# Paso 5: Exportar datos a CSV
def exportar_csv(reporte, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for empleado, detalles in reporte.items():
            writer.writerow([empleado, detalles["Sueldo Base"], detalles["Descuento Salud"], detalles["Descuento AFP"], detalles["Sueldo Líquido"]])

# Función principal con menú
def main():
    empleados = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", 
                 "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

    sueldos = {}

    while True:
        print("\nMenú de opciones:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            sueldos = asignar_sueldos(empleados)
            print("Sueldos asignados aleatoriamente.")
        elif opcion == '2':
            if not sueldos:
                print("Primero debe asignar los sueldos.")
            else:
                menores, medios, superiores = clasificar_sueldos(sueldos)
                while True:
                    print("\nClasificar sueldos:")
                    print("1. Sueldos menores a $800.000")
                    print("2. Sueldos entre $800.000 y $2.000.000")
                    print("3. Sueldos superiores a $2.000.000")
                    print("4. Volver al menú principal")
                    aux_opcion = input("Seleccione una opción: ")

                    if aux_opcion == '1':
                        print("\nSueldos menores a $800.000:")
                        for empleado, sueldo in menores.items():
                            print(f"{empleado}: {sueldo}")
                        print(f"TOTAL: {len(menores)}")
                    elif aux_opcion == '2':
                        print("\nSueldos entre $800.000 y $2.000.000:")
                        for empleado, sueldo in medios.items():
                            print(f"{empleado}: {sueldo}")
                        print(f"TOTAL: {len(medios)}")
                    elif aux_opcion == '3':
                        print("\nSueldos superiores a $2.000.000:")
                        for empleado, sueldo in superiores.items():
                             print(f"{empleado}: {sueldo}")
                        print(f"TOTAL: {len(superiores)}")
                    elif aux_opcion == '4':
                        break
                    else:
                        print("Opción no válida. Intente de nuevo.")
        elif opcion == '3':
            if not sueldos:
                print("Primero debe asignar los sueldos.")
            else:
                max_sueldo, min_sueldo, promedio = ver_estadisticas(sueldos)
                print(f"\nEstadísticas de sueldos:")
                print(f"Sueldo más alto: {max_sueldo}")
                print(f"Sueldo más bajo: {min_sueldo}")
                print(f"Promedio de sueldos: {promedio}")
        elif opcion == '4':
            if not sueldos:
                print("Primero debe asignar los sueldos.")
            else:
                reporte = reporte_sueldos(sueldos)
                exportar_csv(reporte, 'reporte_sueldos.csv')
                suma_total_sueldos = sum([detalles['Sueldo Base'] for detalles in reporte.values()])
                print("Reporte de sueldos generado y exportado a 'reporte_sueldos.csv'.")
                print(f"\nSuma total de sueldos: {suma_total_sueldos}")
                print("\nReporte de sueldos:")
                for empleado, detalles in reporte.items():
                    print(f"{empleado}: Sueldo Base: {detalles['Sueldo Base']}, Descuento Salud: {detalles['Descuento Salud']}, Descuento AFP: {detalles['Descuento AFP']}, Sueldo Líquido: {detalles['Sueldo Líquido']}")
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la función principal
main()

