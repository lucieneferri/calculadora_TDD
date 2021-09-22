
from calculadora import Calculadora #precisam estar na mesma pasta

#estes testes são feitos primeiros que os códigos de fato
def test_01_soma_0_0():
    calc = Calculadora()
    assert calc.soma(0,0) == 0

def teste_01_soma_0_10():
    calc = Calculadora()
    assert calc.soma(0, 10) == 10

def teste_01_soma_3_5():
    calc = Calculadora()
    assert calc.soma(3, 5) == 8

def test_subtrai_10_2():
    calc = Calculadora()
    assert calc.subtrai(10,2) == 8

def test_subtrai_2_10():
    calc = Calculadora()
    assert calc.subtrai(2,10) == -8


