from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 
from auxiliares.info_aplicacion import usuario_db, contrasena_db, servidor_db, puerto_db, nombre_db

Base = declarative_base()


url_db = f"mysql+mysqlconnector://{usuario_db}:{contrasena_db}@{servidor_db}:{puerto_db}/{nombre_db}"
motor_db = create_engine(url_db)
Session = sessionmaker(bind=motor_db)
sesion = Session()

#resumen: Configuración de la conexión a la base de datos utilizando SQLAlchemy