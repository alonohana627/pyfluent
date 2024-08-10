from chapter03.dump import dump


def dump_temp():
    tst_fixture = {"a": 0, **{"x": 1}, "y": 2, **{"z": 3, "x": 4}}
    a = dump(**tst_fixture)
    b = dump(tst_fixture)
    assert a == {"a": 0, "x": 4, "y": 2, "z": 3}
    assert b == {"a": 0, "x": 4, "y": 2, "z": 3}
