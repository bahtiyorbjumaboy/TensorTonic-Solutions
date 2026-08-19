import numpy as np

def scale_cols(data, weights):
    """Returns: np.ndarray of shape (m, n), each column scaled by corresponding weight"""
    d = np.array(data)
    w = np.array(weights)

    return d * w