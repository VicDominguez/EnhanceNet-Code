from use_model import *
from utils import get_input_path, get_output_path
if __name__ == "__main__":
    # Your images and code here
    # Example
    print("Processing eagle")
    resize_from_image_file_to_image_file(get_input_path("eagle.png"), get_output_path("eagle.png"))
