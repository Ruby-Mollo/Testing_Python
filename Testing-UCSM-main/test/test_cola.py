from cola import Cola
import pytest

def test_cola_encolar_desencolar():
    cola = Cola()

    assert cola.esta_vacia() == True
    
    # Añadir elementos
    cola.encolar(1)
    cola.encolar(2)

    assert cola.esta_vacia() == False
    assert cola.tamano() == 2
    
    assert cola.ver_frente() == 1
    
    assert cola.desencolar() == 1
    assert cola.desencolar() == 2

    assert cola.esta_vacia() == True

def test_cola_vacia():
    cola = Cola()
    assert cola.desencolar() == "Cola vacia"
    assert cola.ver_frente() == "Vacia Cola"
