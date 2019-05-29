# Arkusz z treścią i odpowiedziami: https://cke.gov.pl/images/stories/mat3_07/inf_pr_cz2_rozw.pdf
import math


class SitoE:
    "Sito Eratostenesa"

    def __init__(self, nmax):
        self._nmax = nmax
        self._cache = {i: True for i in range(2, nmax + 1)}
        g = int(math.sqrt(nmax)) + 1

        for i in range(2, g):
            if self._cache[i]:
                w = i * i
                while w <= nmax:
                    self._cache[w] = False
                    w += i

    def __contains__(self, item):
        # pozwala użyć operatora 'in' do sprawdzenia, czy liczba jest pierwsza
        if not isinstance(item, int):
            raise TypeError(f'Nieprawidłowy typ ({type(item)})')
        if item > self._nmax:
            raise ValueError(f'Sprawdzana wartość ({item}) poza zakresem sita ({self._nmax}).')
        return self._cache.get(item, False)


sito = SitoE(1006700)


def suprime(liczba):
    return liczba in sito and sum(int(i) for i in str(liczba)) in sito


def suBrime(liczba):
    return suprime(liczba) and sum(int(i) for i in f'{liczba:b}') in sito


def ile_suBrimes(start, stop):
    return sum(1 for i in range(start, stop + 1) if suBrime(i))


def podpunkt_a():
    print(f"Przedział 1: {ile_suBrimes(2, 1000)}")
    print(f"Przedział 2: {ile_suBrimes(100, 10000)}")
    print(f"Przedział 3: {ile_suBrimes(1000, 100000)}")


def podpunkt_b():
    wynik = sum(1 for i in range(100, 10001) if sum(int(j) for j in str(i)) in sito)
    print(f"Liczba liczb w danym przedziale, których suma cyfr jest pierwsza: {wynik}")

    translator = {False: "NIE", True: "TAK"}
    test_sumy = sum(i for i in range(100, 10000) if suBrime(i)) in sito
    print(f"Czy suma liczb superB z danego przedziału jest pierwsza? {translator[test_sumy]}")


if __name__ == '__main__':
    podpunkt_a()
    podpunkt_b()
