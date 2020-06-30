import base64
from PIL import Image
import io
import numpy as np

"""Funciones para procesar la entrada"""


def abrir_imagen_desde_archivo_base64(ruta):
    with open(ruta, "r") as archivo:
        string_base64 = archivo.read()
    return abrir_imagen_desde_string_base64(string_base64)


def abrir_imagen_desde_string_base64(string_base64):
    imagen = base64.b64decode(str(string_base64))
    return Image.open(io.BytesIO(imagen)).convert('RGB')


def abrir_imagen_desde_archivo_imagen(ruta):
    return Image.open(ruta).convert('RGB')


"""Preprocesado"""


def preprocesar_imagen(imagen):
    imagen = np.array(imagen) / 255
    # Añadimos el cuarto eje debido a que tensorflow necesita un tensor 4D
    return np.expand_dims(imagen, axis=0)


"""Procesado salida"""


def _numpy_array_a_imagen(imagen):
    # Multiplicamos el rango por 255 y lo cortamos a 0-255 pasa pasarlo a entero de 1 byte sin signo
    imagen *= 255.0
    imagen = (imagen.clip(0, 255) + 0.5).astype(np.uint8)
    if len(np.shape(imagen)) > 2 and np.shape(imagen)[2] == 1:
        imagen = np.reshape(imagen, (np.shape(imagen)[0], np.shape(imagen)[1]))
    return Image.fromarray(imagen)


def guardar_imagen_archivo_imagen(imagen, ruta):
    im = _numpy_array_a_imagen(imagen)
    im.save(ruta)


def guardar_imagen_a_archivo_base64(imagen, ruta, formato_imagen="JPEG"):
    imagen_base64_string = guardar_imagen_a_string_base64(imagen, formato_imagen)
    with open(ruta, "w") as archivo:
        archivo.write(str(imagen_base64_string, "utf-8"))


def guardar_imagen_a_string_base64(imagen, formato_imagen="JPEG"):
    imagen = _numpy_array_a_imagen(imagen)
    imagen_bytes = io.BytesIO()
    imagen.save(imagen_bytes, format=formato_imagen)
    imagen_bytes = imagen_bytes.getvalue()
    return str(base64.b64encode(imagen_bytes), "utf-8")
