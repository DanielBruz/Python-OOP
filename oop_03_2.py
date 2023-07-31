"""
Zname dalsi typ atributu, a to jsou lokalní promenne. Jsou jako klasicke promenne funkce. Lokali promenna se nepouziva
v definici se "self" ani se jmenem tridy. Nevaze se ani na tridu ani na objekt. Pusobi jen na urovni urcite funkce.
"""


class Kniha():
    vytistena = True

    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def zobraz_info(self):
        oddelovac = "/" # odstranili jsme "Kniha." a vnikla lokalni promenna.
        print("Nazev: ", self.nazev, oddelovac, "Cena: ", self.cena,
              oddelovac, "Vytistena: ", Kniha.vytistena)


kniha1 = Kniha("Honzik a Marenka", 7)
kniha2 = Kniha("Ferda mravenec", 5)

kniha1.zobraz_info()    # vsechno funguje

kniha2.oddelovac    # nefunguje, protoze venku mimo funkci neni lokalni promenna (lokalni atribut) videt.



