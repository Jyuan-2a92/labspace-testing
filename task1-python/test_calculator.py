import pytest
from calculator import Calculator

def test_addition():
    c = Calculator()
    assert c.add(2, 3) == 5

def test_subtraction():
    c = Calculator()
    assert c.subtract(9, 4) == 5

def test_multiply():
    c = Calculator()
    assert c.multiply(10, 4) == 40

def test_divide():
    c = Calculator()
    assert c.divide(5704, 4) == 1426

def test_divide_by_zero():
    c = Calculator()
    with pytest.raises(ValueError):
        c.divide(18, 0)

def test_power():
    c = Calculator()
    assert c.power(4,2) == 16

def test_prime():
    c = Calculator()
    assert c.is_prime(3)

def test_composite():
    c = Calculator()
    assert not(c.is_prime(24))

def test_even():
    c = Calculator()
    assert c.is_even(10)

def test_odd():
    c = Calculator()
    assert not(c.is_even(53))

def test_odd_negative():
    c = Calculator()
    assert c.is_even(-11) is False

def test_fizzbuzz_15():
    c = Calculator()
    assert c.is_fizzbuzz(15) is True

def test_fizzbuzz_7():
    c = Calculator()
    assert c.is_fizzbuzz(7) is False

def test_fizzbuzz_6():
    c = Calculator()
    assert c.is_fizzbuzz(6) is False
