import numpy as np

def angle_features(angles):
    """Returns: np.ndarray of shape (3, n), rows are sin, cos, tan"""
    a = np.array(angles)

    return np.array( [np.sin(a), np.cos(a), np.tan(a)] )