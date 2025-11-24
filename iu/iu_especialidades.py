# Importamos las funciones del "cerebro" (capa de negocio)
from negocio.negocio_especialidades import (
    listado_especialidades, 
    insertar_especialidad,
    modificar_especialidad, 
    eliminar_especialidad  
)

def submenu_especialidades():
    while True:
        print("\n--- Gestión de Especialidades ---")
        print("[1] Listar todas las especialidades")
        print("[2] Registrar nueva especialidad")
        print("[3] Modificar especialidad") 
        print("[4] Eliminar especialidad")   
        print("[0] Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listado_especialidades()

        elif opcion == '2':
            insertar_especialidad()

        elif opcion == '3':
            modificar_especialidad() 

        elif opcion == '4':
            eliminar_especialidad() 

        elif opcion == '0':
            print("Volviendo al Menú Principal...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

        input("\nPresione Enter para continuar...")

#resumen: Este código define un submenú para la gestión de especialidades médicas. Permite listar, registrar, modificar y eliminar especialidades mediante un menú interactivo en la consola.