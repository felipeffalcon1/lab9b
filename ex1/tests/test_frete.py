import pytest
from frete import modalidade_frete

def test_modalidade_frete_suite_inicial():
    assert modalidade_frete(5, 300) == "Correio expresso"
    assert modalidade_frete(2, 1000) == "Correio economico"

def test_modalidade_frete_completos():
    assert modalidade_frete(25, 100) == "Transportadora"
    assert modalidade_frete(5, 10) == "Motoboy"
    
    with pytest.raises(ValueError, match="Peso invalido"):
        modalidade_frete(0, 100)
    with pytest.raises(ValueError, match="Peso invalido"):
        modalidade_frete(31, 100)
    with pytest.raises(ValueError, match="Distancia invalida"):
        modalidade_frete(10, -1)
    with pytest.raises(ValueError, match="Distancia invalida"):
        modalidade_frete(10, 5001)
