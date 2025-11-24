from sqlalchemy import Column, Integer, String, Boolean, Text
from datos.conexion import Base 

class Especialidad(Base):
    __tablename__ = 'especialidades'
    id = Column(Integer, primary_key=True)
    nombre_especialidad = Column(String(100), nullable=False, unique=True)
    descripcion = Column(Text, nullable=True)
    habilitado = Column(Boolean, nullable=False, default=True)

#resumen: Este código define el modelo de datos para las especialidades médicas en una aplicación de gestión hospitalaria, incluyendo atributos como nombre, descripción y estado de habilitación.