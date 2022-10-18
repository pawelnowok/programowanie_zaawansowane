def suma(x: int, y: int, z: int) -> bool:
    return x + y >= z

sprawdzenie = suma(78, 35, 273)

if sprawdzenie == True:
    print("Suma liczb x i y jest większa lub równa liczbie z")
else:
    print("Suma liczb x i y jest mniejsza od liczby z")