# Code: A Public Scratchspace

[![Build Status](https://travis-ci.com/mrajweir/Code.svg?branch=master)](https://travis-ci.com/mrajweir/Code)

This repository contains individual projects or code snippets. More likely than not, what you'll find here is sample code or other relatively "useless" demos that exercise some library or API.

Oh, and if anyone other than me is reading this: hi!

## Projects

### Aliquot Sequences

An aliquote sequence is a sequence of numbers who's factors add up to a new number. It's a recursive process of adding factors together of integers. For example, Factors of 8 are 1, 2, 4, (and 8 - but we ignore the number itself.) If you add those facotrs, you get 7. Which is prime, and so only has two factors (1 and 7 - but we don't count the 7). Aliquote sequences produce runs of numbers that either end with 1, a perfect number, or a socialble/amicable loop of numbers.
### Sudoku

A brute force Sudoku solver with no optimization, except for the solving of blocks. (You only need four cells in non-adjacent positions if you know the integers for the rows and columns.) Strangely proud of it, and it was fun to write. I'll probably work on profiling it and making it quicker. Ideally I'd love it to solve the general problem of Sudoku.

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

### Monopoly Deluxe
Camelot run the UK lottery and offer online "instant win" games, and I thought the Monopoly Deluxe game was particularly interesting. The player (you) have two dice which are rolled: the first dice is the number of moves you make around the board, and the second is a multipler. If you roll a 2, and a X4, you'd get 8 moves. It dawned on me that a lot of numbers would be excluded from the game. For example, you can't roll a 7 anymore, or 11. So I simmed up potential routes around the board and *in a true game of chance* what that would look like.

### RioCurve
Scrapes the raider.io API (gently) and pulls graphs and statistics from Mythic Plus runs. Good way to see the meta in action, and where the M+ community is at large.

## Tests
The "Build Passing" icon you see along the top refers to all given tests in all of the subprojects, where Travis is able to build and execute the unit tests. In reality, that statement will decompile to "The icon reflects the Python projects build status." 
