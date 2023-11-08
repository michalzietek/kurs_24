import pytest

from zajecia_12.student import Student


@pytest.fixture
def student():
    return Student(name="Michal", surname="Zietkowski", age=20)