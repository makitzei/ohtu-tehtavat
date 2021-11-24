from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        if len(self._ostokset) == 0:
            return 0

        lkm = sum(ostos.lukumaara() for ostos in self._ostokset)
        return lkm

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        if len(self._ostokset) == 0:
            return 0

        hinta = sum(ostos.hinta() for ostos in self._ostokset)
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # tarkistetaan onko tuote korissa
        uusi_tuote = True
        for ostos in self._ostokset:
            if lisattava.nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(1)
                uusi_tuote = False
                break
        # jos uusi, lisää tuotteen
        if uusi_tuote:
            self._ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self._ostokset:
            if poistettava.nimi() == ostos.tuotteen_nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self._ostokset.remove(ostos)
                break

    def tyhjenna(self):
        self._ostokset.clear()

    def ostokset(self):
        return self._ostokset
        
