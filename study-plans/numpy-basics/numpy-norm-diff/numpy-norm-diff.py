import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""
    a = np.array(a)
    b = np.array(b)

    a_ = np.clip(a, lo, hi)
    b_ = np.clip(b, lo, hi)

    a_rescale = (a_ - lo) / (hi - lo)
    b_rescale = (b_ - lo) / (hi - lo)

    return np.abs(a_rescale - b_rescale)