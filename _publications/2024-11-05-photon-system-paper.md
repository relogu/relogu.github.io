---
title: "Photon: Federated LLM Pre-Training"
collection: publications
permalink: /publication/2024-11-05-photon-system-paper
excerpt: 'We present Photon, the first fully federated system for the federated pre-training of large language models.'
date: 2024-11-05
venue: 'MLSys 2025 - The Eighth Annual Conference on Machine Learning and Systems'
paperurl: 'https://arxiv.org/abs/2411.02908'
citation: 'Lorenzo Sani, Alex Iacob, Zeyu Cao, Royson Lee, Bill Marino, Yan Gao, Dongqi Cai, Zexi Li, Wanru Zhao, Xinchi Qiu, & Nicholas D. Lane. (2024). Photon: Federated LLM Pre-Training.'
---
We present Photon, the first fully federated system for the federated pre-training of large language models.
The code will be soon released.
The paper has been accepted at MLSys 2025.

[Photon System paper](https://arxiv.org/abs/2411.02908)

Abstract:

> Scaling large language models (LLMs) demands extensive data and computing resources, which are traditionally constrained to data centers by the high-bandwidth requirements of distributed training. Low-bandwidth methods like federated learning (FL) could enable collaborative training of larger models across weakly-connected GPUs if they can effectively be used for pre-training. To achieve this, we introduce Photon, the first complete system for federated end-to-end LLM training, leveraging cross-silo FL for global-scale training with minimal communication overheads. Using Photon, we train the first federated family of decoder-only LLMs from scratch. We show that: (1) Photon can train model sizes up to 7B in a federated fashion while reaching an even better perplexity than centralized pre-training; (2) Photon model training time decreases with available compute, achieving a similar compute-time trade-off to centralized; and (3) Photon outperforms the wall-time of baseline distributed training methods by 35% via communicating 64x-512xless. Our proposal is robust to data heterogeneity and converges twice as fast as previous methods like DiLoCo. This surprising data efficiency stems from a unique approach combining small client batch sizes with extremely high learning rates, enabled by federated averaging's robustness to hyperparameters. Photon thus represents the first economical system for global internet-wide LLM pre-training.

Recommended citation: Lorenzo Sani, Alex Iacob, Zeyu Cao, Royson Lee, Bill Marino, Yan Gao, Dongqi Cai, Zexi Li, Wanru Zhao, Xinchi Qiu, & Nicholas D. Lane. (2024). Photon: Federated LLM Pre-Training.
