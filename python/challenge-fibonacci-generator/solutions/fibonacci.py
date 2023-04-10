from typing import Generator


def fibonacci_generator(n: int) -> Generator:
    """
    A function that returns a generator that generates the first `n` terms of the Fibonacci sequence.

    Parameters:
    n (int): A single integer, representing the number of terms in the sequence to be generated.

    Returns:
    generator: A generator that generates the first `n` terms of the Fibonacci sequence.
    """
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b
