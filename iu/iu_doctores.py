from negocio.negocio_doctores import (
    listado_doctores, 
    insertar_doctor,
    modificar_doctor, 
    eliminar_doctor   
)

def submenu_doctores():
    while True:
        print("\n--- Gestión de Doctores ---")
        print("[1] Listar todos los doctores")
        print("[2] Registrar nuevo doctor")
        print("[3] Modificar doctor")
        print("[4] Eliminar doctor")  
        print("[0] Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listado_doctores()

        elif opcion == '2':
            insertar_doctor()

        elif opcion == '3':
            modificar_doctor() 

        elif opcion == '4':
            eliminar_doctor() 

        elif opcion == '0':
            print("Volviendo al Menú Principal...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

        input("\nPresione Enter para continuar...")

#resumen: Este código define un submenú para la gestión de doctores. Permite listar, registrar, modificar y eliminar doctores mediante un menú interactivo en la consola.