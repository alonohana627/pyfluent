from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    address: str


def match_person(person: Person):
    match person:
        case Person(name=n, age=a, address=_):
            print(f"Person {n} is {a} years old")
        case _:
            print("This object is not a Person instance")


def match_example(value):
    match value:
        case 0 | 1:
            print("Value is 0 or 1")
        case int(x) if x < 10:
            print("Value is an int less than 10")
        case int(x):
            print("Value is an int greater than or equal to 10")
        case list([1, 2, *rest]):
            print("Value is a list starting with 1 and 2")
        case str(s) if s.lower() == "hello":
            print("Value is a string 'hello' (case insensitive)")
        case _:
            print("Value did not match any patterns")


# Next one is matching with a dictionary
def match_dict_example(value):
    match value:
        case {"name": str(n), "age": int(a)}:
            print(f"Dict with name: {n} and age: {a}")
        case {"name": str(n)}:
            print(f"Dict with name: {n}, age is not present")
        case {"age": int(a)}:
            print(f"Dict with age: {a}, name is not present")
        case {}:
            print("Empty dictionary")
        case _:
            print("Value did not match any patterns")
