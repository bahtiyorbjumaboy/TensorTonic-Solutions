import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    mean = np.mean(x)
    median = np.median(x)
    counts = Counter(x)
    mode = max(counts, key=counts.get)

    return {
        "mean": mean,
        "median": median,
        "mode": mode
    }