from auxiliares.info_aplicacion import nombre_aplicacion
from auxiliares.version import numero_version

def menu_principal():
    print(f'\n{nombre_aplicacion} v.{numero_version}')
    print('=======================================')
    print()
    print('[1] Gestión de Pacientes')
    print('[2] Gestión de Doctores')
    print('[3] Gestión de Especialidades')
    print('[4] Agendar Cita Médica')
    print('[5] Ver historial de Citas por Paciente')
    print('[6] Generar Receta Médica')
    print('[7] Cancelar Cita Médica')
    print('[8] Modificar Cita Médica') 
    print('[0] Salir')

    opcion = input('Seleccione una opción: ')
    return opcion

#resumen: Este código define el menú principal de una aplicación de gestión hospitalaria, mostrando opciones para gestionar pacientes, doctores, especialidades, citas médicas y recetas.