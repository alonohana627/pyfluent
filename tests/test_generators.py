import chapter02.generators as gen

import pytest


def test_gen_fib():
    fib = gen.fibonacci_generator()
    a = next(fib)
    b = next(fib)
    c = next(fib)
    d = next(fib)
    e = next(fib)
    assert a == 1
    assert b == 1
    assert c == 2
    assert d == 3
    assert e == 5


if __name__ == "__main__":
    pytest.main()
