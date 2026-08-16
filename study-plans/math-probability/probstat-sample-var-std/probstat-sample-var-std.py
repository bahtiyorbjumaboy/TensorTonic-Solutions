import numpy as np

def sample_var_std(x):
    """
    Returns: dict with 'variance' and 'std_dev' as floats.
    """
    mean = np.mean(x)
    denom = len(x) - 1
    var = 1 / denom * np.sum((x - mean) ** 2)
    std = np.sqrt(var)

    return {
        "variance": var,
        "std_dev": std
    }