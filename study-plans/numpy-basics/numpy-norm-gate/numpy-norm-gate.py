import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    X = np.array(X)
    W = np.array(W)
    Z = X @ W

    return np.where(np.linalg.norm(Z, axis=1)[:, np.newaxis] < threshold, 0, Z)