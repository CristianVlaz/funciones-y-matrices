from sqlalchemy import Column, Integer, String, Boolean, Text, Date
from datos.conexion import Base 

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True)
    rut_paciente = Column(String(10), nullable=False, unique=True)
    nombre_paciente = Column(String(150), nullable=False)
    fecha_nacimiento = Column(Date, nullable=True)
    telefono = Column(String(12), nullable=True)
    historia_clinica = Column(Text, nullable=True)
    habilitado = Column(Boolean, nullable=False, default=True)

#resumen: Este código define el modelo de datos para los pacientes en una aplicación de gestión hospitalaria, incluyendo atributos como RUT, nombre, fecha de nacimiento, teléfono, historia clínica y estado de habilitación.