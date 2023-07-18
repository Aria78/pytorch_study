import torch

# Tensor Math and Comparison Operations

x = torch.tensor([1,2,3])
y = torch.tensor([2,3,4])

# addition
z1 = torch.empty(3)
torch.add(x,y,out=z1)

z2 = torch.add(x,y)
z3 = x + y #z1, z2 and z3 are identical

z = x - y
z += x

z = torch.true_divide((x,y))