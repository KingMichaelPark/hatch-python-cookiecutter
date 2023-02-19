import pytest
from {{ cookiecutter.project_slug }} import example


@pytest.mark.parametrize("x,y,expected", [(1, 2, 3), (-2, 5, 3)])
def test_example_add(x: int, y: int, expected: int):
    assert example.add(x, y) == expected
