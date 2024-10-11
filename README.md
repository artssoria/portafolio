# Porfolio Django

Para empezar debemos crear un entorno virtual.
```bash
    python -m venv porfolio-env
```
##### Activo el entorno virtual.

```bash
    source porfolio-env/Scripts/activate #En Windows
```

##### Instalar la dependencia necesaria para el entorno virtual en este caso Django 4.1

```bash
    pip install Django==4.1
```

##### Para crear un proyecto nuevo e iniciarlo debemos usar el comando django-admin.

```bash
    django-admin startproject portafolio
```

##### Despues para crear un app dentro del proyecto en cuestion vamos a usar otro comando startapp.

```bash
    python manage.py startapp portafolio #Esta va a ser la raiz de nuestro proyecto
```

##### Despues debemos crear otra app dentro del proyecto con el mismo comando.

```bash
    python manage.py startapp core #Va a ser la app que va a interactuar con el proyecto.
```

Para registrar la app recientemente creada debemos modificar el archivo ***portafolio/settings.py***


```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core', #Incorporamos la app que va a interactuar con el proyecto
]
```

Despues hacemos la migraciones de la BBDD para que se creen los componentes en la base de datos que va a tomar las vistas de usuarios, administradores y más.

```bash
    python manage.py migrate 
```

Crear un super usuario para administrar el panel de administración de la aplicación.

```bash
    python manage.py createsuperuser
```
- En la misma terminal le va a solicitar un nombre de usuario.
  * Por convención siempre suele utilizarse el usuario "admin".
Entonces:

Nombre de usuario : admin
Dirección de correo electrónico: admin@admin.com
Password:

En este apartado la contraseña no se vizualiza en la terminal por cuestiones de seguridad, aquí habrá que recordar qué teclas usamos y como configuramos la contraseña. Por obvias razones, al crear un usuario de tales caracteristicas, la contreña será **admin**. 

Nos va a solicitar de nuevo la contreseña para configurarla definitivamente, le ponemos la misma.

Despues nos va a preguntar si queremos que utilize un método de validación Bypass ingresemos la tecla **N**
Al último los va a arrojar el siguente texto

```bash
    Superuser created successfully  # Esto quiere decir que el super usuario se a creado de manera éxitosa.
```

##### Iniciamos el servidor para verificar

```bash
    python manage.py runserver
```
En la terminal deberiamos tener esta respuesta.

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 11, 2024 - 16:51:44
Django version 4.1, using settings 'portafolio.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

* Ingresamos a la dirección http://127.0.0.1:8000/

Se va renderizar la vista principal de la pagina

* Ahora para ingresar al panel de control debemos dirigirmos a la dirección

```bash
    http://127.0.0.1:8000/admin
```

* Cuando cargue la vista nos va a pedir usuario y contraseña. Allí debemos cargar el mismo usuario que hemos creado anteriormente. 

 - Usuario: admin
 - Contraseña : admin