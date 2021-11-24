from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        if len(self.ostokset) == 0:
            return 0

        lkm = sum(ostos.lukumaara() for ostos in self.ostokset)
        return lkm

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        if len(self.ostokset) == 0:
            return 0

        hinta = sum(ostos.hinta() for ostos in self.ostokset)
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)
        # lisää tuotteen
        self.ostokset.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
