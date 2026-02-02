# Práctica FastAPI – Gestión de Películas

## 1. Introducción

En esta práctica se ha desarrollado una **aplicación web completa con FastAPI** que amplía una API REST previa mediante la integración de **páginas web con Jinja2**.  
La aplicación permite gestionar una base de datos de películas mediante operaciones **CRUD** (crear, leer, actualizar y eliminar).

Además, se ha configurado para funcionar con **diferentes motores de base de datos** y **distintos entornos de despliegue**, cumpliendo todos los requisitos solicitados.


## 2. Tecnologías utilizadas

- Python 3  
- FastAPI  
- Jinja2  
- SQLModel  
- MySQL  
- PostgreSQL  
- Docker  
- Docker Compose  
- Render  
- GitHub  

## 3. API REST y páginas web con Jinja2

La aplicación parte de una **API REST** que expone endpoints para gestionar películas.  
Sobre esta API se han añadido **páginas web renderizadas con Jinja2**, permitiendo una interacción visual con la base de datos.

### Funcionalidades implementadas

- Listado de películas  
- Detalle de una película  
- Creación de nuevas películas  
- Edición de películas existentes  
- Eliminación de películas con confirmación  

## 4. MySQL en local (Docker + FastAPI en local)

Se ha configurado la aplicación para que:

- **MySQL** se ejecute en un contenedor Docker  
- **FastAPI** se ejecute en local dentro de un entorno virtual (`venv`)  

### Características

- MySQL se levanta mediante `docker-compose-mysql.yml`, exponiendo el puerto **3307**  
- FastAPI se ejecuta con `uvicorn` desde el entorno virtual  
- Conexión a la base de datos:

```text
mysql+pymysql://usuario:password@localhost:3307/peliculasdb
```

Al arrancar la aplicación:
- Se crean automáticamente las tablas
- Se insertan datos de ejemplo

La aplicación funciona correctamente en:

```text
http://127.0.0.1:8000
```


## 5. MySQL con Docker (App + BD en contenedores)

Se ha configurado un entorno con **Docker Compose** donde:

- FastAPI se ejecuta en un contenedor
- MySQL se ejecuta en otro contenedor
- Ambos servicios se comunican mediante la **red interna de Docker**

Esto permite ejecutar toda la aplicación sin depender del entorno local.


## 6. PostgreSQL en local

La aplicación se ha adaptado para funcionar con **PostgreSQL** modificando únicamente la cadena de conexión:

```text
postgresql://usuario:password@localhost:5432/peliculasdb
```

No ha sido necesario realizar cambios en el código de la aplicación.


## 7. PostgreSQL en Render

Se ha desplegado una base de datos **PostgreSQL en la nube** utilizando Render.

### Pasos realizados

1. Crear la base de datos PostgreSQL en Render  
2. Copiar la URL de conexión  
3. Configurar la variable de entorno `DB_URL`  
4. Usar dicha variable en la aplicación  

## 8. Despliegue de FastAPI en Render

La aplicación FastAPI se ha desplegado en Render como **Web Service** con runtime **Docker**.

### Proceso

- Render clona el repositorio desde GitHub
- Construye la imagen Docker
- Expone la aplicación en el puerto **8000**
- La aplicación se conecta a PostgreSQL en Render mediante variables de entorno

## 9. Inicialización y subida del repositorio a GitHub

Se ha creado y subido el repositorio con los siguientes comandos:

```bash
git init
git add .
git commit -m "Proyecto FastAPI películas"
git branch -M main
git remote add origin https://github.com/alexqv92/fastapi-peliculas.git
git push -u origin main
```


## 10. Deploy de FastAPI + PostgreSQL en Render

### Pasos del despliegue

1. Crear un **Web Service** en Render  
2. Configurar el runtime como **Docker**  
3. Añadir la variable de entorno `DB_URL`  
4. Lanzar el deploy  
5. Verificar el correcto funcionamiento  

✔ **DEPLOY COMPLETADO CON ÉXITO**
