import torch
import torch.nn.functional as F

input = torch.full((2,3), 2.0, requires_grad=True)
target = torch.full((2,3), 1.0)

loss = F.binary_cross_entropy(torch.sigmoid(input), target)
print(loss)
loss.backward()
print(input.grad)
