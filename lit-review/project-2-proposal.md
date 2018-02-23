## Background
Optimizing compilers have been around for a long time and they are vital to the process of creating fast and efficient software without loss of abstraction.  Systems programmers have come to rely on compilers such as GCC, Clang, ICC, and MSVC to produce reasonable assembly when given reasonable code.  Often, one will write code in a specific way because they know of an optimization technique that their compiler can leverage.  Nowadays, this is less necessary because optimizers have gotten particularly good at optimizing specific constructs, such as loop unrolling.  However, with modern software being strongly dependent on CPU cache efficiency, branch prediction, and other non-intuitive hardware optimizations, optimizing compilers have a more difficult job than they did back when most machines more closely modelled the classical von Neumann architecture.

# Rationale
This literature review will introduce classical compiler optimizations as background information and then go on to discuss the modern state-of-the-art in production compilers such as GCC, Clang, ICC, and MSVC.  From there, pioneering research will be explored.  It is expected that much of this research will involve [distributed systems](https://arxiv.org/pdf/1711.07606.pdf) and [concurrent programming](https://arxiv.org/pdf/1211.4101.pdf), as these areas are more common in high-throughput systems and are generally more difficult to optimize.  For example the machine learning-oriented dataflow library, TensorFlow, is largely designed to burn through as much data and as quickly as possible.  While not what one might consider to be a compiler, TensorFlow deals with nearly every problem that an optimizing compiler would, with the additional overhead of having to support distributed workloads.  For this reason, we can see that new compiler-like systems are emerging in non-traditional fields and application domains.



## Resources
Listed here are promising resources for ongoing research in optimizing compilers
* ArXiv 
	* https://arxiv.org/pdf/1711.07606.pdf
	* https://arxiv.org/pdf/1211.4101.pdf
	* https://arxiv.org/pdf/1612.06668
* Programming Languages Design and Implementation (PLDI) Conferences:
	* https://conf.researchr.org/home/pldi-2016
* Principles of Programming Languages (POPL) Symposium:
	* http://sigplan.org/OpenTOC/popl17.html (3 papers specifically on compiler optimizations)

## Potential Issues
One particular concern with this topic is the idea that optimizing compilers are a "solved problem".  They're not, but they have had a *tremendous* amount of brainpower poured into them.  The GNU C Compiler (GCC) has been around since 1987 and has been aggressively improving its optimization capabilities since that time.  All of the "low-hanging fruit" optimizations that compilers attempt to utilize have already been discovered, and most compilation systems that have been around for long enough already implement them.

This area of research is at the intersection of computability theory and software engineering.  Theory can give us some important and usable results, but this problem domain is dictate largely by practicallity.  For this reason, it may be difficult to find research papers that relate directly to programming language compilers.
