---
title: "FedAnchor: Enhancing Federated Semi-Supervised Learning with Label Contrastive Loss for Unlabeled Clients"
collection: publications
permalink: /publication/2024-02-15-fedanchor
excerpt: 'FedAnchor is a methodology to solve federated semi-supervised learning problems.'
date: 2024-02-15
venue: 'arXiv'
paperurl: 'https://arxiv.org/abs/2402.10191'
citation: 'Xinchi Qiu, Yan Gao, Lorenzo Sani, Heng Pan, Wanru Zhao, Pedro P. B. Gusmao, Mina Alibeigi, Alex Iacob, & Nicholas D. Lane. (2024). FedAnchor: Enhancing Federated Semi-Supervised Learning with Label Contrastive Loss for Unlabeled Clients.'
---
FedAnchor is a methodology to solve federated semi-supervised learning problems.

[Download paper here](https://arxiv.org/abs/2402.10191)

Abstract:

> Federated learning (FL) is a distributed learning paradigm that facilitates collaborative training of a shared global model across devices while keeping data localized. The deployment of FL in numerous real-world applications faces delays, primarily due to the prevalent reliance on supervised tasks. Generating detailed labels at edge devices, if feasible, is demanding, given resource constraints and the imperative for continuous data updates. In addressing these challenges, solutions such as federated semi-supervised learning (FSSL), which relies on unlabeled clients' data and a limited amount of labeled data on the server, become pivotal. In this paper, we propose FedAnchor, an innovative FSSL method that introduces a unique double-head structure, called anchor head, paired with the classification head trained exclusively on labeled anchor data on the server. The anchor head is empowered with a newly designed label contrastive loss based on the cosine similarity metric. Our approach mitigates the confirmation bias and overfitting issues associated with pseudo-labeling techniques based on high-confidence model prediction samples. Extensive experiments on CIFAR10/100 and SVHN datasets demonstrate that our method outperforms the state-of-the-art method by a significant margin in terms of convergence rate and model accuracy.

Recommended citation: Xinchi Qiu, Yan Gao, Lorenzo Sani, Heng Pan, Wanru Zhao, Pedro P. B. Gusmao, Mina Alibeigi, Alex Iacob, & Nicholas D. Lane. (2024). FedAnchor: Enhancing Federated Semi-Supervised Learning with Label Contrastive Loss for Unlabeled Clients.
