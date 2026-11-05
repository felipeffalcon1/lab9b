import pytest
from multa import valor_com_multa

def test_multa_valor_limite():
    assert valor_com_multa(100, 0) == 100.0
    assert valor_com_multa(100, 5) == 100.0
    assert valor_com_multa(100, 6) == 101.0
    assert valor_com_multa(100, 60) == 155.0

    with pytest.raises(ValueError, match="atraso invalido"):
        valor_com_multa(100, -1)
    with pytest.raises(ValueError, match="atraso invalido"):
        valor_com_multa(100, 61)
