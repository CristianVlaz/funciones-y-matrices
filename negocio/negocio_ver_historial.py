from prettytable import PrettyTable

# Importamos funciones de 'datos'
from datos.obtener_datos import (
    obtener_paciente_por_rut, 
    obtener_citas_por_paciente,
    obtener_datos_objetos 
)


from modelos.doctor import Doctor
from negocio.negocio_pacientes import listado_pacientes 



def imprimir_historial_del_paciente():
    print("\n--- Historial de Citas por Paciente ---")

    # --- PASO 1: Validar Paciente
    paciente = None
    while not paciente:
        listado_pacientes() 
        rut_paciente = input("Ingrese RUT del Paciente para ver su historial: ")
        paciente = obtener_paciente_por_rut(rut_paciente)
        if not paciente:
            print(f"Error: Paciente con RUT {rut_paciente} no encontrado. Intente de nuevo.")

    print(f"\nMostrando historial para: {paciente.nombre_paciente} (RUT: {paciente.rut_paciente})")

    # --- PASO 2: Buscar sus citas
    citas = obtener_citas_por_paciente(paciente.id)

    if not citas:
        print("El paciente no tiene citas registradas.")
        return

    # --- PASO 3: Imprimir la tabla 
    listado_doctores = obtener_datos_objetos(Doctor)
    dict_doctores = {} 
    if listado_doctores:
        dict_doctores = {doc.id: doc.nombre_doctor for doc in listado_doctores}

    tabla = PrettyTable()
    tabla.field_names = ['ID Cita', 'Fecha', 'Hora', 'Motivo', 'Doctor']

    for cita in citas:
        nombre_doc = dict_doctores.get(cita.id_doctor, "Doctor no encontrado")
        hora_formateada = cita.hora_cita.strftime('%H:%M')

        
        tabla.add_row([
            cita.id, 
            cita.fecha_cita, 
            hora_formateada, 
            cita.motivo_cita, 
            nombre_doc.nombre_doctor
            
        ])

    print(tabla)

#resumen: Este código define la función de negocio para imprimir el historial de citas de un paciente, validando su existencia y mostrando una tabla con detalles de sus citas médicas.