# Fibonacci Generator

## Problem Statement

Write a Python function called `fibonacci_generator` that takes an integer `n` as an argument and returns a generator that generates the first `n` terms of the Fibonacci sequence.

The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers. The first two numbers of the sequence are 0 and 1, and the rest of the numbers are calculated by adding the two preceding numbers.

## Requirements

- Input: A single integer `n` (1 <= n <= 10^3), representing the number of terms in the sequence to be generated.
- Output: A generator that generates the first `n` terms of the Fibonacci sequence.
- You can assume that the input will always be a positive integer.
- Your code should be able to handle large values of `n`.

## Example

```python
>>> fibonacci_gen = fibonacci_generator(5)
>>> for i in fibonacci_gen:
...     print(i)
...
0
1
1
2
3
```

## Hints

- You can use the `yield` statement to create a generator.
- To generate the next number in the Fibonacci sequence, add the two preceding numbers.
- The first two terms of the sequence are 0 and 1.
