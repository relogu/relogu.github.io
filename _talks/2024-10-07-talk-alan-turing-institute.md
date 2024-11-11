---
title: "Federating Large Language Models from Scratch @ Alan Turing Institute"
collection: talks
type: "Talk"
permalink: /talks/2024-10-07-talk-alan-turing-institute
venue: Alan Turing Institute, London
date: 2024-10-07
location: "London, UK"
---

The [Research Engineering Team](https://www.turing.ac.uk/research-engineering) at the [Alan Turing Institute](https://www.turing.ac.uk/) invited me to present our work on federated learning of large language models.
This talk was inserted in the seminar series titled ["Robots in Disguise"](https://github.com/alan-turing-institute/robots-in-disguise).
I presented our work on federated learning of large language models, in particular, how we can train large language models from scratch in a federated manner.
A wider introduction to federate learning and its main challenges was also presented.

Talk abstract:

>Large language models (LLMs) offer unprecedented ML capabilities and continue to improve rapidly. As a result, various organizations are locked in a race to scale LLMs and explore their limits and weaknesses. We believe federated learning (FL) offers an untapped potential to dramatically increase the supply of data sources for these models. Early work has shown, for example, how LLM pre-training can tap into edge device data leveraging FL. Others have shown the impact of using federated optimizers in a poorly connected distributed infrastructure of stateful workers to train a centralized LLM. We believe FL can reshape LLM practices and opportunities thanks to two of its most exciting features: relaxed synchronization requirements and privacy-by-design on users' data. The federated paradigm opens the doors of new interesting possibilities for the LLM community, like resource sharing, unbounded scaling on private data, democratization, and privacy. This talk contributes to the emerging field that blends the two worlds of FL and LLMs by presenting a fully federated approach for LLM pre-training from scratch. Our approach has shown to be viable at a scale of 3B parameters under a real working system.
