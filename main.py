from fastapi import FastAPI, HTTPException, Depends, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER

from contextlib import asynccontextmanager
import threading
from sqlmodel import Session, select

from src.data.db import init_db, get_session
from src.models.pelicula import Pelicula

import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    threading.Thread(target=init_db, daemon=True).start()
    yield

app = FastAPI(lifespan=lifespan)


app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")


# PÁGINAS WEB
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    mensaje = "Bienvenido a la aplicación de películas"
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "mensaje": mensaje}
    )

@app.get("/peliculas", response_class=HTMLResponse)
async def listar_peliculas(
    request: Request,
    session: Session = Depends(get_session)
):
    peliculas = session.exec(select(Pelicula)).all()
    return templates.TemplateResponse(
        "peliculas.html",
        {"request": request, "peliculas": peliculas}
    )


# CREAR PELÍCULA
@app.get("/peliculas/crear", response_class=HTMLResponse)
async def crear_pelicula_form(request: Request):
    return templates.TemplateResponse(
        "crear_pelicula.html",
        {"request": request}
    )

@app.post("/peliculas/crear", response_class=HTMLResponse)
async def crear_pelicula(
    request: Request,
    titulo: str = Form(...),
    director: str = Form(...),
    genero: str = Form(...),
    anio: int = Form(...),
    duracion: int = Form(...),
    session: Session = Depends(get_session)
):
    nueva = Pelicula(
        titulo=titulo,
        director=director,
        genero=genero,
        anio=anio,
        duracion=duracion
    )
    session.add(nueva)
    session.commit()
    session.refresh(nueva)

    return templates.TemplateResponse(
        "pelicula_detalle.html",
        {"request": request, "pelicula": nueva}
    )


# EDITAR PELÍCULA
@app.get("/peliculas/editar/{pelicula_id}", response_class=HTMLResponse)
async def editar_pelicula_form(
    pelicula_id: int,
    request: Request,
    session: Session = Depends(get_session)
):
    pelicula = session.get(Pelicula, pelicula_id)
    if not pelicula:
        raise HTTPException(status_code=404, detail="Película no encontrada")

    return templates.TemplateResponse(
        "editar_pelicula.html",
        {"request": request, "pelicula": pelicula}
    )

@app.post("/peliculas/editar/{pelicula_id}", response_class=HTMLResponse)
async def editar_pelicula(
    pelicula_id: int,
    request: Request,            
    titulo: str = Form(...),
    director: str = Form(...),
    genero: str = Form(...),
    anio: int = Form(...),
    duracion: int = Form(...),
    session: Session = Depends(get_session)
):
    pelicula = session.get(Pelicula, pelicula_id)
    if not pelicula:
        raise HTTPException(status_code=404, detail="Película no encontrada")

    pelicula.titulo = titulo
    pelicula.director = director
    pelicula.genero = genero
    pelicula.anio = anio
    pelicula.duracion = duracion

    session.commit()
    session.refresh(pelicula)

    return templates.TemplateResponse(
        "pelicula_detalle.html",
        {"request": request, "pelicula": pelicula}
    )


# ELIMINAR PELÍCULA
@app.get("/peliculas/eliminar/{pelicula_id}", response_class=HTMLResponse)
async def eliminar_pelicula_form(
    pelicula_id: int,
    request: Request,
    session: Session = Depends(get_session)
):
    pelicula = session.get(Pelicula, pelicula_id)
    if not pelicula:
        raise HTTPException(status_code=404, detail="Película no encontrada")

    return templates.TemplateResponse(
        "eliminar_pelicula.html",
        {"request": request, "pelicula": pelicula}
    )


@app.post("/peliculas/eliminar/{pelicula_id}", response_class=HTMLResponse)
async def eliminar_pelicula(
    pelicula_id: int,
    request: Request,
    session: Session = Depends(get_session)
):
    pelicula = session.get(Pelicula, pelicula_id)
    if not pelicula:
        raise HTTPException(status_code=404, detail="Película no encontrada")

    session.delete(pelicula)
    session.commit()

    peliculas = session.exec(select(Pelicula)).all()

    return templates.TemplateResponse(
        "peliculas.html",
        {"request": request, "peliculas": peliculas}
    )

# DETALLE PELÍCULA 

@app.get("/peliculas/{pelicula_id}", response_class=HTMLResponse)
async def pelicula_detalle(
    pelicula_id: int,
    request: Request,
    session: Session = Depends(get_session)
):
    pelicula = session.get(Pelicula, pelicula_id)
    if not pelicula:
        raise HTTPException(status_code=404, detail="Película no encontrada")

    return templates.TemplateResponse(
        "pelicula_detalle.html",
        {"request": request, "pelicula": pelicula}
    )


# API REST
@app.get("/api/peliculas", response_model=list[Pelicula])
async def api_listar_peliculas(
    session: Session = Depends(get_session)
):
    return session.exec(select(Pelicula)).all()


@app.post("/api/peliculas", response_model=Pelicula, status_code=201)
async def api_crear_pelicula(
    pelicula: Pelicula,
    session: Session = Depends(get_session)
):
    session.add(pelicula)
    session.commit()
    session.refresh(pelicula)
    return pelicula


# EJECUCIÓN
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
