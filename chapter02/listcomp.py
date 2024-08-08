def regular_list_op(lst: list, action):
    for i, e in enumerate(lst):
        lst[i] = action(e)
    return lst


def list_comp_op(lst: list, action):
    return [action(a) for a in lst]


def filter_listcomp_example(lst: list, condition: callable):
    return [a for a in lst if condition(a)]


def filter_example(lst: list, condition: callable):
    return list(filter(condition, lst))


def map_example(lst: list, mapper: callable):
    return list(map(mapper, lst))


def cartesian_matrix():
    operating_systems = ["windows", "linux", "darwin", "openbsd", "freebsd", "fuchsia"]
    versions = ["x86-64", "arm64", "sparc", "risc-v"]
    python_versions = ["3.10", "3.11", "3.12"]
    return [
        (operating_system, version, python_version)
        for operating_system in operating_systems
        for version in versions
        for python_version in python_versions
    ]
