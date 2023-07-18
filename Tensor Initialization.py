import torch

# Initializing tensor
device = 'cuda' if torch.cuda.is_available() else 'cpu'
my_tensor = torch.tensor([[1,2,3],[4,5,6]], dtype=torch.float32,
                         device=device, requires_grad=True)
# can change to "cuda", "cpu" is default

print(my_tensor)
print(my_tensor.dtype)
print(my_tensor.device)

# other common initialization methods
x = torch.empty(size=(3,3))
x = torch.zeros((3,3))

# how to initialize and convert tensors to other types
tensor = torch.arange(4)
print(tensor.bool())
print(tensor.double())
print(tensor.half())

# array to tensor conversion
import numpy as np
np_array = np.zeros((5,5))
tensor = torch.from_numpy(np_array)
np_array_back = tensor.numpy()
