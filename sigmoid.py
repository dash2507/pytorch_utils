import torch

input = torch.ones((2,3), requires_grad=True)
result = torch.sigmoid(input)
print(result)
result.sum().backward()
print(input.grad)
