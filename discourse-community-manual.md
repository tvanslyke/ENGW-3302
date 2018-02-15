* [Getting Started in the Free and Open Source Software Community](## Getting Started in the Free and Open Source Software Community)
* [Who Cares About Open Source Software?](## Who Cares About Open Source Software?)
* [What Programmers Like to Talk About](## What Programmers Like to Talk About)
    * [Conventions](### Conventions)
    * [It's the Code, Stupid!](### It's the Code, Stupid!)
        * [Real Names Please](#### Real Names Please)
    * [C is the Lingua Franca of Programming](### C is the Lingua Franca of Programming)
    * [Your Definition of the Word "Hacker" Is Wrong](### Your Definition of the Word "Hacker" Is Wrong)
* [Some Vocabulary](## Some Vocabulary)
        * [Note: Java is to JavaScript as Car is to Carpet](#### Note: Java is to JavaScript as Car is to Carpet)
* [How Programmers Talk to One Another](## How Programmers Talk to One Another)
    * [The README](### The README)
        * [File Formats: Text, Markdown, ReStructured Text, and more](#### File Formats: Text, Markdown, ReStructured Text, and more)
* [Some Closing Remarks](## Some Closing Remarks)

## Getting Started in the Free and Open Source Software Community
Free and Open Source Software (FOSS) refers to software ... 

Throughout this text, you may find that I use some non-FOSS-specific terms to describe conventions or ideas in the FOSS community without specifying them as such.  For example, if a generalization is made about programmers in the FOSS community, it may read something like: "Programmers will typically do thing X while trying to achieve goal Y".  Please understand that such unqualified generalizations are implicitly FOSS-specific, so the previous text would read: "Programmers in the FOSS comunity ...".  Discussions about the greater programming community as a whole will be explicitly qualified to be so.

## Who Cares About Open Source Software?

Nowadays, entities like [Intel](https://github.com/intel), [Google](https://github.com/google), and even [Microsoft](https://github.com/Microsoft) maintain and contribute to open-source software projects.  Intel and Google, in particular, contribute heavily to what is widely considered to be *the* quintessential open-source project, the [Linux Kernel](https://en.wikipedia.org/wiki/Linux_kernel).  Even if you, the reader, are not interested in Free (as in freedom) and Open Source Software (FOSS), employers certainly are.

An excellent essay on the culture(s) of FOSS communities, [*The Cathedral and the Bazaar*](http://www.catb.org/esr/writings/cathedral-bazaar/), was written in back in the 90's by Eric S. Raymond.  It is worth a read if you want to know more about how different FOSS projects operate; particularly the Linux Kernel.  This essay is worth mentioning because it discusses the highly open and dynamic development model of the Linux Kernel, which has since been a model for many other open source projects.  


## What Programmers Like to Talk About
If you want to start participating It's important to undestand, while talking

### Conventions 
Talk about "quotation marks".

### It's the Code, Stupid!
The most important thing to understand about (most) FOSS projects and communities, is that it's the *code* that counts.  You could be the smartest guy in the room but if your code is no good, nobody is going to really care.  Personal matters are not really discussed at all.  In fact, it is not unheard of for anonymous individuals to submit minor patches to large FOSS projects.  

#### Real Names Please
While we're on the topic of anonymity, just note that real names are quite strongly preferred to pseudonyms (like an account names).  This mostly applies to contributors; bug reports can typically come from anybody under any name.  One notable exception to this rule is Bitcoin, whose [reference implementation](https://github.com/bitcoin/bitcoin) was originally written by an individual (or group of individuals) under the pseudonym [Satoshi Nakamoto](https://en.wikipedia.org/wiki/Satoshi_Nakamoto).

### C is the Lingua Franca of Programming
Though nowadays this has shifted towards Python a bit, partucularly for pseudocode, the C programming language is something every sofware developer is expected to have at least a cursory understanding of.  Although a beginner won't be expected to know much outside of their first language, at some point it *will* be expected that they have the ability to look at a chunk of C code and be able to vaguely reason about what is going on.

### Your Definition of the Word "Hacker" Is Wrong
The word "hacker" gets thrown around a lot nowadays by the media; the term has become so commonplace in the English-speaking world that that one can expect just about anybody to know what you mean when you use the word.  Unfornately, what you think about when you hear the word "hacker" is a bastardization of the term's original meaning.  Here is the definition of "hacker" according to the Jargon File:

> A person who enjoys exploring the details of programmable systems and how to stretch their capabilities, as opposed to most users, who prefer to learn only the minimum necessary. RFC1392, the Internet Users' Glossary, usefully amplifies this as: A person who delights in having an intimate understanding of the internal workings of a system, computers and computer networks in particular.

This is the term's original meaning as defined by the hacker community.  At some point along the way, the meaning of "hacker" has been mutated and reformed to refer to an individual who breaks computer system security.  The preferred terms for this definition are [*security hacker* or *cracker*](https://en.wikipedia.org/wiki/Security_hacker).

Thus, within the larger programming community, the terms "hacker", "hacking", or similar, should be taken to mean their *true* definitions, unless context implies that their adopted meanings are being used.


## Some Vocabulary
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
* Compiler - A tool which turns source code into executable machine code.
* Interpreter - A tool which executes a program in source code format.
* Regression - A change to a piece of software that results in the introduction of a bug.
* Pessimization - A play on the word "optimization" - a pessimization makes code slower to execute while an optimization makes it faster.

A useful resource for exploring more terms like these is the [Jargon File](http://catb.org/jargon/html/).


#### Note: Java is to JavaScript as Car is to Carpet
This is a very common confusion amongst the uninformed.  Java and Javascript are similar only nominally.  The above title is frequently regurgitated by those "in the know" to demonstrate this fact.

## How Programmers Talk to One Another

### The README

#### File Formats: Text, Markdown, ReStructured Text, and more
READMEs will typically come in one of three formats: Text (.txt), Markdown (.md), and ReStructured Text.

Historically, the text file was the most common file format for the README.  

Talk about markdown being used by reddit


## Some Closing Remarks



