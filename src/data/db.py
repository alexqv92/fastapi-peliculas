from sqlmodel import create_engine, SQLModel, Session
from src.models.pelicula import Pelicula
from sqlalchemy.exc import OperationalError
import os
import time

db_user: str = "quevedo"
db_password: str = "1234"
db_server: str = "fastapi-db"
db_port: int = 3306
db_name: str = "peliculasdb"

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}"
engine = create_engine(os.getenv("DB_URL", DATABASE_URL), echo=True)


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    # Esperar a que MySQL esté listo
    for intento in range(10):
        try:
            SQLModel.metadata.drop_all(engine)
            SQLModel.metadata.create_all(engine)
            break
        except OperationalError:
            print("⏳ Esperando a MySQL...")
            time.sleep(2)
    else:
        raise RuntimeError("❌ No se pudo conectar a la base de datos")

    # Datos iniciales
    with Session(engine) as session:
        session.add(Pelicula(
            id=1,
            titulo="Inception",
            director="Christopher Nolan",
            genero="Ciencia ficción",
            anio=2010,
            duracion=148
        ))
        session.add(Pelicula(
            id=2,
            titulo="Interstellar",
            director="Christopher Nolan",
            genero="Ciencia ficción",
            anio=2014,
            duracion=169
        ))
        session.add(Pelicula(
            id=3,
            titulo="The Matrix",
            director="Wachowski",
            genero="Acción",
            anio=1999,
            duracion=136
        ))
        session.add(Pelicula(
            id=4,
            titulo="The Dark Knight",
            director="Christopher Nolan",
            genero="Acción",
            anio=2008,
            duracion=152
        ))
        session.add(Pelicula(
            id=5,
            titulo="The Lord of the Rings",
            director="Peter Jackson",
            genero="Fantasía",
            anio=2001,
            duracion=178
        ))
        session.commit()
