from prettytable import PrettyTable
from datos.obtener_datos import (
    obtener_datos_objetos, 
    obtener_doctor_por_rut, 
    obtener_especialidad_por_nombre,
    obtener_doctor_por_rut_completo 
)
from datos.insertar_datos import insertar_objeto, modificar_objeto
from modelos.doctor import Doctor
from modelos.especialidad import Especialidad
from negocio.negocio_especialidades import listado_especialidades, _crear_especialidad

def listado_doctores():
    # (Esta función no se toca, sigue igual)
    print("\n--- Listado de Doctores ---")
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'RUT', 'Nombre', 'Especialidad']
    listado_doctores = obtener_datos_objetos(Doctor)
    listado_especialidades = obtener_datos_objetos(Especialidad)
    if listado_doctores:
        dict_especialidades = {}
        if listado_especialidades:
             dict_especialidades = {esp.id: esp.nombre_especialidad for esp in listado_especialidades}
        for doc in listado_doctores:
            nombre_esp = dict_especialidades.get(doc.id_especialidad, "Especialidad Borrada")
            tabla.add_row([doc.id, doc.rut_doctor, doc.nombre_doctor, nombre_esp])
        print(tabla)
    else:
        print("No hay doctores registrados.")

def insertar_doctor():
    print("\n--- Registrar Nuevo Doctor ---")
    rut = input("Ingrese RUT del doctor (con guion, ej: 12345678-9): ")
    existente = obtener_doctor_por_rut_completo(rut) 
    if existente and existente.habilitado == True:
        print(f"\nError: El RUT {rut} ya está registrado y activo.")
        return
    nombre = input("Ingrese Nombre Completo del doctor: ")
    print("A continuación, asigne una especialidad:")
    listado_especialidades() 

    especialidad_encontrada = None
    while not especialidad_encontrada:
        nombre_esp = input("Ingrese el Nombre de la especialidad (o 'nueva' para crear una): ")

        if nombre_esp.lower() == 'nueva':
            nuevo_nombre_esp = input("Ingrese el nombre de la NUEVA especialidad: ")
            # _crear_especialidad ahora devuelve un objeto "vivo"
            especialidad_encontrada = _crear_especialidad(nuevo_nombre_esp)
            # ¡Esta línea ahora es SEGURA!
            print(f"Especialidad '{especialidad_encontrada.nombre_especialidad}' creada/reactivada.")
        else:
            especialidad_encontrada = obtener_especialidad_por_nombre(nombre_esp)
            if not especialidad_encontrada:
                print(f"\nError: No se encontró la especialidad '{nombre_esp}'.")
                crear = input(f"¿Desea crear la especialidad '{nombre_esp}' ahora? (s/n): ").lower()
                if crear == 's':
                    # _crear_especialidad ahora devuelve un objeto "vivo"
                    especialidad_encontrada = _crear_especialidad(nombre_esp)
                    # ¡Esta línea ahora es SEGURA!
                    print(f"Especialidad '{especialidad_encontrada.nombre_especialidad}' creada/reactivada.")
                else:
                    print("Intente de nuevo...") 

    # ¡Esta línea también es SEGURA!
    print(f"Doctor será asignado a: {especialidad_encontrada.nombre_especialidad}") 

    if existente and existente.habilitado == False:
        print(f"\nEl doctor con RUT {rut} ya existía pero estaba eliminado.")
        print("Re-habilitando al doctor...")
        existente.habilitado = True
        existente.nombre_doctor = nombre.title()
        existente.id_especialidad = especialidad_encontrada.id
        modificar_objeto()
    else:
        nuevo_doctor = Doctor(
            rut_doctor=rut,
            nombre_doctor=nombre.title(),
            id_especialidad=especialidad_encontrada.id 
        )
        insertar_objeto(nuevo_doctor)

def modificar_doctor():
    print("\n--- Modificar Doctor ---")
    rut = input("Ingrese el RUT del doctor que desea modificar: ")
    doctor = obtener_doctor_por_rut(rut)
    if not doctor:
        print(f"\nError: No se encontró un doctor activo con el RUT {rut}.")
        return
    listado_especialidades_all = obtener_datos_objetos(Especialidad)
    dict_especialidades = {}
    if listado_especialidades_all:
        dict_especialidades = {esp.id: esp.nombre_especialidad for esp in listado_especialidades_all}
    nombre_esp_actual = dict_especialidades.get(doctor.id_especialidad, "N/A")
    print(f"Datos actuales: Nombre({doctor.nombre_doctor}), Especialidad({nombre_esp_actual})")
    nuevo_nombre = input("Ingrese el nuevo nombre (o Enter para no cambiar): ")
    if nuevo_nombre:
        doctor.nombre_doctor = nuevo_nombre.title()
    cambiar_esp = input("¿Desea cambiar la especialidad? (s/n): ").lower()
    if cambiar_esp == 's':
        listado_especialidades()
        especialidad_encontrada = None
        while not especialidad_encontrada:
            nombre_esp = input("Ingrese el Nombre de la nueva especialidad (o 'nueva' para crear): ")
            if nombre_esp.lower() == 'nueva':
                nuevo_nombre_esp = input("Ingrese el nombre de la NUEVA especialidad: ")
                especialidad_encontrada = _crear_especialidad(nuevo_nombre_esp)
                print(f"Especialidad '{especialidad_encontrada.nombre_especialidad}' creada/reactivada.")
            else:
                especialidad_encontrada = obtener_especialidad_por_nombre(nombre_esp)
            if not especialidad_encontrada:
                print(f"\nError: No se encontró la especialidad '{nombre_esp}'.")
                crear = input(f"¿Desea crear la especialidad '{nombre_esp}' ahora? (s/n): ").lower()
                if crear == 's':
                    especialidad_encontrada = _crear_especialidad(nombre_esp)
                    print(f"Especialidad '{especialidad_encontrada.nombre_especialidad}' creada/reactivada.")
                else:
                    print("Intente de nuevo...") 
        doctor.id_especialidad = especialidad_encontrada.id
        print(f"Especialidad actualizada a: {especialidad_encontrada.nombre_especialidad}")
    modificar_objeto()
    print("Doctor actualizado exitosamente.")

def eliminar_doctor():
    print("\n--- Eliminar Doctor ---")
    rut = input("Ingrese el RUT del doctor que desea eliminar: ")
    doctor = obtener_doctor_por_rut(rut)
    if not doctor:
        print(f"\nError: No se encontró un doctor activo con el RUT {rut}.")
        return

    doctor.habilitado = False
    modificar_objeto()
    print(f"Doctor '{doctor.nombre_doctor}' ha sido eliminado (deshabilitado).")

#resumen: Este código define las funciones de negocio para gestionar doctores, incluyendo listar, insertar, modificar y eliminar doctores, con validaciones para especialidades y estados de habilitación.