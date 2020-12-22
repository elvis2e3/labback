LabBack
==================================

Proceso de instalación
----------------------
+ Instalar los requerimientos 
  > pip install -r requirements.txt
+ Ejecutar el proyecto
  > python manage.py runserver

Proceso de instalación con Docker
----------------------
+ Construir el contenedor
  > docker build . -t elvis2e3/labback:latest
+ Ejecutar el proyecto 
  > docker run -d -p 8000:80 elvis2e3/labback:latest