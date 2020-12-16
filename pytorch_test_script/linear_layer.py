import torch
from torch import nn

torch.manual_seed(0)

m = nn.Linear(4, 3)
input = torch.full((2,4), 1.5, requires_grad=True)
output = m(input)
print("Result: ", output)
output.sum().backward()
print("Input Grad: ",input.grad)
