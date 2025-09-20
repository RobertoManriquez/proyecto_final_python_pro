# Aquí se configura y ejecuta la aplicación web con Flask.

# Flask: framework ligero para crear aplicaciones web en Python.
# Nos permite definir rutas, renderizar plantillas (HTML) y manejar peticiones.
from flask import Flask, render_template

# datetime: librería estándar de Python que facilita trabajar con fechas y horas.
# Aquí la usamos para obtener el año actual y mostrarlo en el footer.
from datetime import datetime

# os: librería estándar de Python que permite interactuar con el sistema operativo.
# Muy útil para manejar rutas de archivos o configuraciones a través de variables de entorno.
import os

# Inicializamos la aplicación Flask
# Flask automáticamente buscará:
# - "templates/" para los archivos HTML
# - "static/" para los archivos estáticos (css, imágenes, js)
app = Flask(__name__)

# Ruta principal (cuando se entra a "/")
@app.route("/")
def index():
    # Obtenemos el año actual con Python
    year = datetime.now().year

    # Ejemplo de uso de os:
    # obtenemos el nombre del usuario que ejecuta la aplicación
    usuario = os.getenv("USER", "Invitado")

    # Renderizamos la plantilla HTML "index.html"
    # y le pasamos el valor de "year" para usarlo en el footer
    # También enviamos el nombre de usuario (aunque es opcional mostrarlo)
    return render_template("index.html", year=year, usuario=usuario)

# Ejecutamos el servidor
if __name__ == "__main__":
    # host="0.0.0.0" → permite que funcione en la red local
    # port=5001 → número del puerto (se puede cambiar si está ocupado)
    # debug=True → reinicia el servidor automáticamente al guardar cambios
    app.run(host="0.0.0.0", port=5001, debug=True)
