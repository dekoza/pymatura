# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_od_2015/MIN-R2_1P-162.pdf
# Wyniki: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_od_2015/zasady_oceniania/MIN-R1-N.pdf


def cezar(napis: str, klucz: int) -> str:
    # return ''.join(chr(ord('A') + (ord(l) + klucz - ord('A')) % 26) for l in napis)# SKRÓTOWIEC
    klej = ""
    literki = []
    for l in napis:
        kod_ascii = ord(l)
        zakodowane = (kod_ascii + klucz - ord("A")) % 26  # przesunięcie & zapętlenie
        kod_wynikowy = ord("A") + zakodowane
        litera = chr(kod_wynikowy)
        literki += litera
    return klej.join(
        literki
    )  # literki zostaną połączone w jeden napis, porozdzielane "klejem"


def podpunkt_1():
    with open("dane_6_1.txt") as dane, open("wyniki_6_1.txt", "w") as wyniki:
        for napis in dane:
            wyniki.write(f"{cezar(napis.strip(), 107)}\n")


def podpunkt_2():
    with open("dane_6_2.txt") as dane, open("wyniki_6_2.txt", "w") as wyniki:
        for linia in dane:
            try:
                szyfr, klucz = linia.strip().split()
            except ValueError:  # plik źródłowy zawiera błędne linie bez klucza
                print(f"Błędne dane: {linia}")
            else:
                wyniki.write(f"{cezar(szyfr, -int(klucz))}\n")


def podpunkt_3():
    with open("dane_6_3.txt") as dane, open("wyniki_6_3.txt", "w") as wyniki:
        for linia in dane:
            try:
                wyraz, szyfr = linia.strip().split()
            except ValueError:
                print(f"Błędne dane: {linia}")
            else:
                klucz = ord(szyfr[0]) - ord(wyraz[0])
                spr = cezar(wyraz, klucz)
                if spr != szyfr:
                    wyniki.write(f"{wyraz}\n")


if __name__ == "__main__":
    podpunkt_1()
    podpunkt_2()
    podpunkt_3()
