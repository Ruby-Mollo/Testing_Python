from cola import Cola
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_encolar_y_desencolar_orden(lista):
    cola = Cola()
    for item in lista:
        cola.encolar(item)
    
    assert cola.tamano() == len(lista)
    
    resultados = []
    for _ in range(len(lista)):
        resultados.append(cola.desencolar())
    
    assert resultados == lista

  
    assert cola.esta_vacia()

@given(st.integers())
def test_cola_vacia_comportamiento(item):
    cola = Cola()
    
    # Verificar estado inicial
    assert cola.esta_vacia()
    assert cola.tamano() == 0
    assert cola.ver_frente() == "Vacia Cola"
    assert cola.desencolar() == "Cola vacia"
    
    # Agregar y quitar un elemento
    cola.encolar(item)
    assert not cola.esta_vacia()
    assert cola.tamano() == 1
    assert cola.ver_frente() == item
    assert cola.desencolar() == item
    
    # Verificar que vuelve al estado vacio
    assert cola.esta_vacia()
    assert cola.tamano() == 0

# Prueba de operaciones mixtas
@given(st.lists(st.integers(), min_size=1))
def test_operaciones_mixtas(lista):
    cola = Cola()
    
    # Encolar mitad de elementos
    mitad = len(lista) // 2
    for i in range(mitad):
        cola.encolar(lista[i])
    
    # Verificar tamano y frente
    assert cola.tamano() == mitad
    assert cola.ver_frente() == lista[0]
    
    # Desencolar un elemento
    assert cola.desencolar() == lista[0]
    
    # Encolar el resto
    for i in range(mitad, len(lista)):
        cola.encolar(lista[i])
    
    # Verificar tamano
    assert cola.tamano() == len(lista) - 1
    
    # Desencolar todo y verificar
    resultados = []
    while not cola.esta_vacia():
        resultados.append(cola.desencolar())
    
    esperado = list(reversed(lista[1:mitad])) + list(reversed(lista[mitad:]))
    assert resultados == esperado

if __name__ == "__main__":
    test_encolar_y_desencolar_orden()
    test_cola_vacia_comportamiento()
    test_operaciones_mixtas()
    print("Todas las pruebas pasaron con exito.")
