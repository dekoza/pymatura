# Arkusz: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_od_2015/MIN-R2_1P-162.pdf
# Wyniki: https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2015/Arkusze_egzaminacyjne/2016/formula_od_2015/zasady_oceniania/MIN-R1-N.pdf


def cezar(napis: str, klucz: int) -> str:
    # W ramach prezentacji kliku trików postanowiłem nie używać słowa kluczowego 'if' w tej funkcji

    klucz = (-1 * (klucz < 0) or 1) * (abs(klucz) % 26)
    wynik = []

    for lit in napis.upper():
        num = ord(lit) + klucz
        num = num + 26 * ((num < ord('A')) - (num > ord('Z')))
        wynik.append(chr(num))
    return ''.join(wynik)


### Poniżej wersja wymagająca Pythona 3.8

# def cezar(napis: str, klucz: int) -> str:
#     klucz %= 26
#
#     return ''.join(chr((num:=ord(l) + klucz) + 26 * ((num < ord('A')) - (num > ord('Z')))) for l in napis.upper())

def podpunkt_1():
    with open('dane_6_1.txt') as dane, open('wyniki_6_1.txt', 'w') as wyniki:
        for napis in dane:
            wyniki.write(f"{cezar(napis.strip(), 107)}\n")


def podpunkt_2():
    with open('dane_6_2.txt') as dane, open('wyniki_6_2.txt', 'w') as wyniki:
        for linia in dane:
            try:
                szyfr, klucz = linia.strip().split()
            except ValueError:  # plik źródłowy zawiera błędne linie bez klucza
                continue
            wyniki.write(f"{cezar(szyfr, -int(klucz))}\n")


def podpunkt_3():
    with open('dane_6_3.txt') as dane, open('wyniki_6_3.txt', 'w') as wyniki:
        for linia in dane:
            if linia.strip():
                wyraz, szyfr = linia.strip().split()
                klucz = ord(szyfr[0]) - ord(wyraz[0])
                spr = cezar(wyraz, klucz)
                if spr != szyfr:
                    wyniki.write(f'{wyraz}\n')


if __name__ == '__main__':
    podpunkt_1()
    podpunkt_2()
    podpunkt_3()
