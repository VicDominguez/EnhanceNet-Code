import tensorflow as tf
from utils import PER_CHANNEL_MEANS, get_weights_path


""" neural network layers """


def conv(h, n=64):
    h = tf.contrib.layers.convolution2d(h, n, kernel_size=3, stride=1, padding='SAME', activation_fn=None)
    return h


def relu(h):
    h = tf.nn.relu(h)
    return h


def upsample(h):
    h = tf.image.resize_images(h, [2 * tf.shape(h)[1], 2 * tf.shape(h)[2]],
                               method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    return h


def resi(h, sublayers):
    htemp = h
    for layer in sublayers:
        h = layer[0](h, *layer[1:])
    h += htemp
    return h


def NN(name, layers):
    h = layers[0]
    with tf.compat.v1.variable_scope(name, reuse=False) as scope:
        for layer in layers[1:]:
            h = layer[0](h, *layer[1:])
    return h


def inference(image):
    img_size = image.shape[1:]
    xs = tf.compat.v1.placeholder(tf.float32, [1, img_size[0], img_size[1], img_size[2]])
    rblock = [resi, [[conv], [relu], [conv]]]
    ys_est = NN('generator',
                [xs,
                 [conv], [relu],
                 rblock, rblock, rblock, rblock, rblock,
                 rblock, rblock, rblock, rblock, rblock,
                 [upsample], [conv], [relu],
                 [upsample], [conv], [relu],
                 [conv], [relu],
                 [conv, 3]])
    ys_res = tf.image.resize_images(xs, [4 * img_size[0], 4 * img_size[1]], method=tf.image.ResizeMethod.BICUBIC)
    ys_est += ys_res + PER_CHANNEL_MEANS
    sess = tf.compat.v1.InteractiveSession()
    tf.compat.v1.train.Saver().restore(sess, get_weights_path())
    output = sess.run(ys_est, feed_dict={xs: image - PER_CHANNEL_MEANS})
    sess.close()
    tf.compat.v1.reset_default_graph()
    return output[0]
