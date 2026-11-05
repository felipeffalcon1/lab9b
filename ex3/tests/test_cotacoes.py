import pytest
from cotacoes import menor_preco, dia_da_compra

def test_cotacoes_iniciais():
    assert menor_preco([32, 28, 35, 25, 30]) == 25
    assert menor_preco([40]) == 40
    assert menor_preco([20, 27]) == 20

    assert dia_da_compra([32, 28, 35, 25, 30]) == 3
    assert dia_da_compra([40]) == 0
    assert dia_da_compra([20, 27]) == 0

def test_cotacoes_excecao():
    with pytest.raises(ValueError, match="sem cotacoes"):
        menor_preco([])
    with pytest.raises(ValueError, match="sem cotacoes"):
        dia_da_compra([])

def test_cotacoes_desempate():
    assert dia_da_compra([10, 20, 10]) == 2
