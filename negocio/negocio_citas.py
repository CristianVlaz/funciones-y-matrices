from datetime import datetime
from prettytable import PrettyTable

#funciones de 'datos'
from datos.obtener_datos import (
    obtener_paciente_por_rut, 
    obtener_doctor_por_rut, 
    obtener_citas_por_doctor_y_fecha,
    obtener_cita_por_id 
)
from datos.insertar_datos import insertar_objeto, modificar_objeto


from modelos.cita import Cita

#funciones
from negocio.negocio_pacientes import listado_pacientes
from negocio.negocio_doctores import listado_doctores
from negocio.negocio_ver_historial import imprimir_historial_del_paciente 


def agendar_nueva_cita():
    
    print("\n--- Agendar Nueva Cita Médica ---")
    paciente = None
    while not paciente:
        listado_pacientes() 
        rut_paciente = input("Ingrese RUT del Paciente: ")
        paciente = obtener_paciente_por_rut(rut_paciente)
        if not paciente:
            print(f"Error: Paciente con RUT {rut_paciente} no encontrado. Intente de nuevo.")
    doctor = None
    while not doctor:
        listado_doctores() 
        rut_doctor = input("Ingrese RUT del Doctor: ")
        doctor = obtener_doctor_por_rut(rut_doctor)
        if not doctor:
            print(f"Error: Doctor con RUT {rut_doctor} no encontrado. Intente de nuevo.")
    print(f"\nAgendando cita para Paciente: {paciente.nombre_paciente}")
    print(f"Con el Doctor: {doctor.nombre_doctor}")
    fecha_valida = False
    hora_valida = False
    while not fecha_valida or not hora_valida:
        fecha_cita = input("Ingrese Fecha de la cita (YYYY-MM-DD): ")
        hora_cita_str = input("Ingrese Hora de la cita (HH:MM, formato 24hrs): ")
        citas_existentes = obtener_citas_por_doctor_y_fecha(doctor.id, fecha_cita)
        hora_valida = True 
        if citas_existentes:
            print("El doctor ya tiene citas agendadas ese día:")
            horas_ocupadas = []
            for cita in citas_existentes:
                horas_ocupadas.append(cita.hora_cita.strftime('%H:%M'))
            print(f"Horas ocupadas: {', '.join(horas_ocupadas)}")
            if hora_cita_str in horas_ocupadas:
                print(f"Error: La hora {hora_cita_str} ya está ocupada. Elija otra.")
                hora_valida = False
        if hora_valida:
            fecha_valida = True 
    motivo = input("Ingrese el Motivo de la cita: ")
    nueva_cita = Cita(
        fecha_cita=fecha_cita,
        hora_cita=hora_cita_str,
        motivo_cita=motivo,
        id_paciente=paciente.id,
        id_doctor=doctor.id
    )
    insertar_objeto(nueva_cita)
    print("\n¡Cita agendada exitosamente!")


def cancelar_cita_medica():
    print("\n--- Cancelar Cita Médica ---")
    print("Primero, busque al paciente para ver sus citas activas:")
    imprimir_historial_del_paciente() 
    try:
        id_cita_a_cancelar = int(input("\nIngrese el 'ID Cita' que desea cancelar (0 para salir): "))
        if id_cita_a_cancelar == 0:
            print("Cancelando operación...")
            return
        cita_encontrada = obtener_cita_por_id(id_cita_a_cancelar)
        if not cita_encontrada:
            print(f"\nError: No se encontró ninguna cita activa con el ID {id_cita_a_cancelar}.")
            return
        cita_encontrada.habilitado = False
        modificar_objeto()
        print(f"\n¡Cita ID {id_cita_a_cancelar} ha sido cancelada exitosamente!")
    except ValueError:
        print("\nError: Debe ingresar un número de ID válido.")


def modificar_cita_medica():
    print("\n--- Modificar Cita Médica ---")
    print("Primero, busque al paciente para ver sus citas activas:")
    imprimir_historial_del_paciente() 
    try:
        id_cita_a_modificar = int(input("\nIngrese el 'ID Cita' que desea modificar (0 para salir): "))
        if id_cita_a_modificar == 0:
            print("Cancelando operación...")
            return
        cita = obtener_cita_por_id(id_cita_a_modificar)
        if not cita:
            print(f"\nError: No se encontró ninguna cita activa con el ID {id_cita_a_modificar}.")
            return
        print(f"Modificando cita: Fecha({cita.fecha_cita}), Hora({cita.hora_cita.strftime('%H:%M')}), Motivo({cita.motivo_cita})")
        print("Ingrese los nuevos datos (o presione Enter para no cambiar):")
        nueva_fecha_str = input(f"Nueva Fecha ({cita.fecha_cita}): ")
        nueva_hora_str = input(f"Nueva Hora ({cita.hora_cita.strftime('%H:%M')}): ")
        nuevo_motivo = input(f"Nuevo Motivo ({cita.motivo_cita}): ")
        if not nueva_fecha_str:
            nueva_fecha_str = str(cita.fecha_cita)
        if not nueva_hora_str:
            nueva_hora_str = cita.hora_cita.strftime('%H:%M')
        if not nuevo_motivo:
            nuevo_motivo = cita.motivo_cita
        if nueva_fecha_str != str(cita.fecha_cita) or nueva_hora_str != cita.hora_cita.strftime('%H:%M'):
            print("Validando nueva fecha y hora...")
            citas_existentes = obtener_citas_por_doctor_y_fecha(cita.id_doctor, nueva_fecha_str)
            hora_valida = True
            if citas_existentes:
                horas_ocupadas = []
                for c_existente in citas_existentes:
                    if c_existente.id != cita.id:
                        horas_ocupadas.append(c_existente.hora_cita.strftime('%H:%M'))
                if nueva_hora_str in horas_ocupadas:
                    print(f"Error: El doctor ya tiene una cita a las {nueva_hora_str} en esa fecha.")
                    print("Operación cancelada. Intente de nuevo.")
                    hora_valida = False
            if not hora_valida:
                return
        cita.fecha_cita = nueva_fecha_str
        cita.hora_cita = nueva_hora_str
        cita.motivo_cita = nuevo_motivo
        modificar_objeto()
        print(f"\n¡Cita ID {id_cita_a_modificar} ha sido modificada exitosamente!")
    except ValueError:
        print("\nError: Debe ingresar un número de ID válido.")

#resumen: Este código define las funciones de negocio para gestionar citas médicas, incluyendo agendar, cancelar y modificar citas, con validaciones para evitar conflictos de horarios.