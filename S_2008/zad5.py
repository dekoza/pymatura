# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2008/inform_r2_rozw.pdf
# Wyniki: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2008/wyniki08.rar
import os


def wczytaj(nazwa):
    with open(nazwa) as plik:
        return list(i for i in map(str.strip, plik) if i)


def zapisz_wyrazy(dane, nazwa):
    with open(nazwa, "w") as wyniki:
        wyniki.writelines(map(lambda h: f"{h}\n", dane))


def podpunkt_a(dane):
    hasla = [f"{h[::-1]}" for h in dane]

    haslo_min = min(hasla, key=len)
    haslo_max = max(hasla, key=len)

    zapisz_wyrazy(hasla, "wyniki/hasla_a.txt")

    with open("wyniki/slowa_a.txt", "w") as slowa:
        slowa.writelines(
            [f"{haslo_min} {len(haslo_min)}\n", f"{haslo_max} {len(haslo_max)}\n"]
        )


def koduj(slowo):
    for i in range(len(slowo), 0, -1):
        if slowo[:i] == slowo[:i][::-1]:
            return f"{slowo[i:][::-1]}{slowo}"


def szukaj_len(dane, var):
    return [h for h in dane if len(h) == var]


def podpunkt_b(dane):
    zakodowane = [koduj(s) for s in dane]
    zapisz_wyrazy(zakodowane, "wyniki/hasla_b.txt")

    dwunastki = szukaj_len(zakodowane, 12)

    haslo_min = min(zakodowane, key=len)
    haslo_max = max(zakodowane, key=len)

    suma = sum(len(h) for h in zakodowane)

    with open("wyniki/slowa_b.txt", "w") as slowa:
        slowa.writelines(
            [
                "1\n",
                "\n".join(dwunastki),
                "\n2\n",
                f"{haslo_min}\n",
                f"{haslo_max}\n",
                "3\n",
                f"{suma}\n",
            ]
        )


if __name__ == "__main__":
    os.makedirs("wyniki", exist_ok=True)
    dane = wczytaj("dane/slowa.txt")
    podpunkt_a(dane)
    podpunkt_b(dane)
