class Hissi:
    def __init__(self, min_kerros, max_kerros):
        self.min_kerros = min_kerros
        self.max_kerros = max_kerros
        self.nyk_kerros = min_kerros

    def siirry_kerrokseen(self, päämäärä):
        # jos päämääräksi annetaan liian pieni tai suuri kerros, muutetaan päämäärä min- tai max-kerrokseksi
        if päämäärä < self.min_kerros:
            print(f'Hissi ei kulje {päämäärä}. kerrokseen asti, hissi vie sinut nyt {self.min_kerros}. kerrokseen, joka on hissin ylin kerros.')
            päämäärä = self.min_kerros
        elif päämäärä > self.max_kerros:
            print(f'Hissi ei kulje {päämäärä}. kerrokseen asti, hissi vie sinut nyt {self.max_kerros}. kerrokseen, joka on hissin ylin kerros.')
            päämäärä = self.max_kerros

        # liikutetaan hissiä niin pitkään että se saapuu päämäärä-kerrokseen
        while self.nyk_kerros != päämäärä:
            if self.nyk_kerros < päämäärä:
                self.kerros_ylös()
            elif self.nyk_kerros > päämäärä:
                self.kerros_alas()
            

    def kerros_ylös(self):# hissi liikkuu kerroksen ylöspäin
        self.nyk_kerros += 1
        print(f'Hissi on nyt kerroksessa: {self.nyk_kerros}')

    def kerros_alas(self):# hissi liikkuu yhden kerroksen alaspäin
        self.nyk_kerros -= 1
        print(f'Hissi on nyt kerroksessa: {self.nyk_kerros}')


# pääohjelma

kone = Hissi(0,15)

kone.siirry_kerrokseen(10)
kone.siirry_kerrokseen(0)

