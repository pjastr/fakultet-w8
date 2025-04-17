import pytest
import os


@pytest.fixture
def plik_tymczasowy():
    # Setup
    nazwa_pliku = "test_temp.txt"
    with open(nazwa_pliku, "w") as f:
        f.write("dane testowe")

    # Zwracamy zasób do testu
    yield nazwa_pliku

    # Teardown (wykonywane po zakończeniu testu)
    os.remove(nazwa_pliku)


def test_odczyt_pliku(plik_tymczasowy):
    with open(plik_tymczasowy, "r") as f:
        zawartosc = f.read()
    assert zawartosc == "dane testowe"