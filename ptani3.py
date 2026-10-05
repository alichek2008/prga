nazev = input("Co kupuješ? ")
cena = float(input("Cena za kus (Kč): "))
pocet = int(input("Kolik kusů? "))

bez_dph = cena * pocet
dph = bez_dph * 0.12
s_dph = bez_dph + dph

print()
print("Položka:", nazev, "×", pocet)
print("Cena bez DPH:", bez_dph, "Kč")
print("DPH 12 %:", dph, "Kč")
print("Celkem k úhradě:", s_dph, "Kč")
