import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    w = np.zeros(X.shape[1])
    b = 0
    for step in range(steps):
        pred = _sigmoid(X @ w + b)
        w_grad = 1/X.shape[0] * X.T @ (pred - y)
        b_grad = np.mean(pred - y)

        w -= lr * w_grad
        b -= lr * b_grad

    return w, b