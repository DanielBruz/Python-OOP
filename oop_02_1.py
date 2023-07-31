"""
Vlastnosti objektov môžeme nastaviť počas ich inicializácie.
Vysvetlíme si, ako explicitne volať metódu __init__ a na čo slúži parameter self.
"""


class Kniha:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def zobraz_nazev(self):  # metoda tridy Kniha
        print("Nazev: ", self.nazev)

    def zobraz_cenu(self):
        print("Cena: ", self.cena)


# kniha = Kniha()  # vytvorime objekt
# kniha.nazev = "Honza a Marenka"  # priradime objektu atributy
# kniha.cena = 5.5

"""
existuje efektivnejsi cesta, jak inicializovat objekt, a to specialni metodou __init__
Tato metoda je inicialiizacni metoda. Nastavi pocatecni stav objektu. Je to konstruktor.
Vola se implicitne, kdyz se objekt vytvori, tedy kniha = Kniha().
Metodu __init__ si muzeme definovat primo v Tride, viz kod vyse.

Pak muzeme 3 radky vyse zjednodusit takto:
"""
kniha = Kniha("Honza a Marenka", 5.5)
kniha.zobraz_nazev()
kniha.zobraz_cenu()

"""
Atribut self reprezentuje samostatny objekt, tedy instanci, v tomto pripade "kniha"
Je to stejne, jako bychom do tridy zadali (kniha, nazev, cena): kniha.nazev = nazev atp.
Kazdy konkretni objekt je ale samostatny, proto ho zastupuje self. Tedy objekty např. kniha1, kniha2 atp.
"""
print(kniha.nazev)
print(kniha.cena)

"""
    def zobraz_nazev(self):  # metoda tridy Kniha
        self.atribut = atribut 
        (atribut muzeme vytvorit i jinde v tride, ale vzdy bude self odkazovat na konkretni objekt)
        print("Nazev: ", self.nazev)
"""
