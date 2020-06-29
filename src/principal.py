import base64

from controlador_modelo import *
from flask import Flask, jsonify, request, abort, make_response
import imghdr

app = Flask(__name__)


def comprueba_imagen(string_base64):
    """Comprueba si la imagen es válida y devuelve el tipo correspondiente"""
    try:
        resultado = imghdr.what("ac", h=base64.b64decode(str(string_base64)))
    except:
        resultado = None
    return resultado


"""Manejador para el error 404"""


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


"""Función que llama al controlador del modelo revisando los parámetros. Necesita una petición con el campo
imagen y la imagen codificada en base64 y revuelve la imagen codificada en base64"""


@app.route('/TFG-Computadores/api-aumento/aumento', methods=['POST'])
def realizar_aumento():
    if not request.json or 'imagen' not in request.json:
        abort(402)
    imagen = request.json['imagen']
    tipo_imagen = comprueba_imagen(imagen)
    if tipo_imagen is not None:
        resultado = ampliar_desde_string_base64_a_string_base64(imagen, formato_imagen=tipo_imagen)
        return jsonify({"imagen_ampliada": str(resultado)}), 200
    else:
        abort(400)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
