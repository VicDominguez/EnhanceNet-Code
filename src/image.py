import base64
from PIL import Image
import io
import numpy as np

"""Process input"""


def read_image_from_base64_file(path):
    with open(path, "r") as file:
        base64image = file.read()
    return read_image_from_base64(base64image)


def read_image_from_base64(base64image):
    img = base64.b64decode(str(base64image))
    img = Image.open(io.BytesIO(img)).convert('RGB')
    return img


def read_image_from_file_image(path):
    return Image.open(path).convert('RGB')


"""Image object to numpy array """


def preprocess_image_to_model(img):
    img = np.array(img) / 255
    return np.expand_dims(img, axis=0)


"""Numpy array to image object"""


def numpy_array_to_image(img):
    img *= 255.0
    img = (img.clip(0, 255) + 0.5).astype(np.uint8)

    if len(np.shape(img)) > 2 and np.shape(img)[2] == 1:
        img = np.reshape(img, (np.shape(img)[0], np.shape(img)[1]))
    img = img.astype(np.uint8)
    return Image.fromarray(img)


"""Process output"""


def save_image_to_image_file(img, path):
    im = numpy_array_to_image(img)
    im.save(path)


def save_image_to_base64_file(img, path):
    my_string = save_image_to_base64_string(img)
    with open(path, "w") as file:
        file.write(str(my_string, "utf-8"))


def save_image_to_base64_string(img):
    im = numpy_array_to_image(img)
    imgByteArr = io.BytesIO()
    im.save(imgByteArr, format='JPEG')
    imgByteArr = imgByteArr.getvalue()
    return base64.b64encode(imgByteArr)
