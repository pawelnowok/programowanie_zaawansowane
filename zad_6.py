def check(lista1: list, lista2: list) -> list:
    lista3 = set(lista1 + lista2)
    return lista3

sprawdzenie = check([1, 2, 3, 4, 5], [1, 4, 6, 7, 8, 9])

print(sprawdzenie)