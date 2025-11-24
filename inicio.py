from iu.menu_principal import menu_principal
from iu.iu_pacientes import submenu_pacientes 
from iu.iu_especialidades import submenu_especialidades
from iu.iu_doctores import submenu_doctores
from negocio.negocio_citas import agendar_nueva_cita, cancelar_cita_medica, modificar_cita_medica
from negocio.negocio_ver_historial import imprimir_historial_del_paciente 
from negocio.negocio_recetas import generar_nueva_receta 

def iniciar_aplicacion():
    while True:
        opcion = menu_principal()

        if opcion == '1':
            submenu_pacientes() 

        elif opcion == '2':
            submenu_doctores()

        elif opcion == '3':
            submenu_especialidades()

        elif opcion == '4':
            agendar_nueva_cita()

        elif opcion == '5':
            imprimir_historial_del_paciente() 

        elif opcion == '6':
            generar_nueva_receta()

        elif opcion == '7':
            cancelar_cita_medica()

        elif opcion == '8':
            modificar_cita_medica()

        elif opcion == '0':
            print("\nSaliendo del sistema... ¡Adiós!")
            break 

        else:
            print("\nOpción no válida. Intente de nuevo.")


if __name__ == "__main__":
    iniciar_aplicacion()

#resumen: Este código define la función principal para iniciar la aplicación, mostrando un menú interactivo que permite acceder a diferentes funcionalidades como gestionar pacientes, doctores, especialidades, citas médicas y recetas.