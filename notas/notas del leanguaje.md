# Guia rapida de Django

## 1. Que es Django y el patron MTV

Django usa el patron Modelo-Vista-Plantilla (MTV):

- **Modelo**: Aqui guardo y manejo los datos (por ejemplo, usuarios, productos, etc).
- **Vista**: Es el puente entre el modelo y la plantilla, decido que datos mostrar y como procesar las peticiones.
- **Plantilla**: Es el HTML y CSS, muestro la informacion al usuario de forma visual.

---

## 2. Como crear una vista

1. Escribo la funcion de la vista en el archivo `views.py` de mi app:

```python
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse('Hola desde la vista')
```

2. Registro la vista en `urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('ruta/', views.mi_vista),
]
```

---

## 3. Como crear un modelo

1. Escribo la clase del modelo en `models.py` de mi app:

```python
from django.db import models

class MiModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
```

2. Creo y aplico las migraciones:

```zsh
python manage.py makemigrations
python manage.py migrate
```

---

## 4. Que es el contexto y como funciona

Cuando uso la funcion `render` en una vista, puedo pasarle un "contexto". El contexto es un diccionario con datos que quiero enviar a la plantilla (HTML).

Por ejemplo:

```python
contexto = {
    'lista_carros': lista_carros
}
return render(peticion, "primeraApp.html", contexto)
```

- Creo un diccionario con los datos que quiero mostrar en la plantilla.
- Paso ese diccionario como tercer argumento a la funcion `render`.
- En la plantilla HTML, accedo a esos datos usando las llaves del diccionario. Por ejemplo, en el HTML puedo poner `{{ lista_carros }}` para mostrar la lista de carros.

Esto me permite enviar informacion dinamica desde la vista al HTML y mostrarla al usuario.

---

## 5. Ejemplo de pasar una lista de objetos a la plantilla

En la vista:

```python
def vista(peticion):
    lista_carros = [
        {"titulo": "BMW"},
        {"titulo": "Lambo"}
    ]
    contexto = {
        'lista_carros': lista_carros
    }
    return render(peticion, "primeraApp.html", contexto)
```

En la plantilla HTML:

```django
{% for carro in lista_carros %}
    <p>{{ carro.titulo }}</p>
{% endfor %}
```

---

## 6. Comandos basicos de Django

- `django-admin startproject nombre_del_proyecto`  
  Crea un nuevo proyecto de Django
- `python manage.py runserver`  
  Inicia el servidor web de desarrollo
- `python manage.py startapp nombre_de_la_app`  
  Crea una nueva aplicacion dentro del proyecto
- `python manage.py makemigrations`  
  Prepara los cambios en la base de datos
- `python manage.py migrate`  
  Aplica los cambios en la base de datos
- `python manage.py createsuperuser`  
  Crea un usuario administrador para el panel de Django
- `python manage.py shell`  
  Abre una consola interactiva con el entorno de Django
- `python manage.py collectstatic`  
  Reune los archivos estaticos para su uso en produccion

---

## 7. Notas y tips

- Los modelos representan tablas en la base de datos.
- Las vistas procesan las peticiones y deciden que datos enviar a la plantilla.
- Las plantillas muestran la informacion al usuario usando HTML y las variables que llegan en el contexto.
- El contexto es clave para enviar datos dinamicos a la plantilla.
- Usa los comandos basicos para crear y administrar tu proyecto Django.
