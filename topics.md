# Compiler Internals/Implementation Improvements & New Techniques for Conventional Optimizations
## Internals, IR, and Domain-Specific Languages
* LaminarIR: Compile-Time Queues for Structured Streams 
* Improving Compiler Scalability: Optimizing Large Programs at Small Price
## Dynamic Optimizations - JIT
* Surgical Precision Jit Comilers - https://www.cs.purdue.edu/homes/rompf/papers/rompf-pldi14.pdf
* Cache Locality Optimization for Recursive Programs - http://jlifflander.com/papers/pldi-recursive.pdf
    * Proposes a runtime solution to the problem of optimizing recursive or call-graph-hidden data accesses that may not be cache-optimal.




##  Misc
* A Framework for Enhancing Data Reuse via Associative Reordering - http://web.cse.ohio-state.edu/~pouchet.2/doc/pldi-article.14.pdf
* Cache Locality Optimization for Recursive Programs - http://jlifflander.com/papers/pldi-recursive.pdf
    * Proposes a runtime solution to the problem of optimizing recursive or call-graph-hidden data accesses that may not be cache-optimal.
    * Proposes solution involving automatic parallelization.

## Issues with Call Graphs - Recursion, Top-down vs Bottom-up
* Cache Locality Optimization for Recursive Programs - http://jlifflander.com/papers/pldi-recursive.pdf

LaminarIR: Compile-Time Queues for Structured Streams 
	- http://delivery.acm.org/10.1145/2740000/2737994/p121-ko.pdf?ip=129.10.9.26&id=2737994&acc=ACTIVE%20SERVICE&key=AA86BE8B6928DDC7%2EC2B8A117C7A71F5A%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1519233685_d494640d060f6230ad18b9adf3e3143b

Improving Compiler Scalability: Optimizing Large Programs at Small Price 
	- http://delivery.acm.org/10.1145/2740000/2737954/p143-mehta.pdf?ip=129.10.9.26&id=2737954&acc=ACTIVE%20SERVICE&key=AA86BE8B6928DDC7%2EC2B8A117C7A71F5A%2E4D4702B0C3E38B35%2E4D4702B0C3E38B35&__acm__=1519233866_d7f01c2e69727a2b32519e588a378b5d

Tracing Compilation by Abstract Interpretation 
	- https://www.microsoft.com/en-us/research/wp-content/uploads/2014/01/popl14.pdf

