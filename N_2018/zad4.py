# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2018/formula_od_2015/informatyka/MIN-R2_1P-182.pdf
# Wyniki: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2018/formula_od_2015/Zasady_oceniania/MIN-R2_1P-182_zasady_oceniania.pdf
import os


def wczytaj(nazwa):
    with open(nazwa) as plik:
        return list(map(str.strip, plik))


def podpunkt_1(dane):
    return "".join(s[9] for s in dane[39::40] if len(s) >= 9)


def podpunkt_2(dane):
    prep = [(len(set(wyraz)), -i, wyraz) for i, wyraz in enumerate(dane)]
    # Użycie na drugiej pozycji ujemnego indeksu pozwala funkcji max() wyciągnąć
    # dokładnie to, czego potrzebujemy - wyraz o największej liczbie indywidualnych
    # liter leżący najbliżej początku listy/pliku.
    return max(prep)


def podpunkt_3(dane):
    return [wyraz for wyraz in dane if (ord(max(wyraz)) - ord(min(wyraz))) <= 10]


if __name__ == "__main__":
    os.makedirs("wyniki", exist_ok=True)
    dane = wczytaj("dane/sygnaly.txt")
    print(podpunkt_1(dane))
    print(*podpunkt_2(dane)[::-2])  # najpierw wyraz, potem długość, indeks pomijamy
    with open("wyniki/wyniki4.txt", "w") as wyniki:
        wyniki.writelines(map(lambda x: f"{x}\n", podpunkt_3(dane)))
