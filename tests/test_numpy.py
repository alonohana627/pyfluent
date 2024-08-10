import numpy as np
import pytest


# Examples for how to use numpy


def test_shape():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    assert arr.shape == (2, 3)
    with pytest.raises(ValueError):
        _ = np.array([[1, 2, 3], [4, 5]])
    arr = np.array(
        [
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            [
                [4, 5, 6],
                [7, 8, 9],
            ],
        ]
    )
    assert arr.shape == (2, 2, 3)


def test_ndim():
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    assert arr.ndim == 2
    arr = np.array(
        [
            [
                [1, 2, 3],
                [4, 5, 6],
            ],
            [
                [4, 5, 6],
                [7, 8, 9],
            ],
        ]
    )
    assert arr.ndim == 3


def test_zeros():
    arr = np.zeros((3, 4))
    assert arr.shape == (3, 4)
    assert np.all(arr == 0)


def test_arrange():
    arr = np.arange(10)
    assert arr.shape == (10,)
    assert np.all(arr == np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    arr = np.arange(2, 9, 2)
    assert arr.shape == (4,)
    assert np.all(arr == np.array([2, 4, 6, 8]))
