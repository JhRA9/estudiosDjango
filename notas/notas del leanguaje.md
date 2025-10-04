# Django es un MTV

Django usa el patron Modelo-Vista-Plantilla (MTV):

- **Modelo**: Es la parte de la logica, aqui guardo y manejo los datos (por ejemplo, usuarios, productos, etc).
- **Vista**: Es el puente entre el modelo y la plantilla, aqui decido que datos mostrar y como procesar las peticiones.
- **Plantilla**: Es el HTML y CSS, aqui muestro la informacion al usuario de forma visual.

# Como creo una vista en Django

1. Escribo la funcion de la vista en el archivo views.py de mi app:

```python
from django.http import HttpResponse

def mi_vista(request):
    return HttpResponse('Hola desde la vista')
```
# Esta funcion recibe una peticion y devuelve una respuesta.

2. Registro la vista en urls.py:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('ruta/', views.mi_vista),
]
```
# Esto conecta la URL con la funcion de la vista.

---

# Como creo un modelo en Django

1. Escribo la clase del modelo en models.py de mi app:

```python
from django.db import models

class MiModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()
```
# Un modelo representa una tabla en la base de datos.

2. Creo y aplico las migraciones:

```zsh
python manage.py makemigrations
python manage.py migrate
```
# Estos comandos crean y actualizan la base de datos segun los modelos que defini.
