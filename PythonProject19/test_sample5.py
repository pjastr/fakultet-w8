import pytest

@pytest.mark.parametrize("liczba,kwadrat", [(1, 1), (2, 4), (3, 9), (4, 16)])
def test_potegowanie(liczba, kwadrat):
    assert liczba ** 2 == kwadrat

# Można też użyć wielu dekoratorów do bardziej złożonych przypadków
@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_iloczyn(x, y):
    # Ten test zostanie uruchomiony dla wszystkich kombinacji x i y
    # (0,2), (0,3), (1,2), (1,3)
    print(f"Testowanie dla x={x} i y={y}")
    assert x * y == x * y 