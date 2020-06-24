from enhancenet import inference
from image import *


def _get_upsample_raw(image):
    return inference(preprocess_image_to_model(image))


def resize_from_b64_file_to_b64_file(input_path, output_path):
    image_input = read_image_from_base64_file(input_path)
    image_upsampled = _get_upsample_raw(image_input)
    save_image_to_base64_file(image_upsampled, output_path)


def resize_from_b64_file_to_image_file(input_path, output_path):
    image_input = read_image_from_base64_file(input_path)
    image_upsampled = _get_upsample_raw(image_input)
    save_image_to_image_file(image_upsampled, output_path)


def resize_from_image_file_to_image_file(input_path, output_path):
    image_input = read_image_from_file_image(input_path)
    image_upsampled = _get_upsample_raw(image_input)
    save_image_to_image_file(image_upsampled, output_path)


def resize_from_image_file_to_b64_file(input_path, output_path):
    image_input = read_image_from_file_image(input_path)
    image_upsampled = _get_upsample_raw(image_input)
    save_image_to_base64_file(image_upsampled, output_path)
