import circle as c
import zwembad as z

c1 = c.Cirkel(15)
print(c1.geef_oppervlakte())
print(c1.geef_omtrek())

straal = float(input("Geef de straal van het zwembad in: "))
breedte = float(input("Geef de breedte van het pad rondom het zwembad in: "))
prijs_weg = float(input("Geef de aanlegprijs van het pad in per m²: "))
prijs_rondom = float(input("Geef de prijs van de omheining rond het zwembad in per m: "))

b1 = z.zwembad(straal, breedte, prijs_weg, prijs_rondom)

print("De prijs van het pad is: " + str(b1.pad_prijs()))
print("De prijs van de omheining romdom het zwembad is: " + str(b1.bereken_omheining_prijs()))
totaal_prijs = b1.pad_prijs() + b1.bereken_omheining_prijs()
print("De totaalprijs is: " + str(totaal_prijs))
