"""Lisätään unittest ja varasto"""
import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """Tämä on testien luokka"""
    #luomiseen perustuvat testit
    def test_negatiivinen_tilavuus(self):
        """Luodaan varasto neg tilavuudella"""
        var = Varasto(-1)
        self.assertEqual(var.tilavuus, 0)

    def test_saldo_negatiivinen(self):
        """Luodaan varasto neg saldolla"""
        var = Varasto(10, -2)
        self.assertEqual(var.saldo, 0)

    def test_saldo_ylitilavuuden(self):
        """Luodaan varasto jossa saldo > tilavuus"""
        var = Varasto(3, 10)
        self.assertEqual(var.saldo, var.tilavuus)
    #lisaamiseen perustuvat testit
    def test_negatiivisen_lisaaminen(self):
        """lisätään varastoon neg määrä"""
        var = Varasto(10,5)
        var.lisaa_varastoon(-1)
        self.assertEqual(var.saldo, 5)

    def test_liika_lisaaminen(self):
        """lisätään varastoon enemmän kuin siellä voi olla"""
        var = Varasto(10,0)
        var.lisaa_varastoon(11)
        self.assertEqual(var.saldo, var.tilavuus)

    #Ottamiseen perustuvat testit
    def test_liika_ottaminen(self):
        """otetaan varastosta enemmän kuin siellä on"""
        var = Varasto(10,5)
        otto = var.ota_varastosta(7)
        self.assertEqual(otto, 5)
        self.assertEqual(var.saldo, 0)

    def test_negatiivinen_ottaminen(self):
        """otetaan neg määrä"""
        var = Varasto(10, 3)
        otto = var.ota_varastosta(-1)
        self.assertEqual(var.saldo, 3)
        self.assertEqual(otto, 0.0)
    def setUp(self):
        """Luodaan varasto"""
        self.varasto = Varasto(10)
    #__str__ testi
    def test_string(self):
        """return funktio"""
        var = Varasto(10, 5)
        oletus = "saldo = 5, vielä tilaa 5"
        self.assertEqual(str(var), oletus)





    #esimerkki testit
    def test_konstruktori_luo_tyhjan_varaston(self):
        """Luodaan tyhjä varasto"""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Luodaan varasto"""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Lisätään saldoa"""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """lisätään saldoa ja varmistetaan, että tilavuus pienentyy"""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """ottaminen palauttaa oikein"""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """ottamisen jälkeen on enemmän tilaa"""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
