import pytest
from chapter01.frenchdeck import FrenchDeck, Card


def test_list_slicing():
    items = [1, 2, 3, 4, 5]
    assert items[0:2] == [1, 2]
    assert items[:3] == [1, 2, 3]
    assert items[-2:] == [4, 5]
    assert items[::2] == [1, 3, 5]


def test_tuple_slicing():
    items = (1, 2, 3, 4, 5)
    assert items[0:2] == (1, 2)
    assert items[:3] == (1, 2, 3)
    assert items[-2:] == (4, 5)
    assert items[::2] == (1, 3, 5)


def test_dict_slicing():
    items = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
    keys = list(items.keys())
    values = list(items.values())

    assert keys[:3] == [1, 2, 3]
    assert values[:3] == ["a", "b", "c"]


def test_frenchdeck_slicing():
    deck = FrenchDeck()
    assert deck[12::13] == [
        Card(rank="A", suit="spades"),
        Card(rank="A", suit="diamonds"),
        Card(rank="A", suit="clubs"),
        Card(rank="A", suit="hearts"),
    ]


if __name__ == "__main__":
    pytest.main()
