import pytest

@pytest.mark.slow
def test_powolna_operacja():
    # Symulacja długotrwałej operacji
    import time
    time.sleep(10)
    assert True

@pytest.mark.fast
def test_szybka_operacja():
    assert True