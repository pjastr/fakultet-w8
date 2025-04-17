import pytest  # dla wyjątku


def test_asercje():
    # Proste asercje
    assert True
    assert "tekst" == "tekst"
    assert 10 > 5

    # Asercje z wiadomością
    assert 3 + 4 == 7, "Podstawowa arytmetyka nie działa!"

    # Sprawdzanie wyjątków
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_porownanie_list():
    lista1 = [1, 2, 4]
    lista2 = [1, 2, 4]
    assert lista1 == lista2  # Ten test nie przejdzie i pytest pokaże różnicę