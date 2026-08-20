import torch

def compute_loss(pred, target, method, delta=1.0):
    """
    Returns: float, the mean loss value
    """
    n = len(target)
    pred = torch.tensor(pred, dtype=torch.float)
    target = torch.tensor(target, dtype=torch.float)
    if method == "mse":
        return 1/n * torch.sum((pred - target) ** 2)
    elif method == "cross_entropy":
        target = torch.tensor(target, dtype=torch.long)
        max_val = pred.max(dim=1, keepdim=True).values
        shifted = pred - max_val
        log_sum_exp = shifted.exp().sum(dim=1).log() + max_val.squeeze(1)
        correct_logits = pred[torch.arange(pred.shape[0]), target]
        return (log_sum_exp - correct_logits).mean().item()
        
    elif method == "huber":
        diff = (pred - target).abs()
        loss = torch.where(diff <= delta, 0.5 * diff ** 2, delta * (diff - 0.5 * delta))
        return loss.mean().item()