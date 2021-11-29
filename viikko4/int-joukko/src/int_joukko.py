KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0
    
    def kuuluu(self, n):
        if n in self.ljono:
            return True
        return False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        self.ljono[self.alkioiden_lkm] = n
        self.alkioiden_lkm = self.alkioiden_lkm + 1

        # kasvatetaan taulukon kokoa ilman kopiointia
        if self.alkioiden_lkm == len(self.ljono):
            self.ljono.append([0] * self.kasvatuskoko)

        return True

    def poista(self, n):
        if not self.kuuluu(n):
            return False
        
        self.ljono.remove(n)
        self.ljono.append(0)
        self.alkioiden_lkm = self.alkioiden_lkm - 1
        return True

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        lukulista = self.ljono[:self.alkioiden_lkm]
        palautettava = ', '.join(str(i) for i in lukulista)
        return f'{{{palautettava}}}'
