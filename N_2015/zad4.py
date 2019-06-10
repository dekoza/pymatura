# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_od_2015/MIN-R2_1P-152.pdf
# Wyniki: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2015/formula_od_2015/odpowiedzi/MIN-R1-N.pdf
from collections import Counter


def wczytaj(nazwa):
    with open(nazwa) as plik:
        # return list(map(str.strip, plik))  # SKRÓTOWIEC

        wynik = []
        for linia in plik:
            wynik.append(linia.strip())
        return wynik


def przezerowane(liczby):
    # return sum(1 for i in liczby if Counter(i).most_common(1)[0][0] == '0')  # SKRÓTOWIEC

    suma = 0
    for i in liczby:
        if Counter(i).most_common(1)[0][0] == '0':
            suma += 1
    return suma


def podzielne(liczby):
    przez_2 = 0
    przez_8 = 0
    for liczba in liczby:
        if liczba[-1] == '0':
            przez_2 += 1
        if liczba[-3:] == '000':
            przez_8 += 1

    return {'2': przez_2, '8': przez_8}


def gdzie_minmax(liczby):
    # algorytmicznie suboptymalne, ale bardziej idiomatyczne
    pomocnik = [int(i, 2) for i in liczby]
    gdzie_min = pomocnik.index(min(pomocnik))
    gdzie_max = pomocnik.index(max(pomocnik))
    return gdzie_min, gdzie_max


if __name__ == '__main__':
    liczby = wczytaj('liczby.txt')

    wynik = podzielne(liczby)
    gdzie_min, gdzie_max = gdzie_minmax(liczby)

    print(f"Liczb mających więcej zer niż jedynek: {przezerowane(liczby)}.")
    print(f"Liczb podzielnych przez 2: {wynik['2']}.")
    print(f"Liczb podzielnych przez 8: {wynik['8']}.")
    print(f'Najmniejsza liczba znajduje się w wierszu {gdzie_min + 1}')  # bo w życiu liczymy od 1
    print(f'Największa liczba znajduje się w wierszu {gdzie_max + 1}')
