import tensorflow as tf
from utils import PER_CHANNEL_MEANS, obtener_ruta_pesos

tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


def _conv(h, n=64):
    """Capa de convolución 2D"""
    return tf.contrib.layers.convolution2d(h, n, kernel_size=3, stride=1, padding='SAME', activation_fn=None)


def _relu(h):
    """Función de activación relú"""
    return tf.nn.relu(h)


def _ampliar(h):
    """Capa para ampliar la imagen en un factor de 2"""
    return tf.image.resize(h, [2 * tf.shape(h)[1], 2 * tf.shape(h)[2]],
                           method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)


def _bloque_residual(h, subcapas):
    """Crea el bloque residual a partir de las subcapas que entran por parámetro"""
    htemp = h
    for subcapa in subcapas:
        h = subcapa[0](h, *subcapa[1:])
    h += htemp
    return h


def _crear_red(nombre, capas):
    """Crea la red a partir de una lista de capas"""
    h = capas[0]
    with tf.compat.v1.variable_scope(nombre, reuse=False) as scope:
        for capa in capas[1:]:
            h = capa[0](h, *capa[1:])
    return h


def inferencia(imagen):
    """Crea la red, carga los pesos y amplia la imagen de entrada en un factor de 4"""
    tamanio_imagen = imagen.shape[1:]
    # Creamos el placeholder de la entrada del grafo de tensorflow
    entrada_placeholder = tf.compat.v1.placeholder(tf.float32,
                                                   [1, tamanio_imagen[0], tamanio_imagen[1], tamanio_imagen[2]])
    # Definimos la red
    bloque_r = [_bloque_residual, [[_conv], [_relu], [_conv]]]
    salida_estimada = _crear_red('generator',
                                 [entrada_placeholder,
                                  [_conv], [_relu],
                                  bloque_r, bloque_r, bloque_r, bloque_r, bloque_r,
                                  bloque_r, bloque_r, bloque_r, bloque_r, bloque_r,
                                  [_ampliar], [_conv], [_relu],
                                  [_ampliar], [_conv], [_relu],
                                  [_conv], [_relu],
                                  [_conv, 3]])
    # Definimos la imagen bicubica y configuramos la salida
    imagen_bicubica = tf.image.resize_images(entrada_placeholder, [4 * tamanio_imagen[0], 4 * tamanio_imagen[1]],
                                             method=tf.image.ResizeMethod.BICUBIC)
    salida_estimada += imagen_bicubica + PER_CHANNEL_MEANS
    # Creamos la sesion, cargamos los pesos y ejecutamos
    sess = tf.compat.v1.InteractiveSession()
    tf.compat.v1.train.Saver().restore(sess, obtener_ruta_pesos())
    salida = sess.run(salida_estimada, feed_dict={entrada_placeholder: imagen - PER_CHANNEL_MEANS})
    sess.close()
    tf.compat.v1.reset_default_graph()
    return salida[0]
