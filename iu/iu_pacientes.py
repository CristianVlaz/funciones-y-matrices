# Importamos las funciones del "cerebro" (capa de negocio)
from negocio.negocio_pacientes import (
    listado_pacientes, 
    insertar_paciente, 
    modificar_paciente, 
    eliminar_paciente
)

def submenu_pacientes():
    while True:
        print("\n--- Gestión de Pacientes ---")
        print("[1] Listar todos los pacientes")
        print("[2] Registrar nuevo paciente")
        print("[3] Modificar datos de paciente")
        print("[4] Eliminar paciente")
        print("[0] Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listado_pacientes() 
        
        elif opcion == '2':
            insertar_paciente() 
        
        elif opcion == '3':
            modificar_paciente() 
        
        elif opcion == '4':
            eliminar_paciente() 
        
        elif opcion == '0':
            print("Volviendo al Menú Principal...")
            break #vuelve a inicio.py
        
        else:
            print("Opción no válida. Intente de nuevo.")
        
        input("\nPresione Enter para continuar...")

#resumen: Este código define un submenú para la gestión de pacientes. Permite listar, registrar, modificar y eliminar pacientes mediante un menú interactivo en la consola.