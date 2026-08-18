import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x, dtype=torch.float32)
    e_plus = torch.exp(x)
    e_minus = torch.exp(-x)
    if method == "relu":
        return torch.clamp(x, min=0).tolist()
    elif method == "sigmoid":
        return (1 / (1 + e_minus)).tolist()
    elif method == "tanh":
        return ((e_plus - e_minus)/(e_plus + e_minus)).tolist()
    elif method == "leaky_relu":
        return torch.where(x <= 0, 0.01 * x, x).tolist()