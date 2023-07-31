"""
Atributy i metody mají více úrovní.
Pridame novou metodu, ktera nema nic spolecneho s konkretni instanci tridy.
"""


class Kniha():
    vytistena = True

    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def zobraz_info(self):
        oddelovac = "/"
        print("Nazev: ", self.nazev, oddelovac, "Cena: ", self.cena,
              oddelovac, "Vytistena: ", Kniha.vytistena)

    # vytvorime si metodu, zda-li je kniha tistena (v eshopu muzeme resit, # zda je to e-book nebo audio).
    # Metoda nebude pracovat s daty objektu. "cls" = metoda se vaze na tridu a nepracuje s konkretnim objektem.
    # Nepracuje se "self", jen s atributem tridy, tedy jde o "metodu tridy". Oznacime ji dekoratorem classmetod:
    @classmethod
    def zobraz_tisk(cls):
        if Kniha.vytistena:     # "Kniha.vytistena == True:" je stejne jako "Kniha.vytistena:"
            print("Tištěná")
        else:
            print("Kniha neni tistena")


kniha1 = Kniha("Honzik a Marenka", 7)
kniha2 = Kniha("Ferda mravenec", 5)

kniha1.zobraz_tisk()

