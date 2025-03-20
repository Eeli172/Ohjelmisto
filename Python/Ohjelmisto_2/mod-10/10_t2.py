# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. 
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. 
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = []
        for i in range(hissien_määrä):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissi_nro, päämäärä):
            try:
                hissi = self.hissit[hissi_nro-1]

                if hissi_nro < 1 or hissi_nro > len(self.hissit):# jos kyseistä hissiä ei ole
                    print(f"\nHissiä nro. {hissi_nro} ei ole vielä rakennettu.")
        
                else:# jos kyseinen hissi on olemassa
                    print(f'\nMenit hissiin nro. {hissi_nro}, olet kerroksessa {hissi.nyk_kerros}')
                    hissi.siirry_kerrokseen(päämäärä)

            except IndexError:
                print(f"\nHissiä nro. {hissi_nro} ei ole vielä rakennettu.")



# pääohjelma

toimistorakennus = Talo(0, 15, 5)

toimistorakennus.aja_hissiä(1, 17)
toimistorakennus.aja_hissiä(1, -17)


toimistorakennus.aja_hissiä(2, 4)
toimistorakennus.aja_hissiä(2, 0)


toimistorakennus.aja_hissiä(0, 4)


toimistorakennus.aja_hissiä(6, 4)




