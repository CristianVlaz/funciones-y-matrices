from prettytable import PrettyTable
from datos.obtener_datos import obtener_datos_objetos, obtener_paciente_por_rut
from datos.insertar_datos import insertar_objeto, modificar_objeto
from modelos.paciente import Paciente


def listado_pacientes():
    print("\n--- Listado de Pacientes ---")
    tabla_pacientes = PrettyTable()
    tabla_pacientes.field_names = ['ID', 'RUT', 'Nombre', 'Teléfono', 'Nacimiento']
    listado = obtener_datos_objetos(Paciente)
    if listado:
        for p in listado:
            tabla_pacientes.add_row(
                [p.id, p.rut_paciente, p.nombre_paciente, p.telefono, p.fecha_nacimiento])
        print(tabla_pacientes)
    else:
        print("No hay pacientes registrados.")

def insertar_paciente():
    print("\n--- Registrar Nuevo Paciente ---")
    rut = input("Ingrese RUT (con guion, ej: 12345678-9): ")
    paciente_existente = obtener_paciente_por_rut(rut)
    if paciente_existente:
        print(f"\nError: El RUT {rut} ya está registrado.")
        return
    nombre = input("Ingrese Nombre Completo: ")
    telefono = input("Ingrese Teléfono (ej: +569...): ")
    nacimiento = input("Ingrese Fecha de Nacimiento (YYYY-MM-DD): ")
    historia = input("Ingrese Historia Clínica (Antecedentes): ")
    nuevo_paciente = Paciente(
        rut_paciente=rut,
        nombre_paciente=nombre.title(),
        telefono=telefono,
        fecha_nacimiento=nacimiento,
        historia_clinica=historia
    )
    insertar_objeto(nuevo_paciente)
    print("Paciente registrado exitosamente.") 

def modificar_paciente():
    print("\n--- Modificar Paciente ---")
    rut = input("Ingrese el RUT del paciente que desea modificar: ")
    paciente = obtener_paciente_por_rut(rut)
    if not paciente:
        print(f"\nError: No se encontró un paciente con el RUT {rut}.")
        return
    print(f"Datos actuales: Nombre({paciente.nombre_paciente}), Teléfono({paciente.telefono})")
    nuevo_nombre = input("Ingrese nuevo nombre (o Enter para no cambiar): ")
    nuevo_telefono = input("Ingrese nuevo teléfono (o Enter para no cambiar): ")
    if nuevo_nombre:
        paciente.nombre_paciente = nuevo_nombre.title()
    if nuevo_telefono:
        paciente.telefono = nuevo_telefono
    modificar_objeto()
    print("Paciente actualizado exitosamente.") 

def eliminar_paciente():
    print("\n--- Eliminar Paciente ---")
    rut = input("Ingrese el RUT del paciente que desea eliminar: ")

    paciente = obtener_paciente_por_rut(rut)

    if not paciente:
        print(f"\nError: No se encontró un paciente con el RUT {rut}.")
        return


    # Eliminado Lógico
    paciente.habilitado = False

    modificar_objeto()

    
    print(f"Paciente '{paciente.nombre_paciente}' ha sido eliminado (deshabilitado).")

def obtener_pacientes_para_gui():
    """
    Esta función no imprime nada, solo devuelve la lista 
    de objetos 'Paciente' para que la GUI los use.
    """
    lista_pacientes = obtener_datos_objetos(Paciente)
    return lista_pacientes

#resumen: Este código define las funciones de negocio para gestionar pacientes, incluyendo listar, insertar, modificar y eliminar pacientes, con validaciones para evitar duplicados y manejar estados de habilitación.