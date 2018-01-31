# A Note to the Reader
If you're reading this, you probably know that this is still a draft.  Please understand that the structure of this document is still very much a work in progress.  Sections are still being added and shifted around quite whimsically.  

Also, the tone here is intentionally quite informal.  A lot (but not all) of these sections are written as though they are answers to imagined questions - the kind I may have wanted answers to when I was first learning about programming and software development.  It may be best to ort of like what you might see on [Stack Overflow](https://stackoverflow.com/), if you're familiar with that community.  I have a tendancy to get very explain-y, so it seems like a goo

Also, chances are that I have yet to proofread any part of this.  Don't judge my errors too harshly. :)

# Open Source Software
Nowadays, entities like [Intel](https://github.com/intel), [Google](https://github.com/google), and even [Microsoft](https://github.com/Microsoft) maintain and contribute to open-source software projects.  Intel and Google, in particular, contribute heavily to what is widely considered to be *the* quintessential open-source project, the [Linux Kernel](https://en.wikipedia.org/wiki/Linux_kernel).  Even if you, the reader, are not interested in Free (as in freedom) and Open Source Software (FOSS), employers certainly are.

An excellent essay on the culture(s) of FOSS communities, [*The Cathedral and the Bazaar*](http://www.catb.org/esr/writings/cathedral-bazaar/), was written in back in the 90's by Eric S. Raymond.  It is worth a read if you want to know more about how different FOSS projects operate; particularly the Linux Kernel.  This essay is worth mentioning because it discusses the highly open and dynamic development model of the Linux Kernel, which has since been a model for many other open source projects.  

## It's the Code, Stupid!
The most important thing to understand about (most) FOSS projects and communities, is that it's the *code* that counts.  You could be the smartest guy in the room but if your code is no good, nobody is going to really care.  Personal matters are not really discussed at all.  In fact, it is not unheard of for anonymous individuals to submit minor patches to large FOSS projects.  

### Real Names Please
While we're on the topic of anonymity, just note that real names are quite strongly preferred to pseudonyms (like an account names).  This mostly applies to contributors; bug reports can typically come from anybody under any name.  One notable exception to this rule is Bitcoin, whose [reference implementation](https://github.com/bitcoin/bitcoin) was originally written by an individual (or group of individuals) under the pseudonym [Satoshi Nakamoto](https://en.wikipedia.org/wiki/Satoshi_Nakamoto).

## C is the Lingua Franca of Programming
Though nowadays this has shifted towards Python a bit, partucularly for pseudocode, the C programming language is something every sofware developer is expected to have at least a cursory understanding of.  Although a beginner won't be expected to know much outside of their first language, at some point it *will* be expected that they have the ability to look at a chunk of C code and be able to vaguely reason about what is going on.

# Some Vocabulary
Listed here are several common terms you might see in discussions among programmers:

* svn (Subversion), git, cvs, hg (Mercurial) ... - Version control systems.
* The Right Thing (TM) - A somewhat sardonic way of referring to a what one might consider the correct algorithm, data structure, or whatever.  Its literal meaning is highly contextual.
* K&R C - [*The C Programming Language*](https://en.wikipedia.org/wiki/The_C_Programming_Language); both a book and a (quite old) dialect of C.  K&R = Kernighan and Ritchie, the book's authors.
* Metal/Bare Metal - Low level stuff.  Code or programming languages that are "near the metal" are low-level and less abstract.
* Release - A version of a piece of software which is considered "finished".  A release is usually associated with a version number, like `gcc-7.2`.  Releases are (usually) immutable; frozen in time.
* Commit - In reference to version control systems, a commit is a change to source code which has been added to the main version.  Changes can exist before being committed, but such changes are not yet official.
* Interface - The means with which a software component can be interacted with.  An interface is just a description of "what it does" and "how to use it", without the "how it works" part.
* Implementation - An implementation, in software, is the "how it works" part of an *interface* (defined above).  More correctly, it is not a part of the interface, but instead it is the set of inner workings that are accessible via the corresponding interface.  A keyboard is an interface to a computer, but the computer (plus operating system and associated firmware/software) does the actual work.
* OS - Operating system.
* Debian, Ubuntu, Manjaro, ... - Linux distributions.
* emacs, vi, nano, pico, ... - Text editors.
* C, C++, C#, Objective C, Java, Python, Lisp, Ruby, JavaScript, PHP, ... - Programming languages.
* Turing Complete - A computational system is turing complete if it can, in theory, be used to compute anything that a computer can.  Turing completeness is a category; all programming languages are Turing complete (though a turing complete system need not be a linguistic construct).
* Compiler - A tool which turns source code into machine code.
* Interpreter - A tool which executes a program in source code format.
* Regression - A change to a piece of software that results in the introduction of a bug.
* Pessimization - A play on the word "optimization" - a pessimization makes code slower to execute while an optimization makes it faster.

A useful resource for exploring more terms like these is the [Jargon File](http://catb.org/jargon/html/).

# Different Jobs Need Different Tools
There is no "best" programming language.  Different languages have different use cases and some are better than others at different jobs.  For example, say you have a text file like this:

```
Seinfeld  Jerry  64
Burr      Bill   49
Carlin    George 80
     ...
```

And you wanted to see all of the lines that where the third column has a number that is less than 60.  Most programmers would write a program to do this.  To demonstrate that some languages might do the job better than others, here's a Python program that does the task:

python```
from sys import stdin
for line in stdin:
	third_col = int(line.strip().split()[2])
	if third_col < 60:
		print(line)
```

The same thing in AWK:
awk```
$3 < 60
```
AWK is clearly the better tool for the job; even if it is less popular than Python, in general.

At the same time, you'll never find an operating system written in either Python or AWK.  They're the wrong tools for the job.  That kind of task is reserved for *Systems Programming Languages* like C, C++, or Rust.

#### Note: Java is to JavaScript as Car is to Carpet
This is a very common confusion amongst the uninformed.  Java and Javascript are similar only nominally.  The above title is frequently regurgitated by those "in the know" to demonstrate this fact.

# More Sections Here


# Some Closing Remarks



