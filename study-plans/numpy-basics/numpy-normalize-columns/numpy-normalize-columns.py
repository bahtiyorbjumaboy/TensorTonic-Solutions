import numpy as np

def normalize(data):
    """Returns: np.ndarray of shape (m, n), z-score normalized per column"""
    d = np.array(data)
    mean = np.mean(d, axis=0)
    std = np.std(d, axis=0)

    return (d - mean) / std