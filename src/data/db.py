from sqlmodel import create_engine, SQLModel, Session, select
from src.models.pelicula import Pelicula
from sqlalchemy.exc import OperationalError
import os
import time

# Configuración por defecto (MySQL Docker / local)
db_user: str = "quevedo"
db_password: str = "1234"
db_server: str = "fastapi-db" # Cambiar por "localhost" si se usa Docker
db_port: int = 3306# Cambiar por 3306 si se usa localmente
db_name: str = "peliculasdb"

DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_server}:{db_port}/{db_name}"

engine = create_engine(
    os.getenv("DB_URL", DATABASE_URL),
    echo=True
)


def get_session():
    with Session(engine) as session:
        yield session


def init_db():
    # Esperar a que la base de datos esté lista
    for intento in range(10):
        try:
            SQLModel.metadata.create_all(engine)
            break
        except OperationalError:
            print("⏳ Esperando a la base de datos...")
            time.sleep(2)
    else:
        raise RuntimeError("❌ No se pudo conectar a la base de datos")

    # Insertar datos iniciales SOLO si la tabla está vacía
    with Session(engine) as session:
        existe = session.exec(select(Pelicula)).first()
        if existe:
            return

        peliculas_iniciales = [
            Pelicula(
                titulo="Inception",
                director="Christopher Nolan",
                genero="Ciencia ficción",
                anio=2010,
                duracion=148
            ),
            Pelicula(
                titulo="Interstellar",
                director="Christopher Nolan",
                genero="Ciencia ficción",
                anio=2014,
                duracion=169
            ),
            Pelicula(
                titulo="The Matrix",
                director="Wachowski",
                genero="Acción",
                anio=1999,
                duracion=136
            ),
            Pelicula(
                titulo="The Dark Knight",
                director="Christopher Nolan",
                genero="Acción",
                anio=2008,
                duracion=152
            ),
            Pelicula(
                titulo="The Lord of the Rings",
                director="Peter Jackson",
                genero="Fantasía",
                anio=2001,
                duracion=178
            ),
        ]

        session.add_all(peliculas_iniciales)
        session.commit()

