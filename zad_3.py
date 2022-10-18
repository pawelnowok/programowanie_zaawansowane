def parzysta(x: int) -> bool:
    return x % 2 == 0

sprawdzenie = parzysta(6461)

if sprawdzenie == True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
