FROM python:3.8

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos del directorio actual al contenedor
COPY requirements.txt /app/requierements.txt

#Instalacion de requerimientos
#pip: como ya indicamos el entorno (python:3.8) no es necesario indicarle pip3
#--no-cache-dir : No aplique el cache
#--upgrade: actualización del gestor de paquetes pip
RUN pip install --no-cache-dir --upgrade -r /app/requierements.txt

COPY . /app

#Mantener el servicio encendido
CMD bash -c "while true; do sleep 1; done"