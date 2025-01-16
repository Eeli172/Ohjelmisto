kuha_cm = float(input("kuhan pituus cm: "))

if kuha_cm < 37:
    puuttuu = 37 - kuha_cm
    print(f"Kuha on alimittainen, alimmasta sallitusta pyyntimitasta puuttuu {puuttuu:.2f} cm")
