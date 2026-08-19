import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    d = np.array(data)

    return np.stack( [np.mean(d, axis), np.std(d, axis), np.min(d, axis), np.max(d, axis)] )