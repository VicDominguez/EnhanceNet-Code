import numpy as np
import pathlib

PER_CHANNEL_MEANS = np.array([0.47614917, 0.45001204, 0.40904046])
_weights_path = pathlib.Path("./weights")


def _path_2_string(path):
    """Convert Path object to absolute path string."""
    return str(path.resolve())


def get_weights_path():
    return _path_2_string(_weights_path)
