# Arkusz: https://cke.gov.pl/images/stories/Matura2005/inf_a2.pdf
# Odpowiedzi: https://cke.gov.pl/images/stories/Matura_odp_2005/informat_a2_model.pdf

from collections import Counter  # import z biblioteki standardowej


def najsuma(lista):
    if not lista:
        return

    suma = presuma = 0
    best = lista[0]
    for i in lista:
        if i < 0:
            presuma = suma
        suma += i
        if suma < 0:
            suma = 0
        best = max(suma, best, presuma, i)
    return best


def zliczacz(lista):
    return Counter(lista).most_common(1)  # po prostu zlicza elementy listy
                                          # i zwraca 1 najpopularniejszy element
                                          # wraz z liczbą wystąpień.


def wczytaj(nazwa):
    with open(nazwa) as plik:
        return list(map(int, plik))  # map traktuje funkcją (pierwszy arg) każdy
                                     # kolejny element iterabla (drugi arg)


def podpunkt_a():
    liczby = [1, -2, 6, -5, 7, -3]
    print(f"Najlepsza suma: {najsuma(liczby)}")
    print("""
    Najlepsza suma drugiego ciągu jest równa najlepszej sumie pierwszego ciągu,
    gdyż zamiana podciągu liczb o danym znaku na sumę jego wyrazów nie zmienia
    końcowego wyniku.
    """)


def podpunkt_b():
    print("""
    1. suma, przedsuma := 0; najlepsza = pierwszy element
    2. dla każdego i-tego elementu listy (ozn. ei):
        a. jeśli ei < 0: przedsuma := suma
        b. suma := suma + ei
        c. jeśli suma < 0: suma := 0
        d. wybierz największy element spośród: (suma, najlepsza, przedsuma, ei)
    3. zwróć najlepsza
    """)
    for i in range(1, 4):
        nazwa = f"dane5-{i}.txt"
        print(f"Najlepsza suma dla {nazwa}:  {najsuma(wczytaj(nazwa))}")


def podpunkt_c():
    print("Algorytm zapewniony przez bibliotekę podstawową :P")
    print("Można o nim powiedzieć tylko tyle, że na pewno jest optymalny ;)")
    for i in range(1, 4):
        nazwa = f"dane5-{i}.txt"
        print(f"Najpopularniejszy element w {nazwa}: {zliczacz(wczytaj(nazwa))[0][0]}")


if __name__ == '__main__':
    podpunkt_a()
    podpunkt_b()
    podpunkt_c()
