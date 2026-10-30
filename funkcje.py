try:
    import machine
except ImportError:
    pass

import time
try:
    from test_rata_rowna import testy
except ImportError:
    def testy():
        print("Pominiecie testow.")

def oblicz_rate_kredytu(K, r, n):
    if K <= 0:
        raise ValueError("Kwota kredytu musi byc wieksza od zera")
    if n <= 0:
        raise ValueError("Okres kredytowy musi byc wiekszy niz zero")
    if r < 0:
        raise ValueError("Oprocentowanie roczne nie moze byc ujemne")
    
    # Przypadek 0% oprocentowanie
    if r == 0:
        return float(K / n)
    
    # Wzor na rate równą
    q = 1 + r / 1200
    rata = K * q**n * ((q - 1) / (q**n - 1))
    return float(rata)

def zmierz_wydajnosc(x):
    print("\n--- Pomiar wydajnosci dla duzych danych ---")
    start_tick = time.ticks_ms()
    for _ in range(x):
        _ = oblicz_rate_kredytu(5000000.0, 8.5, 360)
    koniec_tick = time.ticks_ms()
    czas_trwania = time.ticks_diff(koniec_tick, start_tick)

    print("Czas wykonywania {} iteracji: {} ms".format(x, czas_trwania))

def main():
    testy()
    zmierz_wydajnosc(10000)
    zmierz_wydajnosc(1000000)
    
    print("\n--- Przyklady obliczen ---")
    przyklady = [
        (50000, 4.5, 60),  # Przyklad 1: maly kredyt
        (400000, 2.3, 300),  # Przyklad 2: duzy kredyt hipoteczny
        (15000, 0, 18),  # Przyklad 3: pozyczka 0%
    ]

    for i, (kwota, oprocentowanie, okres) in enumerate(przyklady, 1):
        rata = oblicz_rate_kredytu(kwota, oprocentowanie, okres)
        print("Przyklad {}: Kwota = {}, Oprocentowanie = {}%, Okres = {} miesiecy. Wyliczona Rata = {:.2f}".format(
            i, kwota, oprocentowanie, okres, rata))

    print("\n--- Manualny kalkulator ---")
    try:
        kwota_wejscie = float(input("Podaj kwote kredytu: "))
        opr_wejscie = float(input("Podaj roczne oprocentowanie w %: "))
        mies_wejscie = int(input("Podaj okres w miesiacach: "))

        obliczona_rata = oblicz_rate_kredytu(kwota_wejscie, opr_wejscie, mies_wejscie)
        print("Miesieczna rata wynosi {:.2f}".format(obliczona_rata))
    except ValueError:
        print("Niepoprawnie wprowadzone wartosci liczbowe")
    except KeyboardInterrupt:
        print("\nPrzerwano wprowadzanie danych.")
    except Exception as e:
        print("Wystapil nieoczekiwany blad: {}".format(e))

if __name__ == "__main__":
    main()