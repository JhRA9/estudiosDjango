# Documentacion del proyecto Django

## Creacion del proyecto y la app

- Cree el proyecto Django usando el comando `django-admin startproject proyectoDjango`.
- Cree la app llamada `primeraApp` con `python manage.py startapp primeraApp`.

## Modelo

- En el archivo `models.py` de la app, defini la clase `Carro` con un campo `titulo` de tipo `TextField` y un maximo de 250 caracteres.

## Vista

- En el archivo `views.py` cree la funcion `vista`.
- Dentro de la funcion, defini una lista llamada `lista_carros` que contiene diccionarios, cada uno con el titulo de un carro.
- Cree un diccionario llamado `contexto` que incluye la lista de carros.
- Retorne el renderizado del template `primeraApp/index.html` pasando el contexto para que el template pueda acceder a la lista de carros.

## Template

- Cree el archivo `index.html` en la carpeta `templates/primeraApp/`.
- En el template use la sintaxis de Django `{% for carro in lista_carros %}` para iterar sobre la lista de carros enviada desde la vista.
- Dentro del ciclo, muestro el titulo de cada carro usando `{{ carro.titulo }}`.
- Esto permite que se muestren todos los titulos de los carros en una lista en la pagina web.

## Configuracion de URLs

- Importe la vista en el archivo `urls.py` del proyecto.
- Configure la ruta para que apunte a la vista creada.

## ORM

- Permite crear clases y realizarlas con la tabla de la base de datos

## migrate

- manage.py migrate para crear las tablas por defecto

## makemigrations
- manage.py migrations para crear las tablas personalizadas de mi proyecto

Exporta facturas de zac psm italiano a zigo

# django, html y css

# Exporta facturas y pagos
Reaven manager system para analizar la competencia

API 5