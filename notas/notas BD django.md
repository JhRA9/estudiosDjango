# Como uso las bases de datos en Django

## 1. Como configuro la base de datos

En Django, configuro la base de datos en el archivo `settings.py` usando la seccion `DATABASES`. Puedo usar motores como SQLite, PostgreSQL, MySQL, etc.

Ejemplo para PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django',
        'USER': 'admin',
        'PASSWORD': 'mi_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 2. Como defino los modelos

Los modelos en Django son clases que yo escribo y representan tablas en la base de datos. Cada atributo de la clase es una columna de la tabla.

Ejemplo:

```python
class Carro(models.Model):
    titulo = models.CharField(max_length=100)
```

## 3. Como uso las migraciones

Las migraciones son archivos que Django usa para crear y modificar las tablas segun los modelos que defino.

- Para crear migraciones:

```zsh
python manage.py makemigrations
```

- Para aplicar migraciones:

```zsh
python manage.py migrate
```

## 4. Como uso el ORM

Django tiene un ORM que me permite interactuar con la base de datos usando Python en vez de SQL. Puedo crear, leer, actualizar y borrar registros usando metodos de Python.

Ejemplo:

```python
# Crear un registro
Carro.objects.create(titulo="BMW")

# Consultar registros
Carro.objects.all()

# Filtrar registros
Carro.objects.filter(titulo="BMW")
```

## 5. Como administro los datos

Django tiene un panel de administracion donde puedo ver y modificar los datos de la base de datos de forma grafica. Para acceder, creo un superusuario:

```zsh
python manage.py createsuperuser
```

## 6. Como cambio el motor de base de datos

Puedo cambiar el motor de base de datos (por ejemplo, de SQLite a PostgreSQL) modificando la configuracion en `settings.py` y asegurandome de instalar el paquete necesario (como `psycopg2` para PostgreSQL).

---

Estas son las bases para trabajar con bases de datos en Django. Si quiero ejemplos mas avanzados o detalles sobre consultas, lo puedo pedir.
