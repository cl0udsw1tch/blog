

<h1 style="text-align:center">Tensorial Formulation of Backpropagation</h1>

The matrix formulation of both feed-foward neural networks and convolutional neural networks (and other networks as well, for example, transformers) is inspired by the linear relationship between the parameters of the network. However, when the dimensions of the space the parameters live in begins to grow, and so do the relationships between parameters, matrices become an inappropriate tool to mathematically describe the model and a rather clumsy tool to describe the backpropogation algorithm, so here, tensors are chosen instead. 
## 1. Feed Forward Neural Networks
We will call a neural network a layered model that produces features of samples in a "linear" way, by using parameters and the sample features at previous layers and then applying a non-linear transform. Define the following:

* Dataset: $$\mathcal{D} = \{(x^i, v^i)\}_{i \in I} $$ for some index set $I$, where $x^i \in \mathbb{R}^n$ is a sample with $n$ features, and $v^i \in \mathbb{R}$ is its label
* $$(y_{l})^{i,j}$$: The $j$th feature of the $i$th sample produced at hidden layer $l-1$, feeding into hidden layer $l$. 

Suppose now we have $(y_{l-1})^{i,j}$ for every $j$ in some index set $\mathcal{V}_{l-1}$. We aim to produce [one of] the next features $(y_{l})^{i,k}$ for the same sample $i$; namely feature number $k \in \mathcal{V}_l$ not necessarily equal to $j$. The feed-forward neural network (FFN) achieves this in two steps:

___
**1**\. We take a set of **parameters** $\{(W_l)^{j,k} \in \mathbb{R}\}_{j \in \mathcal{V}_{l-1}}$ - we may also call these ***weights*** - and multiply each to the respective $j$th feature of the $i$th sample at layer $l-1$, before summing. That is, we produce 
$$
\begin{equation}
(z_l)^{i,k} = \sum_{j \in \mathcal{V}_{l-1}}(y_{l-1})^{i,j} (W_l)^{j,k} 
\end{equation}
$$ 
a "preimage" of the $k$th feature of the $i$th sample at layer $l$. Just the preimage thus far, since at step 2...

**2**\. a **smooth, nonlinear transform** from $C^{\infty}(\mathbb{R}, \mathbb{R})$ is henceforth applied:
$$
\begin{equation}
(y_l)^{i,k} = f_l((z_l)^{i,k})
\end{equation}
$$
producing the desired feature. 
___
<h3>Tensors</h3>

It is at this point we will specify important details need to understand the rest of the article. Firstly, we will use *Einstein's Summation Convention* (ESC) to simplify sums with a repeated index, signifying the summation of the terms over said index. For example, we can rewrite (1) as
$$
\begin{equation}
(z_l)^{i,k} = (y_{l-1})^{i,j} (W_l)^{j,k} 
\end{equation}
$$
where the sum is meant to be over $j$, which repeats, and where all terms are zero outside of their domains. This too deserves formalization. Firstly, let's consider $(y_l)$ as a well defined object, namely, a **tensor** over infinite dimensional vector spaces, but with *finite support*. Let's clarify, since $(y_l)$ will contain $\mathcal{V}_l$ features for $n$ samples, lets define
$$
\begin{equation}
y_l = \sum_{i,k} (y_l)^{i,k} e_i \otimes e_k \in \mathbb{R}^{\mathbb{Z}} \otimes \mathbb{R}^{\mathbb{Z}} 
\end{equation}
$$
where $(y_l)^{i,k}$ is as previously defined when $i \in \{1...n\}, k\in \mathcal{V}_l$ and $0$ elsewise. Also, $\{e_z\}_{z\in\mathbb{Z}}$ will always be the canonical orthornormal basis for $\mathbb{R}^{\mathbb{Z}}$. This redefinition of $y_l$ allows us to conviniently leave out bounds in the summation to imply summing over the entirety of $\mathbb{Z}$ for each index, something that will be exploited for all tensors in this article, which will also have finite support. 

We will also make use of *Abstract Index Notation* (AIN), which is particularly useful when representing the *shape* of a tensor. For example, we could write $(y_l)^{ab}$ to denote that $y_l \in V \otimes V$ for some vector space $V$, or for a more general example
$$
T^{ab}{}_{c}{}^{d}{}_{e}
$$
to denote a tensor $T \in V \otimes V \otimes V^* \otimes V \otimes V^*$

$W_l = \sum_{j,k} (W_l)^{j,k} e_j \otimes e_k$ in this formalization, and we proceed from the tensorized version of (1) 
$$
\begin{align}
(z_l)^{i,k} e_i \otimes e_k &=  (y_{l-1})^{i,j} (W_l)^{j,k} e_i \otimes e_k \\ 
\implies z_l &= \sum_{i,j,k} (y_{l-1})^{i,j} (W_l)^{j,k} e_i \otimes e_k
\end{align}
$$
where we remind the reader the index $j$ can be left out of the above sum when (6) is written using ESC.

We also need to transform the $C^{\infty}(\mathbb{R}, \mathbb{R})$ transform into one that acts on tensors, that is one from $C^{\infty}(\mathbb{R}^{\mathbb{Z}} \otimes \mathbb{R}^{\mathbb{Z}},\mathbb{R}^{\mathbb{Z}} \otimes \mathbb{R}^{\mathbb{Z}})$ by defining
$$
\begin{equation}
y_l = F_l(z_l) = \sum_{i,k} f_l((z_l)^{i,k}) e_i \otimes e_k
\end{equation}
$$

___
<h3>The Model </h3>

We now formalize the FNN model $\mathcal{F}$ completely. 
<ul style="list-style: disc">
<li>
First we start with the input layer, $L_0$, which is merely the dataset $\{x_i \in \mathcal{D}\}$
</li>

</ul>
We can now formulate the backpropogation algorithm.
___

<h3>Backpropogation</h3>





END






