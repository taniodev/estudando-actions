from contas import multiplicar, somar, subtrair


def test_multiplicar():
        assert multiplicar(3, 2) == 6


def test_somar():
    assert somar(3, 4) == 7


def test_subtrair():
        assert subtrair(9, 4) == 5
