"""Tests for my_package.core."""

import pytest

from my_package.core import add, greet


class TestGreet:
    def test_greet_with_name(self):
        assert greet("Alice") == "Hello, Alice!"

    def test_greet_with_empty_string(self):
        assert greet("") == "Hello, !"


class TestAdd:
    def test_add_integers(self):
        assert add(2, 3) == 5

    def test_add_floats(self):
        assert add(1.5, 2.5) == pytest.approx(4.0)

    def test_add_negative(self):
        assert add(-1, 1) == 0

    def test_add_mixed(self):
        assert add(1, 2.5) == pytest.approx(3.5)
