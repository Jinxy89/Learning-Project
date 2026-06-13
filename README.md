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

# Phase 0 done by Jun-12th-2026
Setting the environment needed for the further practice.
## problem for 00_start_test
- For cell2, we use torch.randn(3, 4) to create a 2-dimensisonal matrix with random number.

-   Given `x.shape == (3, 4)`, the result has shape `(4,)`.
    Rule: `sum(dim=k)` collapses the k-th axis, so the output shape is the 
    input shape with the k-th dimension removed.

-  `x.sum(dim=0)` performs cross-sample aggregation. For each feature position j, it sums the values from all 3 samples at that position. The "which sample" information is discarded; the "per-feature total across the batch" is kept.

-   Contrast: `x.sum(dim=1)` would be within-sample aggregation, summing the 4 features inside each sample.