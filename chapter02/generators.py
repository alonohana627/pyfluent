def fibonacci_generator():
    """
    Generating fibonacci numbers.
    How to use:
    `fib = fibonacci_generator()`
    `x = next(fib)`
    `y = next(fib)`
    """
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b
