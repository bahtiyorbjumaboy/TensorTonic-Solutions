import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    """
    Returns: two-layer MLP output (linear -> ReLU -> linear)
    """

    def __init__(self, in_features, hidden_size, out_features):
        super().__init__()
        self.nn = nn.Sequential(
            nn.Linear(in_features, hidden_size),
            nn.ReLU(hidden_size),
            nn.Linear(hidden_size, out_features)
        )

    def forward(self, x):
        return self.nn(x)
