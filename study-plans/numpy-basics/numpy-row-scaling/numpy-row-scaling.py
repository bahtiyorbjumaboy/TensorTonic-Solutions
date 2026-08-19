import numpy as np

def scale_rows(data, weights):
    """Returns: np.ndarray of shape (m, n), each row scaled by corresponding weight"""
    d = np.array(data)
    w = np.array(weights)

    return w[:, np.newaxis] * d