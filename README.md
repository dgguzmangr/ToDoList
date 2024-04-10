### Aplicación de Gestión de Tareas

La aplicación de Gestión de Tareas es una herramienta diseñada para ayudar a los usuarios a organizar y realizar un seguimiento de sus tareas diarias, asignándoles proyectos, tareas y subtareas.

## Características

Crear, ver, actualizar y eliminar proyectos.
Crear, ver, actualizar y eliminar tareas.
Crear, ver, actualizar y eliminar subtareas.
Almacenar fecha y hora de creación de proyectos.
Almacenar fecha y hora de creación de tareas.
Almacenar fecha y hora de creación de subtareas.
Establecer fechas de vencimiento para proyectos.
Establecer fechas de vencimiento para tareas.
Establecer fechas de vencimiento para subtareas.
Filtrar y buscar tareas por diferentes criterios.

## Tecnologías Utilizadas

Django: Framework web de alto nivel escrito en Python.
PostgreSQL: Sistema de gestión de bases de datos relacional.

## Configuración del Entorno

#  Clona el repositorio desde GitHub:

git clone https://github.com/dgguzmangr/ToDoList.git

# Crea y activa un entorno virtual:

python -m venv venv
source venv/bin/activate  # En Linux/Mac
source\venv\Scripts\activate   # En Windows

# Instala las dependencias del proyecto:

pip install -r requirements.txt

# Configura la base de datos PostgreSQL en settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('db_name'),
        'USER': config('user_db'),
        'PASSWORD': config('password'),
        'HOST': config('db_host'),
        'PORT': config('db_port'),
    }
}

# Realiza las migraciones:

python manage.py makemigrations
python manage.py migrate
Ejecuta el servidor de desarrollo:

python manage.py runserver

# Uso

Abre tu navegador web y accede a    http://localhost:8000/swagger/
                                    http://127.0.0.1:8000/admin/


Podrás ver todas tus tareas y realizar las acciones necesarias (crear, editar, eliminar, marcar como completada).
Utiliza los filtros y la búsqueda para encontrar tareas específicas según tus necesidades.

# Contribución
Si deseas contribuir a este proyecto, ¡te damos la bienvenida! Siempre estamos abiertos a nuevas ideas y mejoras. Siéntete libre de enviar pull requests.

# Licencia
Este proyecto está bajo la Licencia MIT.