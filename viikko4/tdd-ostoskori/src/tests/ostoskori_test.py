import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

        self.maito = Tuote("Maito", 3)
        self.leipa = Tuote("Leipä", 5)

    # step 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # step 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # step 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta(self):
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 3)
    
    # step 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    # step 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)

        self.assertEqual(self.kori.hinta(), 8)
    
    # step 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    # step 7
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteen_hinta_kertaa_kaksi(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 2*self.maito.hinta())
    
    # step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)
 
        ostokset = self.kori.ostokset()

        # testaa että metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)
    
    # step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
 
        ostos = self.kori.ostokset()[0]
 
        # testaa onko palautetun listan ensimmäinen ostos on halutunlainen
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)
    
    # step 10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.leipa)
 
        ostokset = self.kori.ostokset()

        # testaa että metodin palauttaman listan pituus 2
        self.assertEqual(len(ostokset), 2)
    
    # step 11
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
    
    # step 12
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
 
        ostos = self.kori.ostokset()[0]
 
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)
    
    # step 13
    def test_kahden_saman_tuotteen_lisaamisen_ja_yhden_postamisen_jalkeen_korissa_ostosolio_oikealla_nimella_ja_maaralla(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.kori.poista_tuote(self.maito)
 
        ostos = self.kori.ostokset()[0]
 
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

