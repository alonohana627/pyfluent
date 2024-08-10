def set_test():
    a = {1, 2, 3, 4}
    b = {1, 2, 2, 3, 4, 4}
    assert a == set([1, 2, 3, 4])
    assert b == {1, 2, 3, 4}


def set_inter_test():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    assert a & b == {3, 4}


def set_uni_test():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    assert a | b == {1, 2, 3, 4, 5, 6}


def set_sub_test():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    assert a - b == {1, 2}


def set_xor_test():
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    assert a ^ b == {1, 2, 5, 6}
