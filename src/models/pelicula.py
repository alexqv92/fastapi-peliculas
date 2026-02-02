from datetime import date
from sqlmodel import Field, SQLModel

class Pelicula(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    titulo: str = Field(max_length=100)
    director: str = Field(max_length=100)
    genero: str = Field(max_length=50, index=True)
    anio: int
    duracion: int  # minutos
