import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    x, y = torch.tensor(x), torch.tensor(y)
    if op == "add":
        return torch.add(x, y)
    elif op == "multiply":
        return torch.mul(x, y)
    elif op == "matmul":
        return torch.matmul(x, y)
    elif op == "power":
        return torch.pow(x, y)
    elif op == "max":
        return torch.max(x, y)
    else:
        raise ValueError("Unknown operation")