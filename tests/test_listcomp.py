import chapter02.listcomp as listcomp

import pytest


# Testing regular_list_op function
def test_regular_list_op():
    def double(x):
        return x * 2

    assert listcomp.regular_list_op([1, 2, 3], double) == [2, 4, 6]


# Testing list_comp_op function
def test_list_comp_op():
    def double(x):
        return x * 2

    assert listcomp.list_comp_op([1, 2, 3], double) == [2, 4, 6]


# Testing filter_listcomp_example function
def test_filter_listcomp_example():
    def is_even(x):
        return x % 2 == 0

    assert listcomp.filter_listcomp_example([1, 2, 3, 4, 5], is_even) == [2, 4]


# Testing filter_example function
def test_filter_example():
    def is_even(x):
        return x % 2 == 0

    assert listcomp.filter_example([1, 2, 3, 4, 5], is_even) == [2, 4]


# Testing map_example function
def test_map_example():
    def double(x):
        return x * 2

    assert listcomp.map_example([1, 2, 3], double) == [2, 4, 6]


# This code collects all the test cases in this script
if __name__ == "__main__":
    pytest.main()
