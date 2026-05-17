import torch


def add_tensors(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    result = torch.add(x, y)
    return result.tolist()

a = torch.tensor([12,34,56], dtype=torch.int32)
b = torch.tensor([78,90,12], dtype=torch.int32)
c = add_tensors(a, b)
print(c)
