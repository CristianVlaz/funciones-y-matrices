from datetime import date # Para la fecha de emision
from prettytable import PrettyTable

# Importamos funciones de 'datos'
from datos.obtener_datos import (
    obtener_paciente_por_rut, 
    obtener_citas_por_paciente,
    obtener_receta_por_id_cita, # <-- La que acabamos de agregar
    obtener_datos_objetos # Para doctores
)
from datos.insertar_datos import insertar_objeto

# Importamos los "moldes"
from modelos.receta import Receta
from modelos.doctor import Doctor

# Importamos funciones de otros 'negocios'
from negocio.negocio_pacientes import listado_pacientes


def generar_nueva_receta():
    print("\n--- Generar Nueva Receta Médica ---")

    # --- PASO 1: Validar Paciente ---
    paciente = None
    while not paciente:
        listado_pacientes()
        rut_paciente = input("Ingrese RUT del Paciente al que se le emitirá la receta: ")
        paciente = obtener_paciente_por_rut(rut_paciente)
        if not paciente:
            print(f"Error: Paciente con RUT {rut_paciente} no encontrado.")

    # --- PASO 2: Mostrar sus citas (para que el usuario elija una) ---
    print(f"\nCitas registradas para: {paciente.nombre_paciente}")
    citas = obtener_citas_por_paciente(paciente.id)

    if not citas:
        print("El paciente no tiene citas registradas. No se puede generar una receta.")
        return

    # Imprimimos la tabla de citas (similar a negocio_historial.py)
    listado_doctores = obtener_datos_objetos(Doctor)
    dict_doctores = {doc.id: doc.nombre_doctor for doc in listado_doctores}
    tabla_citas = PrettyTable()
    tabla_citas.field_names = ['ID Cita', 'Fecha', 'Hora', 'Motivo', 'Doctor', 'Receta']

    citas_validas_para_receta = [] # Guardamos IDs de citas que SÍ existen

    for cita in citas:
        # Regla de Negocio: Revisamos si la cita ya tiene receta
        receta_existente = obtener_receta_por_id_cita(cita.id)
        tiene_receta = "Sí" if receta_existente else "No"

        nombre_doc = dict_doctores.get(cita.id_doctor, "N/A")
        hora_formateada = cita.hora_cita.strftime('%H:%M')

        tabla_citas.add_row([
            cita.id, 
            cita.fecha_cita, 
            hora_formateada, 
            cita.motivo_cita, 
            nombre_doc,
            tiene_receta # Mostramos si ya tiene receta
        ])
        citas_validas_para_receta.append(cita.id) # Agregamos el ID de la cita a una lista de validación

    print(tabla_citas)

    # --- PASO 3: Validar Cita ---
    cita_valida = False
    while not cita_valida:
        try:
            id_cita_seleccionada = int(input("\nIngrese el 'ID Cita' para la cual desea generar la receta: "))

            # Regla 1: ¿Es un ID de la lista?
            if id_cita_seleccionada not in citas_validas_para_receta:
                print("Error: Ese ID de cita no pertenece a este paciente.")
                continue # Vuelve a preguntar

            # Regla 2: ¿Ya tiene receta?
            receta_existente = obtener_receta_por_id_cita(id_cita_seleccionada)
            if receta_existente:
                print(f"Error: La cita {id_cita_seleccionada} ya tiene una receta asociada.")
                continue # Vuelve a preguntar

            cita_valida = True # Si pasa ambas, es válida

        except ValueError:
            print("Error: Debe ingresar un número de ID válido.")

    # --- PASO 4: Pedir datos de la receta ---
    print("\nIngrese los detalles de la receta:")
    medicamentos = input("Medicamentos (separados por coma): ")
    instrucciones = input("Instrucciones (ej: 1 cada 8 horas): ")

    fecha_hoy = date.today() # Obtenemos la fecha actual

    # --- PASO 5: Guardar Receta ---
    nueva_receta = Receta(
        id_cita=id_cita_seleccionada,
        medicamentos=medicamentos,
        instrucciones=instrucciones,
        fecha_emision=fecha_hoy
    )

    insertar_objeto(nueva_receta)
    print(f"\n¡Receta generada y asociada a la cita {id_cita_seleccionada} exitosamente!")

#resumen: Este código define la función de negocio para generar una nueva receta médica, validando el paciente, la cita y asegurando que no exista una receta previa antes de guardar la nueva receta en la base de datos.