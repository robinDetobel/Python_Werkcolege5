import math as m
class Cirkel:
    def __init__(self, straal):
        self.straal = straal

    def geef_omtrek(self):
        omtrek = 2 * m.pi * self.straal
        return omtrek

    def geef_oppervlakte(self):
        oppervlakte = m.pi * self.straal * self.straal
        return oppervlakte
