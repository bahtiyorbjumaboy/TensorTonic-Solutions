import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    d = np.array(data)

    return np.stack([
        np.sort(d, axis),
        np.argsort(d, axis)
    ])