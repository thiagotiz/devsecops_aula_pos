import pytest
from test_op import somar
from test_op import subtrair

def test_somar():
    assert somar(2,3) == 5


def test_subtracao():
    assert subtrair(12,3) == 9