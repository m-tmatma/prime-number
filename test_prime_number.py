import pytest
from prime_number import is_prime

@pytest.mark.parametrize("number, expected", [
    (0, False),
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (10, False),
    (13, True),
    (17, True),
    (19, True),
    (20, False)
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected