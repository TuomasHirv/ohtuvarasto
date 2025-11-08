"""Emme tarvitse moduuleja tähän"""
class Varasto:
    """Varasto on luokka jossa pidetään tiedossa tilavuutta ja saldoa."""

    def __init__(self, tilavuus, alku_saldo = 0):
        self.tilavuus = tilavuus
        if tilavuus < 0.0:
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    #ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa
    def paljonko_mahtuu(self):
        """Lasketaan paljon tilavuutta on jäljellä"""
        return self.tilavuus - self.saldo
 #testaåspdoaåspldåasldäöalsäödlaäösldasd
    def lisaa_varastoon(self, maara):
        """Lisätään varastoon saldoa"""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus
    #Varastosta ottaminen
    def ota_varastosta(self, maara):
        """Otetaan varastosta saldoa"""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara
    #kutsuessa varastoa niin tämä palautetaan.
    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
