---
title: "SparsyFed: Sparse Adaptive Federated Training"
collection: publications
excerpt: 'This work proposes a novel approach to sparse federated training that does not require to fix a global mask to be efficient.'
permalink: /publication/2024-10-07-dept
date: 2024-10-07
venue: 'ICLR 2025 - The Thirteenth International Conference on Learning Representations'
paperurl: 'https://openreview.net/forum?id=OBUQNASaWw'
citation: 'Adriano Guastella*, Lorenzo Sani*, Alex Iacob, Alessio Mora, Paolo Bellavista, & Nicholas Donald Lane (2025). SparsyFed: Sparse Adaptive Federated Learning. In The Thirteenth International Conference on Learning Representations.
'
---
We present SparsyFed, a novel approach to sparse federated training that does not require to fix a global mask to be efficient.
SparsyFed allows federated clients to manipulate their own sparsity masks, while retaining an impressive global model performance on the server.

[Download the paper here.](https://openreview.net/forum?id=OBUQNASaWw)

Abstract:

> Sparse training is often adopted in cross-device federated learning (FL) environments where constrained devices collaboratively train a machine learning model on private data by exchanging pseudo-gradients across heterogeneous networks. Although sparse training methods can reduce communication overhead and computational burden in FL, they are often not used in practice for the following key reasons: (1) data heterogeneity impacts more clients’ consensus on sparse models compared to dense models, requiring longer training; (2) there is a lack of sufficient plasticity to adapt to never-seen data distributions, crucial in cross-device FL; and (3) additional hyperparameters are required, which are notably challenging to tune in FL. This paper presents SparsyFed, a practical federated sparse training method that critically addresses the problems above. Previous works have only solved one or two of these challenges at the expense of introducing new trade-offs, such as clients’ consensus on masks versus sparsity pattern plasticity. We show that SparsyFed simultaneously (1) can produce 95% sparse models, with negligible degradation in accuracy, while only needing a single hyperparameter, (2) achieves a per-round weight regrowth 200 times smaller than previous methods, and (3) still offers plasticity under this sparse design, by outperforming all the baselines at adapting to never-seen data distributions.

Recommended citation: Adriano Guastella*, Lorenzo Sani*, Alex Iacob, Alessio Mora, Paolo Bellavista, & Nicholas Donald Lane (2025). SparsyFed: Sparse Adaptive Federated Learning. In The Thirteenth International Conference on Learning Representations.
