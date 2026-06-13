# Learning-Project
This repository is for Jinxy to study ML optimization and algorithms

<!-- PROJECT_STRUCTURE_START -->

```text
Learning-Project/
├── .github/
│   └── workflows/
│       └── python-package.yml
├── data/
│   └── MNIST/
│       └── raw/
│           ├── t10k-images-idx3-ubyte
│           ├── t10k-images-idx3-ubyte.gz
│           ├── t10k-labels-idx1-ubyte
│           ├── t10k-labels-idx1-ubyte.gz
│           ├── train-images-idx3-ubyte
│           ├── train-images-idx3-ubyte.gz
│           ├── train-labels-idx1-ubyte
│           └── train-labels-idx1-ubyte.gz
├── experiments/
│   └── 00_start_test.ipynb
├── results/
├── src/
├── README.md
└── update_readme_tree.py
```

<!-- PROJECT_STRUCTURE_END -->

---
# Basic Knowledge preparation
- What is tensor? - a container with different integers which is samilar to the numpy array, and we can add different dimension.
For example, we can create `torch.tensor([1,2], [3,4])` which is `shape (2, 2)` and 2 dimensional
- `shape == (D0, D1, D2, ..., Dn-1)`, where the first index represents the dimension 1 and etc. 
    * `dim=0 represents　batch size`
    * `dim=1 represents　channel`
    * `dim=2 represents　height`
    * `dim=3 represents　width`
- Boardcasting: the operation help tensors with different shape to do addition
- Batch/ Epoch/ Iteration
    * Batch refers to the total number of sample give to the model.
    * Iteration(step) refers to the one `forward() + backward() + optimizer.step()`, one step process one batch.
    * 60000 images / batch size 64 = 938 steps, go through the whole datasize one time.
- 5 MNIST shape pipeline

---
# Phase 0 done by Jun-12th-2026
Setting the environment needed for the further practice.
## problem for 00_start_test
- For cell2, we use torch.randn(3, 4) to create a 2-dimensisonal matrix with random number.

- Given `x.shape == (3, 4)`, the result has shape `(4,)`.
    Rule: `sum(dim=k)` collapses the k-th axis, so the output shape is the 
    input shape with the k-th dimension removed.

- `x.sum(dim=0)` performs cross-sample aggregation. For each feature position j, it sums the values from all 3 samples at that position. The "which sample" information is discarded; the "per-feature total across the batch" is kept.

- Contrast: `x.sum(dim=1)` would be within-sample aggregation, summing the 4 features inside each sample.