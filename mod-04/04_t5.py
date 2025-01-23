kt = "python"
ss = "rules"
kt_a = ""
ss_a = ""
x = 0

while kt != kt_a and ss != ss_a and x < 5:

    kt_a = input("Syötä käyttäjätunnus: ")
    ss_a = input("Syötä salasana: ")
    x += 1
    if kt == kt_a and ss == ss_a:
        print("\nTervetuloa!\n")
    elif x == 5:
        print("\nOlet syöttänyt virheellisen käyttäjätunnuksen tai salasanan viisi kertaa, yritä myöhemmin uudelleen.\n")
    else:
        print(f"\nPääsy evätty, yritä uudelleen. \nTämä oli {x}. yrityksesi. Maksimi yritykset: 5\n")

