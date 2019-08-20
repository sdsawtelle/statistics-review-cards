# statistics-review-cards

This is a set of PDF review cards (with the generating LaTex) for reviewing important basic concepts in probability and statistics. The content is based off of a series of lecture notes by Dr. Joe Chang (Yale) for an introductory course I took. The content is also heavily augmented by discussions with Dr. David Brinda (Yale), especially the "decision theoretic framework for data analysis" perspective. 

Each card begins by listing a series of questions (either related to explaining or proving a concept, or a toy problem utilizing a concept), then the body of the card contains the "solutions" to these questions. *For maximum effectiveness when you are reviewing, you should give your best effort to fully answering a question before you look at the "solution".*

The review cards are written in LaTex, where the file for each card references the general preamble file [concepts_pre.tex](concepts_pre.tex). Also included is a short python script [latex_cleanup.py](latex_cleanup.py) for cleaning up all the auxilliary files created by LaTex during the typesetting process. The [Images](Images) folder contains the included graphics and a powerpoint file that I used for some basic figure editing.

Below is a preview of what each review card contains, listed in the order that it makes sense to review them.

1. [counting-problems](/Cards/counting-problems/counting-problems.pdf)
This card reviews the fundamental principle of counting, and permutations and combinations. It provides a general framework for counting problems where a set of n objects can be
assigned to k roles, and either the roles or objects, or both or neither, are indistinguishable. It introduces the "stars and bars" approach to visualizing problems concerning combinatorics with subsets.

2. [conditional-probability](/Cards/conditional-probability/conditional-probability.pdf)
This card defines conditional probability and disjointness and independence. It discusses how to calculate the probability of a union or intersection of outcomes. It describes how to transform calculations of probability by partitioning the sample space in a useful way.

3. [decision-theoretic-framework-of-analysis](/Cards/decision-theoretic-framework-of-analysis/decision-theoretic-framework-of-analysis.pdf)
This card lays out a general logical framework for statistical data analysis. This framework is an abstract schema that fits many, many specific techniques and terms in statistical inference. The card discusses the definition of loss function, risk, risk curve, and decision rules. It introduces the following common topics in terms of the framework: estimators (density estimation and function estimation), bias/variance decomposition of estimators, bayesian analyses.

4.[estimation](/Cards/estimation/estimation.pdf)
Reviews definition of estimators from the DTFoA context. Defines the likelihood function and maximum likelihood estimators with some examples. Introduces linear regression and logistic regression.

5. [bayesian-data-analysis](/Cards/bayesian-data-analysis/bayesian-data-analysis.pdf)
This card builds from the conditional-probability card and the decision-theoretic-framework-of-analysis card by applying conditional probability to data analysis. It cover the general framework of Bayesian analysis and how it is commonly employed in practice.

6. [random-variables-and-LLN](/Cards/random-variables-and-LLN/random-variables-and-LLN.pdf)
This card dives deeper into statistics by discussing random vectors and joint, conditional and marginal distributions. It defines mean, variance and conditional expectation which are important metrics on a distribution. It discusses the very important example of mean and variance of the sample mean of data. It gives the Law of Large Numbers regarding sample means and discusses the Markov Inequality by way of proof of the LLN. 

7.[common-distributions-and-CLT](/Cards/common-distributions-and-CLT/common-distributions-and-CLT.pdf)
This card follows up an understanding of distributions, mean and variance by outlining a few of the most common or important distributions - binomial, geometric, cauchy, normal. The Central Limit Theorem is discussed here.

8. [markov-chain-and-MCMC](/Cards/markov-chain-and-MCMC/markov-chain-and-MCMC.pdf)
This card defines markov chains and gives a discussion of the associated ideas of limiting distribution, stationary distribution and irreducibility. It gives the ergodic theorem for markov chains. It then describes the Metropolis Hastings algorithm for simulating a draw from a distribution with an unknown normalization.