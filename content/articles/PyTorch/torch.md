Title: PyTroch 之 torch 包
Category: 教程
Date: 2018-10-12 11:27:17
Modified: 2018-10-12 12:36:32
Tags: PyTroch, 机器学习, 深度学习

[TOC]

## 1. 张量

```
torch.is_tensor(obj)
torch.is_storage(obj)
```

```
torch.set_default_dtype(d) // default: torch.float32
torch.get_default_dtype() → torch.dtype
torch.set_default_tensor_type(t) // default: torch.FloatTensor
```

```
torch.numel(input) → int
torch.set_printoptions(precision=None, threshold=None,
    edgeitems=None, linewidth=None, profile=None)
torch.set_flush_denormal(mode) → bool
```

### 1.1 创建

```
torch.tensor(data, dtype=None, device=None, requires_grad=False)
 → Tensor
```

```
torch.sparse_coo_tensor(indices, values, size=None, dtype=None,
    device=None, requires_grad=False) → Tensor
```

```
torch.as_tensor(data, dtype=None, device=None) → Tensor
torch.from_numpy(ndarray) → Tensor
torch.zeros(*sizes, out=None, dtype=None, layout=torch.strided,
    device=None, requires_grad=False) → Tensor
torch.zeros_like(input, dtype=None, layout=None, device=None,
    requires_grad=False) → Tensor
torch.ones(*sizes, out=None, dtype=None, layout=torch.strided,
    device=None, requires_grad=False) → Tensor
torch.ones_like(input, dtype=None, layout=None, device=None,
    requires_grad=False) → Tensor
torch.arange(start=0, end, step=1, out=None, dtype=None,
    layout=torch.strided, device=None, requires_grad=False) → Tensor
torch.range(start=0, end, step=1, out=None, dtype=None,
    layout=torch.strided, device=None, requires_grad=False) → Tensor
torch.linspace(start, end, steps=100, out=None, dtype=None,
    layout=torch.strided, device=None, requires_grad=False) → Tensor
torch.logspace(start, end, steps=100, out=None, dtype=None,
    layout=torch.strided, device=None, requires_grad=False) → Tensor
torch.eye(n, m=None, out=None, dtype=None, layout=torch.strided,
    deviceNone, requires_grad=False) → Tensor
torch.empty(*sizes, out=None, dtype=None, layout=torch.strided,
    device=None, requires_grad=False) → Tensor
torch.empty_like(input, dtype=None, layout=None, device=None,
    requires_grad=False) → Tensor
torch.full(size, fill_value, out=None, dtype=None,
    layout=torch.strided, device=None, requires_grad=False) → Tensor
torch.full_like(input, fill_value, out=None, dtype=None,
    layout=torch.strided, device=None, requires_grad=False) → Tensor
```

### 1.2 切片、索引、连接和转换操作

```
torch.cat(tensors, dim=0, out=None) → Tensor
torch.chunk(tensor, chunks, dim=0) → List of Tensors
torch.gather(input, dim, index, out=None) → Tensor
torch.index_select(input, dim, index, out=None) → Tensor
torch.masked_select(input, mask, out=None) → Tensor
torch.narrow(input, dimension, start, length) → Tensor
torch.nonzero(input, out=None) → LongTensor
torch.reshape(input, shape) → Tensor
torch.split(tensor, split_size_or_sections, dim=0)
torch.squeeze(input, dim=None, out=None) → Tensor
torch.stack(seq, dim=0, out=None) → Tensor
torch.t(input) → Tensor
torch.take(input, indices) → Tensor
torch.transpose(input, dim0, dim1) → Tensor
torch.unbind(tensor, dim=0) → seq
torch.unsqueeze(input, dim, out=None) → Tensor
torch.where(condition, x, y) → Tensor
```

## 1.3 随机采样

```
torch.manual_seed(seed) → torch._C.Generator
torch.initial_seed()
torch.get_rng_state()
```
