---
title: "The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators"
collection: publications
permalink: /publication/2026-06-24-red-queen-godel-machine
excerpt: 'A self-improving system in which agents and the evaluators that score them co-evolve, avoiding the reward hacking that fixed evaluators invite.'
date: 2026-06-24
venue: "Preprint"
paperurl: 'https://arxiv.org/abs/2606.26294'
citation: 'Alex Iacob, Andrej Jovanović, William F. Shen, Daniel Burkhardt, Meghdad Kurmanji, Nurbek Tastan, Lorenzo Sani, Niccolò Alberto Elia Venanzi, Ambroise Odonnat, Zeyu Cao, Bill Marino, Xinchi Qiu, Nicholas D. Lane (2026). The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators. arXiv:2606.26294.'
---
A self-improving system in which agents and the evaluators that score them co-evolve, avoiding the reward hacking that fixed evaluators invite.

[Read the paper here.](https://arxiv.org/abs/2606.26294)

Abstract:

> Self-improving agents are state-of-the-art (SOTA) on agentic coding benchmarks and have recently been extended to general domains. However, their search methods generally assume a stationary evaluation criterion: a fixed verifier, benchmark, or labeled dataset that remains valid as the agent improves. This ignores a central feature of evolution: species adapt as their environments change with them. We aim to bring the same principle to recursive self-improvement, making evaluation part of the improvement loop and opening search to evolving evaluators, adversarial objectives, and dynamic utilities that may surpass static benchmarks. We introduce the Red Queen Godel Machine (RQGM), an evolutionary framework for recursive self-improvement under non-stationary utilities. The RQGM makes this possible through controlled utility evolution: search is organized into epochs with a fixed within-epoch evaluation criterion, while the utility can be updated at epoch boundaries, so self-improvement guarantees hold per epoch as the objective evolves across them. We begin by showing that even on verifiable coding tasks, the RQGM improves test pass rate over the prior SOTA by adding a complementary agent-as-a-judge code-review signal. This signal is cheaper and the RQGM uses 1.35x-1.72x fewer tokens. We then turn to scientific paper writing and reviewing, and Olympiad-level proof writing and grading, where the RQGM improves performance over prior self-improving agents: co-evolved writers reach 1.78x-1.86x higher acceptance rates under a diverse agent-as-a-judge panel, while co-evolved graders reach 9% higher ground-truth accuracy. In paper reviewing, the strongest baseline reviewer over-accepts AI-generated papers at up to 1.91x the human rate. The RQGM corrects this by introducing an adversarial objective that discovers reviewers equally stringent on AI and human work.

Recommended citation: Alex Iacob, Andrej Jovanović, William F. Shen, Daniel Burkhardt, Meghdad Kurmanji, Nurbek Tastan, Lorenzo Sani, Niccolò Alberto Elia Venanzi, Ambroise Odonnat, Zeyu Cao, Bill Marino, Xinchi Qiu, Nicholas D. Lane (2026). The Red Queen Gödel Machine: Co-Evolving Agents and Their Evaluators. arXiv:2606.26294.
