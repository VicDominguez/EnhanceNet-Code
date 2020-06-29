import numpy as np
import pathlib

PER_CHANNEL_MEANS = np.array([0.47614917, 0.45001204, 0.40904046])
_ruta_pesos = pathlib.Path("./weights")

_carpeta_entrada = pathlib.Path("../input")
_carpeta_salida = pathlib.Path("../output")


def _ruta_a_string(path):
    """Convert Path object to absolute path string."""
    return str(path.resolve())


def obtener_ruta_pesos():
    return _ruta_a_string(_ruta_pesos)


def obtener_ruta_archivo_entrada(archivo):
    """Devuelve la ruta para un nombre de archivo de entrada"""
    return (_carpeta_entrada / archivo).resolve()


def obtener_ruta_archivo_salida(archivo):
    """Devuelve la ruta para un nombre de archivo de salida"""
    return (_carpeta_salida / archivo).absolute()
