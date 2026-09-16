---
title: "The Future of Large Language Model Pre-training is Federated"
collection: publications
permalink: /publication/2024-05-17-photon-tech-report
excerpt: 'We present in this work the first fully federated system for the federated pre-training of large language models.'
date: 2024-05-17
venue: "International Workshop on Federated Foundation Models In Conjunction with NeurIPS 2024 (FL@FM-NeurIPS'24)"
paperurl: 'https://arxiv.org/abs/2405.10853'
citation: 'Lorenzo Sani, Alex Iacob, Zeyu Cao, Bill Marino, Yan Gao, Tomas Paulik, Wanru Zhao, William F. Shen, Preslav Aleksandrov, Xinchi Qiu, & Nicholas D. Lane. (2024). The Future of Large Language Model Pre-training is Federated.'
---
We present in this work the first fully federated system for the federated pre-training of large language models.
This work has been accepted at the [International Workshop on Federated Foundation Models In Conjunction with NeurIPS 2024 (FL@FM-NeurIPS'24)](https://federated-learning.org/fl@fm-neurips-2024/).
A follow up more detailed system paper has been released the 5th of November 2024; a short description can be found [here](https://relogu.github.io/publication/2024-11-05-photon-system-paper).

[Original technical report](https://arxiv.org/abs/2405.10853)

Abstract:

> Generative pre-trained large language models (LLMs) have demonstrated impressive performance over a wide range of tasks, thanks to the unprecedented amount of data they have been trained on. As established scaling laws indicate, LLMs' future performance improvement depends on the amount of computing and data sources they can leverage for pre-training. Federated learning (FL) has the potential to unleash the majority of the planet's data and computational resources, which are underutilized by the data-center-focused training methodology of current LLM practice. Our work presents a robust, flexible, reproducible FL approach that enables large-scale collaboration across institutions to train LLMs. We propose a scalable deployment system called Photon to enable the investigation and development of this new training paradigm for LLM pre-training. We show that Photon can be used by organizations interested in collaborating with their private data sources and computational resources for pre-training LLMs with billions of parameters. This paradigm would mobilize more computational and data resources while matching or potentially exceeding centralized performance. We further show the effectiveness of the federated training scales with model size and present our approach for training billion-scale federated LLMs using limited resources. Thus far, we have used Photon to train LLM models to the size of 7B parameters and anticipate larger models being completed in the near future. Finally, we show that LLM training is highly resilient to the classical challenges of federated statistical and hardware heterogeneity. Furthermore, we show that convergence is robust to partial participation, opening the avenue for compute-efficient collaborative training. Photon will help data-rich actors to become the protagonists of LLMs pre-training instead of leaving the stage to compute-rich actors alone.

Recommended citation: Lorenzo Sani, Alex Iacob, Zeyu Cao, Bill Marino, Yan Gao, Tomas Paulik, Wanru Zhao, William F. Shen, Preslav Aleksandrov, Xinchi Qiu, & Nicholas D. Lane. (2024). The Future of Large Language Model Pre-training is Federated.
