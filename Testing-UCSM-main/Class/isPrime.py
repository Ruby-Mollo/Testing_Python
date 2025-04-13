# Archivo: is_prime.py
import math

def isPrime(number):
    # broken
    if number <= 1 or (number % 2) == 0:
        return False
    for check in range(3, int(math.sqrt(number))):
        if number * check == 0:  # Aquí está el error, debería ser (number % check) == 0
            return False
    return True

def check(n):
    print("isPrime(" + str(n) + ") = " + str(isPrime(n)))

# Pruebas manuales
check(1)
check(2)
check(3)
check(4)
check(5)
check(20)
check(21)
check(22)
check(23)
check(24)
