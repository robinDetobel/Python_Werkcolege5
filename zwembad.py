import circle as c

class zwembad:
    def __init__(self, straalz, b_pad, weg_prijs, omheining_prijs):
        self.straalz = straalz
        self.b_pad = b_pad
        self.weg_prijs = weg_prijs
        self.omheining_prijs = omheining_prijs

    def bad_grootte(self):
        cirkel = c.Cirkel(self.straalz)
        bad = cirkel.geef_oppervlakte()
        return bad

    def pad_oppervlakte(self):
        bad = c.Cirkel(self.straalz)
        bad_opp = bad.geef_oppervlakte()
        totaal = c.Cirkel(self.straalz+self.b_pad)
        totaal_opp = totaal.geef_oppervlakte()
        pad = totaal_opp - bad_opp
        return pad

    def pad_prijs(self):
        prijs_pad = self.pad_oppervlakte()*self.weg_prijs
        return prijs_pad

    def bereken_omheining_prijs(self):
        totstraal = self.straalz + self.b_pad
        totaal = c.Cirkel(totstraal)
        prijs_omheining = totaal.geef_omtrek() * self.omheining_prijs
        return prijs_omheining
