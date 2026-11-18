# Usar una imagen oficial de Python súper ligera
FROM python:3.11-slim

# Establecer variables de entorno para que Python no escriba archivos .pyc
# y envíe la salida estándar directamente a la terminal (útil para logs)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el archivo de dependencias e instalar
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente de tu computadora al contenedor
COPY . /app/

# Exponer el puerto en el que correrá Django
EXPOSE 8000

# Comando por defecto al levantar el contenedor (usaremos Gunicorn en prod)
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]