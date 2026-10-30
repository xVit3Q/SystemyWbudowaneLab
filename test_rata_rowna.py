from funkcje import oblicz_rate_kredytu

def testy():
    print("Uruchomienie testow...")

    # test 1 - Standardowy
    wynik_1 = oblicz_rate_kredytu(100000, 5, 120)
    assert (abs(wynik_1 - 1060.66) < 0.1), "Test 1 sie nie powiodl"

    # test 2 - Przypadek brzegowy - 0%
    wynik_2 = oblicz_rate_kredytu(48000, 0, 12)
    assert (abs(wynik_2 - 4000) < 1e-5), "Test 2 nie powiodl sie: Bledna obsluga przypadku oprocentowania zerowego"

    # test 3 - Przypadek brzegowy - krotki okres kredytowy 1 miesiac
    wynik_3 = oblicz_rate_kredytu(10000, 12, 1)
    assert (abs(wynik_3 - 10100) < 1e-5), "Test 3 nie powiodl sie: Bledny wynik dla krotkiego okresu"

    # test 4: Ujemna kwota kredytu
    blad_dane = False
    try:
        oblicz_rate_kredytu(-100000, 5, 12)
    except ValueError:
        blad_dane = True
    assert blad_dane, "Test 4 nie powiodl sie: Zle obslugiwany wyjatek z ujemna kwota"

    # Test 5: Okres kredytowy zerowy
    blad_dane = False
    try:
        oblicz_rate_kredytu(100000, 5, 0)
    except ValueError:
        blad_dane = True
    assert blad_dane, "Test 5 nie powiodl sie: Zerowy okres kredytowania"

    print("Wszystkie testy zakonczone powodzeniem")

