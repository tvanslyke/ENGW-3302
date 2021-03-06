# Getting Started in the Free and Open-Source Software Community
Free and Open-Source Software (FOSS) refers to software for which the source code is made available to users (making it open-source), and for which users of the software are granted permission to modify and redistribute the software.  Some well-known examples of FOSS projects are Firefox, VLC Media Player, and the Linux Kernel.

The FOSS community refers to individuals who are involved in the development of different FOSS projects.  Though members of the FOSS community need not be programmers, they typically are and this document is targeted towards new programmers who are looking to get involved with the FOSS community, but are unsure of where or how to start.  This document will discuss terminology and conventional means of communication within the FOSS community as well as the programming community at large.

Throughout this text, you may find that I use some non-FOSS-specific terms to describe conventions or ideas in the FOSS community without specifying them as such.  For example, if a generalization is made about programmers in the FOSS community, it may read something like: "Programmers will typically do thing X while trying to achieve goal Y".  Please understand that such unqualified generalizations are implicitly FOSS-specific, so the previous text would read: "Programmers in the FOSS community ...".  Discussions about the greater programming community as a whole will be explicitly qualified to be so.

## Who Cares About Open-Source Software?

Nowadays, entities like [Intel](https://github.com/intel), [Google](https://github.com/google), and even [Microsoft](https://github.com/Microsoft) maintain and contribute to open-source software projects.  Intel and Google, in particular, contribute heavily to what is widely considered to be *the* quintessential open-source project, the [Linux Kernel](https://en.wikipedia.org/wiki/Linux_kernel).  Even if you, the reader, are not interested in Free (as in freedom) and Open-Source Software (FOSS), employers certainly are.

An excellent essay on the culture(s) of FOSS communities, [*The Cathedral and the Bazaar*](http://www.catb.org/esr/writings/cathedral-bazaar/), was written in back in the 90's by Eric S. Raymond.  It is worth a read if you want to know more about how different FOSS projects operate; particularly the Linux Kernel.  This essay is worth mentioning because it discusses the highly open and dynamic development model of the Linux Kernel, which has since been a model for many other open-source projects.  


# Programming Discourse
Here we'll walk through some quirks of in the way programmers write and talk as well as some expectations about how communication should occur.  Think of this section as a guide of "what to say" or "how to say it" in general.  Not every convention or best practice is covered here, but some common mistakes and confusions are pointed out so that a newcomer like yourself doesn't get *too* lost when trying to communicate with other programmers (getting a *little* lost is okay and is a rite of passage in the programming community).




## Conventions
Here are some general conventions to follow in the FOSS community.  These tidbits of information apply in most communication mediums.

### Real Names Please
When communicating with other developers in an open-source project, please note that real names are quite strongly preferred to pseudonyms (like an account names).  This mostly applies to contributors; bug reports can typically come from anybody under any name.  Nonetheless, if you want to be actively involved in a FOSS project, the best thing you can do is 

One notable exception to this rule is Bitcoin, whose [reference implementation](https://github.com/bitcoin/bitcoin) was originally written by an individual (or group of individuals) under the pseudonym [Satoshi Nakamoto](https://en.wikipedia.org/wiki/Satoshi_Nakamoto).

### C is the Lingua Franca of Programming
Though nowadays this has shifted towards Python a bit, particularly for pseudocode, the C programming language is something every software developer is expected to have at least a cursory understanding of.  Although a beginner won't be expected to know much outside of their first language, at some point it *will* be expected that they have the ability to look at a chunk of C code and be able to vaguely reason about what is going on.  C is also the language of choice for many open source projects like CPython and the Linux Kernel.  Complete ignorance of C will keep many communication barriers erected for those trying to get involved in many big-name FOSS projects.

### Your Definition of the Word "Hacker" Is Wrong
The word "hacker" gets thrown around a lot nowadays by the media; the term has become so commonplace in the English-speaking world that that one can expect just about anybody to know what you mean when you use the word.  Unfortunately, what you think about when you hear the word "hacker" is a bastardization of the term's original meaning.  Here is the definition of "hacker" according to the Jargon File:

> A person who enjoys exploring the details of programmable systems and how to stretch their capabilities, as opposed to most users, who prefer to learn only the minimum necessary. RFC1392, the Internet Users' Glossary, usefully amplifies this as: A person who delights in having an intimate understanding of the internal workings of a system, computers and computer networks in particular.

This is the term's original meaning as defined by the hacker community.  At some point along the way, the meaning of "hacker" has been mutated and reformed to refer to an individual who breaks computer system security.  The preferred terms for this definition are [*security hacker* or *cracker*](https://en.wikipedia.org/wiki/Security_hacker).

Thus, within the larger programming community, the terms "hacker", "hacking", or similar, should be taken to mean their *true* definitions, unless context implies that their adopted meanings are being used.

## Some Vocabulary
Shown here is a non-exhaustive list of several common terms you might see in discussions among programmers, in no particular order:

* C, C++, C#, Objective C, Java, Python, Lisp, Ruby, JavaScript, PHP, ... - Programming languages.
* OS - Operating system.
* Debian, Ubuntu, Manjaro, ... - Linux distributions.
* emacs, vi, nano, pico, ... - Text editors.
* Release - A version of a piece of software which is considered "finished".  A release is usually associated with a version number, like `gcc-7.2`.  Releases are (usually) immutable; frozen in time.
* Commit - In reference to version control systems, a commit is a change to source code which has been added to the main version.  Changes can exist before being committed, but such changes are not yet official.
* svn (Subversion), git, cvs, hg (Mercurial) ... - Version control systems.
* The Right Thing (TM) - A somewhat sardonic way of referring to a what one might consider the correct choice of algorithm, data structure, or anything really.  Its literal meaning is highly contextual, but it is almost always in reference to a design choice.
* K&R C - [*The C Programming Language*](https://en.wikipedia.org/wiki/The_C_Programming_Language); both a book and a (quite old) dialect of C.  K&R = Kernighan and Ritchie, the book's authors.
* Metal/Bare Metal - Low level stuff.  Code or programming languages that are "near the metal" are low-level and less abstract.
* Interface - The means with which a software component can be interacted with.  An interface is just a description of "what it does" and "how to use it", without the "how it works" part.
* Implementation - An implementation, in software, is the "how it works" part of an *interface* (defined above).  More correctly, it is not a part of the interface, but instead it is the set of inner workings that are accessible via the corresponding interface.  A keyboard is an interface to a computer, but the computer (plus operating system and associated firmware/software) does the actual work.
* Turing Complete - A computational system is Turing complete if it can, in theory, be used to compute anything that a computer can.  Turing completeness is a category; all programming languages are Turing complete (though a Turing complete system need not be a linguistic construct).
* Compiler - A tool which turns source code into executable machine code.
* Interpreter - A tool which executes a program in source code format.
* Regression - A change to a piece of software that results in the introduction of a bug.
* Pessimization - A play on the word "optimization" - a pessimization makes code slower to execute while an optimization makes it faster.

A useful resource for exploring more terms like these is the [Jargon File](http://catb.org/jargon/html/).


# How Programmers Talk to One Another
Here we'll discuss some of the formats that programmers use to communicate with each other.

## The README
All software projects should have an associated README file.  The README file tells users and other developers the basics of how to obtain and use the associated software and code.  

### What's in a README?
If you're looking to write a README for one of your software projects and are unsure of where to start, the best thing you can do is go have a look at other open-source projects **for the language you're using** and use them as guidelines for your own. For example, CPython, the [reference implementation](https://en.wikipedia.org/wiki/Reference_implementation) for the Python programming language, written in C, has a [README](https://github.com/python/cpython/) with sections that tell you things like:
1. How to build and install the software.
2. How to use the software.
3. How to contribute to the project.
4. How to run the test suite.
5. Where to report bugs.

and so on.  CPython is in an interesting position of being a project that is written in one programming language, C, while simultaneously implementing another, Python.  So in that project, you'll find a mixture of conventions from both the C community and the Python community.  

The most common elements of a README, regardless of the languages used in the associated project are:
1. An introduction. 
	1. What is this project?  What problem does it solve and who might want to use it?
2. Installation Guide
    1. How do I install this software?
        1. Projects written in compiled languages (C, C++, Rust, ...) typically use a [build system](https://en.wikipedia.org/wiki/Build_automation) (e.g. CMake, GNU Autotools, Bazel, ...).  Pick one and demonstrate how to use it to install your project in your README.
        2. Dynamic languages, like Python, tend to use [package managers](https://en.wikipedia.org/wiki/Package_manager) (like [PIP](https://en.wikipedia.org/wiki/Pip_(package_manager))) that you can distribute your software with.
3. Tutorials and Documentation
    1. How do I use this software?
        1. Show examples of how to use your project.  If it's a library, show code examples.  If it's a standalone application, show some common use cases.  Include pictures if there's a GUI component.
    2. Documentation 
        1. Documentation should be provided that explains what your code does and how others might use your code in their own projects, even if that wasn't your intention.
        2. Again, follow the conventions of your language.  The Python guys like to use [Sphinx](http://www.sphinx-doc.org/en/master/) for documentation, Java uses [JavaDoc](https://en.wikipedia.org/wiki/Javadoc), and C++ projects may use [Doxygen](https://en.wikipedia.org/wiki/Doxygen).
4. Contributing and Bug Reports
	1. Though not strictly required, it's good form to provide a method for others to contribute and report bugs in your README.


### File Formats: Text, Markdown, ReStructured Text, and more
READMEs will typically come in one of three formats: Text (.txt), [Markdown](https://en.wikipedia.org/wiki/Markdown) (.md), and [ReStructured Text](https://en.wikipedia.org/wiki/ReStructuredText).  These formats are preferred because they are *simple*; you should be able to open and comfortably view a README file in a simple text editor (e.g. Notepad on Windows).  Programmers, in general, like to be able to read and edit files without having to start up a bulky application like, for instance, MS Word.  A good rule of thumb is that if you're writing a README, another programmer should be able to read it in their terminal.

Text files are rather self-explanatory, but how about Markdown and ReStructured Text?  Both of these are minimalist [markup languages](https://en.wikipedia.org/wiki/Lightweight_markup_language).  Both are human-readable files containing text that can be processed to generate a more pleasant-looking document.  This manual is written in Markdown and if you're reading this on Github, then you can see what the unprocessed file looks like by navigating to the top of the page and clicking on the 'Raw' button.  You'll find that, while not exactly pretty, the file is perfectly readable as-is.  

## The Mailing List 
Mailing lists are a very common communication medium for FOSS projects.  For example, the [Linux Kernel Mailing List](https://lkml.org/) is the primary method for communicating with Linux kernel developers about Linux kernel development.  LLVM has its own mailing list as well, [cfe-commits](https://reviews.llvm.org/p/cfe-commits/).  

Mailing lists are typically used by FOSS developers to communicate changes, proposals, and announcements within their respective projects.  Discourse in this medium is almost always informal but highly technical.  For an example of this mixture, see the conversation on LKML linked [here (** WARNING STRONG LANGUAGE **)](https://lkml.org/lkml/2014/7/24/584).  In that email, Linus Torvalds, who is known for his usage of strong language, angrily attacks GCC (a very popular open-source C compiler) while simultaneously speaking about topics such as register spilling, stack redzoning, and the x86_64 ABI.

When communicating in a mailing list:
* Don't be overly formal, but do try to be polite.
* Stay on topic.  If you're in an email chain about a proposed patch, talk about the patch and the systems it affects.
* Keep it short.  Only say what needs to be said; if somebody else already said what you were thinking, then you don't need to add anything.

## Academic Writing and Code Documentation
Though less common in the FOSS community specifically, academic and other formal writing formats *do* come up every now and then.  For an example of a formal document written by a member of the FOSS community see Ulrich Drepper's [What Every Programmer Should Know About Memory](https://people.freebsd.org/~lstewart/articles/cpumemory.pdf).  The document details, with perhaps a *bit* too much depth, both how computer memory works and, more importantly, how it affects the speed of software applications.

Documents like this, almost invariably, are written in a very dense markup language called [LaTeX](https://en.wikipedia.org/wiki/LaTeX).  LaTeX, or sometimes just TeX, is used in STEM fields for academic publications and is known for its extremely pristine typesetting engine.  LaTeX is preferred over more conventional alternatives, like MS Word, because it is able to produce documents that tend to be "easier on the eyes" and that look more professional than [WYSIWYG word processors](https://en.wikipedia.org/wiki/WYSIWYG).  While this may largely be a subjective matter, consider that LaTeX is designed for typography while word processors tend to be designed to be easy to use, even for amateurs.

The writing style in academic computer science literature is not unlike that of mathematics or physics.  It can be very dense at times and it will often involve quite a bit of math.  Perhaps the only component unique to formal writing in the world of programming is the usage of *pseudocode*.  Pseudocode is a programming language-agnostic, code-like representation of an algorithm.  It is used to describe how an algorithm works as a supplement to a more formal, mathematical description.  For example, what follows is a pseudocode representation of a recursive Fibonacci function:
```
function fibonacci(input n) is 
	if n is 0 or 1 then 
		return 1
	else 
		return fibonacci(n - 1) + fibonacci(n - 2)
```
This representation of the algorithm relies primarily on plain English.  Pseudocode is intended to be clear, concise, and most importantly, readable.  Keep in mind your audience when you're writing pseudocode.  C, C++, C#, or Java programmers would likely prefer pseudocode that looks like more like C while Python or Ruby programmers would prefer a more Python-like syntax.  There are no hard and fast rules to writing pseudocode, just rules of thumb and a reliance on common sense.

# Getting Involved in Open-Source Software Projects
If you would like to get involved in any FOSS projects, the best thing you can do is find a project you're interested in and start playing with the code!  For example, if you enjoy programming in both C and Python, perhaps you might also enjoy writing CPython extensions in C.  Once you get the hang of the project's conventions and design, take a look at the project's README to see how you can get started with contributing.  Beyond that, there's not much advice to be given.  

Some projects are notorious for having very hard-to-understand code, like GCC, while others, like CPython, are known for exactly the opposite.  Some projects have only a few core developers while others have hundreds or thousands.  If you want to get involved, just give it your best shot on something you're interested in.  

Once you've found a project that you're interested in, a few small tips are:
* Be sure to read the documentation and learn the conventions of the project.
* Test your code before submitting!  Nobody likes it when contributions lead to bugs.
* Start small!  Completely rewriting an entire portion of the codebase, even if it's an improvement, probably won't be well received.  After all, now *only you* understand how that component works.
* Lastly, be polite and agreeable.  If the project's maintainers ask you to make a modification to your patch, they probably have a good reason.  Arguing with them is a good way to get your patch rejected.  If they're asking you to make changes, they obviously think your patch is worthwhile!  Otherwise they would've just outright rejected it.

Of course, the most important part is that you get involved at all.  Programmers are always happy when somebody is interested in their project.  Why else would we bother?  Get out there, use our code and, when you're ready, let us use yours too!
