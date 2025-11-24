from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from datos.conexion import Base 

class Doctor(Base):
    __tablename__ = 'doctores'
    id = Column(Integer, primary_key=True)
    rut_doctor = Column(String(10), nullable=False, unique=True)
    nombre_doctor = Column(String(150), nullable=False)
    id_especialidad = Column(Integer, ForeignKey('especialidades.id'), nullable=False)
    habilitado = Column(Boolean, nullable=False, default=True)

#resumen: Este código define el modelo de datos para los doctores en una aplicación de gestión hospitalaria, incluyendo atributos como RUT, nombre, especialidad y estado de habilitación.