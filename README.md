# Code: A Public Scratchspace

[![Build Status](https://travis-ci.com/mrajweir/Code.svg?branch=master)](https://travis-ci.com/mrajweir/Code)

This repository contains individual projects or code snippets. More likely than not, what you'll find here is sample code or other relatively "useless" demos that exercise some library or API.

Oh, and if anyone other than me is reading this: hi!

## Projects

### Mr Tumble

A credit card number generator, that when given the first six and last four digits, aims to complete the card number. The point of this script was to demonstrate just how trivial it would be to generate the numbers based on what is permissible under PCI rules. 

### Genetic Guesser

An attempt at implementing a simple genetic algorithm that cycles through and guesses what number you've just input. I'm not even sure this is a good implementation of a genetic algorithm, but it's something I should do more work to understand.

### Primes

I wanted to graph the prime numbers over the range n..m. A notoriously inefficient spend of CPU time, but I wanted to write it anyway. There's a few small optimisations in there like ignoring even numbers after 2, etc. I'd like to multithread this next. For me, it's more about applying the principles of optimisation and getting the run time down than it is about generating prime numbers.

### Collatz
The  Collatz conjecture states that for any given number, x, if it's even, you divide by two and if it's odd, you multiply by three and add one, that all numbers for x will reduce down to 1 - eventually. 

```
f(x), x != 1 => if x mod 2 == 0, f(x/2)
                if x mod 2 == 1, f(3x+1)
```

## Tests
The "Build Passing" icon you see along the top refers to all given tests in all of the subprojects, where Travis is able to build and execute the unit tests. In reality, that statement will decompile to "The icon reflects the Python projects build status." 
