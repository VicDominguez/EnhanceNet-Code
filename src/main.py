import base64

from use_model import *
from flask import Flask, jsonify, request, abort, make_response
import imghdr

app = Flask(__name__)


def check_image(base64image):
    try:
        resultado = imghdr.what("ac", h=base64.b64decode(str(base64image)))
    except:
        resultado = None
    return resultado


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/TFG-Computadores/api-upsample/upsample', methods=['POST'])
def make_upsample():
    if not request.json or not 'image' in request.json:
        abort(400)
    image = request.json['image']
    result = check_image(image)
    if result is not None:
        result = str(resize_from_b64_to_b64(image))
    else:
        abort(401)

    return jsonify({"upsampled": result}), 400


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True, host="0.0.0.0")
