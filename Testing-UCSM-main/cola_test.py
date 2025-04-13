from cola import Cola

def test_cola():
    cola = Cola()
    assert cola.esta_vacia() == True

    cola.encolar(5)
    cola.encolar(10)
    assert cola.tamano() == 2
    assert cola.ver_frente() == 5

    assert cola.desencolar() == 5
    assert cola.desencolar() == 10
    assert cola.desencolar() == "Cola vacia"

test_cola()
print("Exito")
from cola import Cola

def test_cola():
    cola = Cola()
    assert cola.esta_vacia() == True

    cola.encolar(5)
    cola.encolar(10)
    assert cola.tamano() == 2
    assert cola.ver_frente() == 5

    assert cola.desencolar() == 5
    assert cola.desencolar() == 10
    assert cola.desencolar() == "Cola vacia"

test_cola()
print("Exito")
