# Deep Learning by Ian Goodfellow
## Chapter 1 - Introduction

**QA: What is computational graphs?**

A computational graph is a directed graph where the nodes correspond to **operations** or **variables**. **Variables** can feed their value into **operations**, and **operations** can feed their **output** into other **operations**. This way, every node in the graph defines a function of the variables.

The values that are fed into the nodes and come out of the nodes are called **tensors**.

**Sub - QA**: Diff between scalar, Vector, Matrix and Tensor?

![matrix](/home/nullbyte/Pictures/Matrix1.jpeg)

$$ \text{Let’s look at an example. The following computational graph computes the sum z of two inputs x and y. Here, x and y are input nodes to z and z is a consumer of x and y. z therefore defines a function} z : \mathbb{R^2} \rightarrow \mathbb{R}. $$

![matrix](/home/nullbyte/Pictures/cg1.png)