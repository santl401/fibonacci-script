import pytest
from fibonacci import fibonacci


@pytest.mark.parametrize(
    "n, expected",
    [
        (-10, []),
        (0, []),
        (1, [0]),
        (2, [0, 1]),
        (3, [0, 1, 1]),
        (7, [0, 1, 1, 2, 3, 5, 8]),
    ],
)
def test_fibonacci_values(n, expected):
    assert fibonacci(n) == expected


def test_fibonacci_type_error():
    with pytest.raises(TypeError):
        fibonacci("5")
