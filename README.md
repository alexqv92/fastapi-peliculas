# Práctica FastAPI – Gestión de Películas

## 1. Introducción

En esta práctica se ha desarrollado una aplicación web completa basada en **FastAPI** que amplía una API REST previa mediante la integración de **páginas web con Jinja2**. La aplicación permite gestionar una base de datos de películas mediante operaciones CRUD (crear, leer, actualizar y eliminar).
Además, la aplicación se ha configurado para funcionar con distintos motores de bases de datos y entornos de despliegue, cumpliendo todos los requisitos solicitados.

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

La aplicación parte de una **API REST** que expone endpoints para gestionar películas. Sobre esta API se han añadido **páginas web renderizadas con Jinja2**, permitiendo una interacción visual con la base de datos.

### Funcionalidades implementadas

- Listado de películas
- Detalle de una película
- Creación de nuevas películas
- Edición de películas existentes
- Eliminación de películas con confirmación


## 4. MySQL en localhost

La aplicación puede ejecutarse utilizando una base de datos **MySQL instalada en local**. La conexión se realiza mediante una cadena como la siguiente:

mysql+pymysql://usuario:password@localhost:3306/peliculasdb


## 5. MySQL con Docker

Se ha configurado un entorno con **Docker Compose** donde:
- FastAPI se ejecuta en un contenedor
- MySQL se ejecuta en otro contenedor

Ambos se comunican mediante la red interna de Docker.


## 6. PostgreSQL

La aplicación se ha adaptado para funcionar con **PostgreSQL** cambiando únicamente la cadena de conexión.

postgresql://usuario:password@localhost:5432/peliculasdb


## 7. PostgreSQL en Render

Se ha desplegado una base de datos PostgreSQL en la nube usando **Render**.

Pasos:
1. Crear la base de datos en Render
2. Copiar la URL de conexión
3. Configurar la variable de entorno DB_URL
4. Desplegar la aplicación FastAPI


## 8. Despliegue de FastAPI en Render

La aplicación se despliega como **Web Service** con runtime Docker.
Render construye la imagen y expone la app en el puerto 8000.


## 9. Inicialización del repositorio Git

git init  
git add .  
git commit -m "Proyecto FastAPI películas"  
git branch -M main  
git remote add origin https://github.com/alexqv92/fastapi-peliculas.git  
git push -u origin main  


# 🚀 Deploy de FastAPI + PostgreSQL en Render

## Paso 1 — Crear Web Service en Render
## Paso 2 — Configuración del servicio
## Paso 3 — Variables de entorno
## Paso 4 — Deploy
## Paso 5 — Verificación

✔ DEPLOY APROBADO
