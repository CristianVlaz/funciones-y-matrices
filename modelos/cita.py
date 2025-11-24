from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Time
from datos.conexion import Base 

class Cita(Base):
    __tablename__ = 'citas'
    id = Column(Integer, primary_key=True)
    fecha_cita = Column(Date, nullable=False)
    hora_cita = Column(Time, nullable=False)
    motivo_cita = Column(String(255), nullable=False)
    id_paciente = Column(Integer, ForeignKey('pacientes.id'), nullable=False)
    id_doctor = Column(Integer, ForeignKey('doctores.id'), nullable=False)
    habilitado = Column(Boolean, nullable=False, default=True)

#resumen: Este código define el modelo de datos para las citas médicas en una aplicación de gestión hospitalaria, incluyendo atributos como fecha, hora, motivo, y referencias a pacientes y doctores.