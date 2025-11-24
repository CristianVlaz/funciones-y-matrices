from datos.conexion import sesion
from auxiliares.normalizar_cadena import normalizar_cadena
from modelos.paciente import Paciente
from modelos.especialidad import Especialidad
from modelos.doctor import Doctor
from modelos.cita import Cita
from modelos.receta import Receta
from modelos.especialidad import Especialidad


def obtener_datos_objetos(objeto):
    listado_objetos = sesion.query(objeto).filter_by(habilitado=True).all()
    if len(listado_objetos) > 0:
        return listado_objetos

def obtener_paciente_por_rut(rut_paciente):
    listado_pacientes = obtener_datos_objetos(Paciente)
    paciente_encontrado = None
    if listado_pacientes:
        for paciente in listado_pacientes:
            if normalizar_cadena(paciente.rut_paciente) == normalizar_cadena(rut_paciente):
                paciente_encontrado = paciente
                break
    return paciente_encontrado

def obtener_especialidad_por_nombre(nombre):
    """
    Función específica para buscar una especialidad por su nombre.
    """
    listado = obtener_datos_objetos(Especialidad)
    encontrada = None
    if listado:
        for esp in listado:
            
            if normalizar_cadena(esp.nombre_especialidad) == normalizar_cadena(nombre):
                encontrada = esp
                break
    return encontrada

def obtener_doctor_por_rut(rut_doctor):
    """
    Función específica para buscar un doctor por su RUT.
    """
    listado = obtener_datos_objetos(Doctor)
    encontrado = None
    if listado:
        for doc in listado:
            if normalizar_cadena(doc.rut_doctor) == normalizar_cadena(rut_doctor):
                encontrado = doc
                break
    return encontrado

def obtener_citas_por_doctor_y_fecha(id_doctor, fecha):
    """
    Función específica para buscar citas de un doctor en una fecha específica.
    """
    
    listado = sesion.query(Cita).filter_by(
        id_doctor=id_doctor, 
        fecha_cita=fecha,
        habilitado=True
    ).all()

    if len(listado) > 0:
        return listado
    return None 

def obtener_citas_por_paciente(id_paciente):
    """
    Función específica para buscar todas las citas de un paciente.
    """
    listado = sesion.query(Cita).filter_by(
        id_paciente=id_paciente,
        habilitado=True
    ).order_by(Cita.fecha_cita.desc()) #de la más nueva a la más antigua

    if listado.count() > 0:
        return listado.all()
    return None 

def obtener_receta_por_id_cita(id_cita_buscada):
    """
    Función específica para buscar una receta asociada a un ID de cita.
    """

    receta_encontrada = sesion.query(Receta).filter_by(
        id_cita=id_cita_buscada,
        habilitado=True
    ).first() 

    return receta_encontrada 

def obtener_especialidad_por_nombre_completo(nombre_buscado):
    """
    Busca una especialidad por nombre (normalizado), 
    sin importar si está habilitada o no.
    """
  
    listado_total = sesion.query(Especialidad).all() 
    if not listado_total:
        return None

    nombre_norm = normalizar_cadena(nombre_buscado)
    for esp in listado_total:
        if normalizar_cadena(esp.nombre_especialidad) == nombre_norm:
            return esp 
    return None

def obtener_doctor_por_rut_completo(rut_buscado):

    
    listado_total = sesion.query(Doctor).all() 
    if not listado_total:
        return None

    rut_norm = normalizar_cadena(rut_buscado)
    for doc in listado_total:
        if normalizar_cadena(doc.rut_doctor) == rut_norm:
            return doc 
    return None

def obtener_cita_por_id(id_cita_buscada):
    
    # Primero, intentamos obtener la cita (debe estar en la sesión)
    cita_encontrada = sesion.get(Cita, id_cita_buscada)
    
   
    # Si la encuentra y está habilitada, la devuelve.
    if cita_encontrada and cita_encontrada.habilitado:
        return cita_encontrada
        
    # Si no la encuentra, o la encuentra pero está deshabilitada,
    # devolvemos None (o la cita, si quisiéramos "reactivarla",
    # pero para cancelar, solo nos interesan las activas).
    elif not cita_encontrada or not cita_encontrada.habilitado:
        return None
    
#resumen: Funciones para obtener datos específicos de la base de datos