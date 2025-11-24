from prettytable import PrettyTable
from datos.obtener_datos import (
    obtener_datos_objetos, 
    obtener_especialidad_por_nombre, 
    obtener_especialidad_por_nombre_completo
)
from datos.insertar_datos import insertar_objeto, modificar_objeto 
from modelos.especialidad import Especialidad
from auxiliares.normalizar_cadena import normalizar_cadena


def listado_especialidades():
    print("\n--- Listado de Especialidades ---")
    tabla = PrettyTable()
    tabla.field_names = ['ID', 'Nombre', 'Descripción']
    listado = obtener_datos_objetos(Especialidad)
    if listado:
        for esp in listado:
            tabla.add_row([esp.id, esp.nombre_especialidad, esp.descripcion])
        print(tabla)
    else:
        print("No hay especialidades registradas.")


def _crear_especialidad(nombre, descripcion=""):
    """
    Función interna. Crea o reactiva una especialidad.
    ¡Devuelve el OBJETO COMPLETO "VIVO"!
    """
    existente = obtener_especialidad_por_nombre_completo(nombre)

    if existente and existente.habilitado == True:
        return existente 

    if existente and existente.habilitado == False:
        print(f"\n(Info: Reactivando la especialidad '{existente.nombre_especialidad}'...)")
        existente.habilitado = True
        existente.descripcion = descripcion if descripcion else existente.descripcion
        modificar_objeto()
        return existente 

    else:
        print(f"\n(Info: Creando nueva especialidad '{nombre.title()}'...)")
        nueva_especialidad = Especialidad(
            nombre_especialidad=nombre.title(),
            descripcion=descripcion
        )
        insertar_objeto(nueva_especialidad)
        return nueva_especialidad 


def insertar_especialidad():
    print("\n--- Registrar Nueva Especialidad ---")
    nombre = input("Ingrese Nombre de la especialidad: ")

    existente_activa = obtener_especialidad_por_nombre(nombre) 
    if existente_activa:
        print(f"\nError: La especialidad '{nombre}' ya existe y está activa.")
        return

    descripcion = input("Ingrese una descripción (opcional): ")
    _crear_especialidad(nombre, descripcion)

def modificar_especialidad():
    print("\n--- Modificar Especialidad ---")
    nombre_actual = input("Ingrese el Nombre de la especialidad que desea modificar: ")
    especialidad = obtener_especialidad_por_nombre(nombre_actual)
    if not especialidad:
        print(f"\nError: No se encontró la especialidad '{nombre_actual}'.")
        return
    print(f"Datos actuales: Nombre({especialidad.nombre_especialidad}), Descripcion({especialidad.descripcion})")
    nuevo_nombre = input("Ingrese el nuevo nombre (o Enter para no cambiar): ")
    nueva_desc = input("Ingrese la nueva descripción (o Enter para no cambiar): ")
    if nuevo_nombre:
        especialidad.nombre_especialidad = nuevo_nombre.title()
    if nueva_desc:
        especialidad.descripcion = nueva_desc
    modificar_objeto()
    print("Especialidad actualizada exitosamente.")

def eliminar_especialidad():
    print("\n--- Eliminar Especialidad ---")
    nombre = input("Ingrese el Nombre de la especialidad que desea eliminar: ")
    especialidad = obtener_especialidad_por_nombre(nombre)
    if not especialidad:
        print(f"\nError: No se encontró la especialidad '{nombre}'.")
        return

    especialidad.habilitado = False
    modificar_objeto() 

    print(f"Especialidad '{especialidad.nombre_especialidad}' ha sido eliminada (deshabilitada).")

#resumen: Este código define las funciones de negocio para gestionar especialidades médicas, incluyendo listar, insertar, modificar y eliminar especialidades, con validaciones para evitar duplicados y manejar estados de habilitación.