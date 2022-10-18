def check(lista: list, x: int) -> bool:
    return x in lista

sprawdzenie = check([1, 2, 3, 4, 5, 6, 7, 8, 9], 12)

if sprawdzenie == True:
    print("Element x należy do listy")
else:
    print("Element x nie należy do listy")