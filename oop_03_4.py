# Udelame si metodu "ma_nazev", ktera nepracuje ani s daty objektu, ani s daty tridy.


class Kniha():
    vytistena = True

    def __init__(self, nazev, cena):
        self.nazev = self.ma_nazev(nazev)  # tady pouziji metodu "ma_nazev".
        self.cena = cena

    def zobraz_info(self):
        oddelovac = "/"
        print("Nazev: ", self.nazev, oddelovac, "Cena: ", self.cena,
              oddelovac, "Vytistena: ", Kniha.vytistena)

    @classmethod    # metoda tridy = dekorator classmethod
    def zobraz_tisk(cls):
        if Kniha.vytistena:
            print("Tištěná")
        else:
            print("Kniha neni tistena")

    @staticmethod   # staticka metoda = dokorator staticmethod, jinak nám vyhodi chybu, protože bude chtit doplnit self.
    def ma_nazev(nazev):
        if not isinstance(nazev, str):  # kdyz hodnota v nazev nebude string, treba prazdna hodnota atp.
            return "Neznámé jméno"
        else:  # a zmenime v __init__ "self.nazev = self.ma_nazev(nazev)
            return nazev


kniha1 = Kniha("Honzik a Marenka", 7)
kniha2 = Kniha(0, 5)  # nema zadany nazev
