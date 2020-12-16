import torch
from torch import nn

torch.manual_seed(0)

x = torch.empty(1, 2, dtype=torch.double)
# print("Uniform Result: \n", nn.init.uniform_(x))
print("Kaiming Uniform Result: \n", nn.init.kaiming_uniform_(
    x, mode='fan_in', nonlinearity='leaky_relu'))
