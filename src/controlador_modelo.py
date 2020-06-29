from modelo import inferencia
from procesado import *


def _realizar_ampliacion(image):
    return inferencia(preprocesar_imagen(image))


def ampliar_desde_archivo_base64_a_archivo_base64(ruta_entrada, ruta_salida):
    imagen_entrada = abrir_imagen_desde_archivo_base64(ruta_entrada)
    imagen_ampliada = _realizar_ampliacion(imagen_entrada)
    guardar_imagen_a_archivo_base64(imagen_ampliada, ruta_salida)


def ampliar_desde_archivo_base64_a_archivo_imagen(ruta_entrada, ruta_salida):
    imagen_entrada = abrir_imagen_desde_archivo_base64(ruta_entrada)
    imagen_ampliada = _realizar_ampliacion(imagen_entrada)
    guardar_imagen_archivo_imagen(imagen_ampliada, ruta_salida)


def ampliar_desde_archivo_imagen_a_archivo_imagen(ruta_entrada, ruta_salida):
    imagen_entrada = abrir_imagen_desde_archivo_imagen(ruta_entrada)
    imagen_ampliada = _realizar_ampliacion(imagen_entrada)
    guardar_imagen_archivo_imagen(imagen_ampliada, ruta_salida)


def ampliar_desde_archivo_imagen_a_archivo_base64(ruta_entrada, ruta_salida):
    imagen_entrada = abrir_imagen_desde_archivo_imagen(ruta_entrada)
    imagen_ampliada = _realizar_ampliacion(imagen_entrada)
    guardar_imagen_a_archivo_base64(imagen_ampliada, ruta_salida)


def ampliar_desde_string_base64_a_string_base64(string_base64, formato_imagen="JPEG"):
    imagen_entrada = abrir_imagen_desde_string_base64(string_base64)
    imagen_ampliada = _realizar_ampliacion(imagen_entrada)
    return guardar_imagen_a_string_base64(imagen_ampliada,formato_imagen=formato_imagen)
