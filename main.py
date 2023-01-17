# Dane wejściowe

liczba_elementow = int(input("Podaj ilość elementów paczki: "))

liczba_paczek_wyslanych = 0

liczba_kilogramow_wyslanych = 0

suma_pustych_kilogramow = 0

waga_najlzejszej_paczki = 20

# numer_najlzejszej_paczki = None

nr_elementu = 0

waga_paczki = 0

# Pętla

for nr_elementu in range(liczba_elementow):
    waga_elementu = float(input(f"Podaj wagę elementu nr. {nr_elementu +1} [kg]: "))
    if waga_elementu < 1 or waga_elementu > 10:
        print("Za duża waga elementu!")
        break
    waga_paczki += waga_elementu

print(waga_paczki)
if waga_paczki <= 20:
    liczba_paczek_wyslanych += 1
    liczba_kilogramow_wyslanych += waga_paczki
    suma_pustych_kilogramow += (20 - waga_paczki)
else:
    liczba_paczek_wyslanych += 1
    waga_paczki -= 20
    if waga_paczki < waga_najlzejszej_paczki:
        liczba_paczek_wyslanych += 1
        liczba_kilogramow_wyslanych += waga_paczki
        suma_pustych_kilogramow += (20 - waga_paczki)

# Wyniki

print(f"1. Liczba wysłanych paczek {liczba_paczek_wyslanych} \n"
      f"2. liczba wysłanych kilogramów {liczba_kilogramow_wyslanych} \n"
      f"3. Suma pustych kilogramów w wysłanych paczkach {suma_pustych_kilogramow}")

        
