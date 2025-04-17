import pytest

@pytest.fixture
def przykladowa_lista():
    return [1, 2, 3, 4, 5]

def test_dlugosc_listy(przykladowa_lista):
    assert len(przykladowa_lista) == 5

def test_suma_listy(przykladowa_lista):
    assert sum(przykladowa_lista) == 15