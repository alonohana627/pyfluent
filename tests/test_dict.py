import pytest


def get_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 2, "authors": [*names]}:
            return names
        case {"type": "book", "api": 1, "author": name}:
            return [name]
        case {"type": "book"}:
            raise ValueError(f"Invalid 'book' record: {record!r}")
        case {"type": "movie", "director": name}:
            return [name]
        case _:
            raise ValueError(f"Invalid record: {record!r}")


def test_merge():
    a = {"a": 3, "b": 4, "c": 5, "d": 6}
    b = {"b": 4, "d": 6, "e": 10}
    c = a | b
    assert c == {"a": 3, "b": 4, "c": 5, "d": 6, "e": 10}


def test_get_creators():
    record1 = {"type": "book", "api": 2, "authors": ["alon", "ohana"]}
    record2 = {"type": "book", "api": 1, "author": "alon ohana"}
    record3 = {}
    assert get_creators(record1) == ["alon", "ohana"]
    assert get_creators(record2) == ["alon ohana"]
    with pytest.raises(ValueError):
        _ = get_creators(record3)
