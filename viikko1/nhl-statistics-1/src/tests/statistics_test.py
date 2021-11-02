import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_alustetaan_oikea_pelaajalista(self):
        pelaajat = list(map(lambda x: x.name ,self.statistics._players))
        self.assertEqual(pelaajat, ["Semenko", "Lemieux", "Kurri", "Yzerman", "Gretzky"])
    
    def test_hakee_oikean_pelaajan(self):
        pelaaja = self.statistics.search("Kurri")
        self.assertEqual(pelaaja.name, "Kurri")
    
    def test_pelaajaa_ei_loydy_palauttaa_none(self):
        pelaaja = self.statistics.search("Hiiri")
        self.assertEqual(pelaaja, None)

    def test_hakee_tietyn_joukkueen_pelaajat(self):
        pelaajat = list(map(lambda x: x.name ,self.statistics.team("EDM")))
        self.assertEqual(pelaajat, ["Semenko", "Kurri", "Gretzky"])
    
    def test_parhaat_kolme_oikein(self):
        pelaajat = list(map(lambda x: x.name, self.statistics.top_scorers(3)))
        parhaat = ["Gretzky", "Lemieux", "Yzerman"]
        self.assertEqual(pelaajat, parhaat)