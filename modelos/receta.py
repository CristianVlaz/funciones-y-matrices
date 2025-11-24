from sqlalchemy import Column, Integer, Boolean, Text, Date, ForeignKey
from datos.conexion import Base 

class Receta(Base):
    __tablename__ = 'recetas'
    id = Column(Integer, primary_key=True)
    id_cita = Column(Integer, ForeignKey('citas.id'), nullable=False)
    medicamentos = Column(Text, nullable=True)
    instrucciones = Column(Text, nullable=True)
    fecha_emision = Column(Date, nullable=False)
    habilitado = Column(Boolean, nullable=False, default=True)

#resumen: Este código define el modelo de datos para las recetas médicas en una aplicación de gestión hospitalaria, incluyendo atributos como la cita asociada, medicamentos, instrucciones, fecha de emisión y estado de habilitación.