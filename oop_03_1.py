"""
Kontext atribútov a metód objektov Pythonu:
V Pythone môžeme vytvoriť premenné s dátami na niekoľkých úrovniach.
Oboznámili sme sa s objektovými atribútmi, ktoré sa viažu na self.
V tomto videu si povieme niečo o statických atribútoch a aký význam majú lokálne premenné.
Taktiež si ukážeme a vysvetlíme, ako fungujú metódy viazané na class a statické metódy.
"""

"""
Promenne jsou specificke pro konkretni instanci nebo Tridu, pokud jde o atributy objektu.
Atribut objektu je vazany na self.
"""


class Kniha():
    vytistena = True  # staticky atribut. Vsechny instance, objekty teto tridy maji pak tento atribut = True.

    def __init__(self, nazev, cena):  # self = inicializace konkretmí instance tridy
        self.nazev = nazev  # pouzijeme self, protoze se to vaze na konkretni objekt
        self.cena = cena

    def zobraz_info(self):
        Kniha.oddelovac = "/"   #  staticky atribut definovany v jine metode. Prebiraji ho vsechny objekty.
        # Zmenu hodnoty atributu staci udelat tady.
        # print("Nazev: ", self.nazev, "/ Cena: ", self.cena, "/ Vytistena: ", Kniha.vytistena)
        print("Nazev: ", self.nazev, Kniha.oddelovac, "Cena: ", self.cena,
              Kniha.oddelovac, "Vytistena: ", Kniha.vytistena)

# kniha1 = Kniha()
# kniha2 = Kniha()

# objektu priradime atributy. Např.:

# kniha1.cena = 7  # tento atribut je vazany na konkretni objekt
# print(kniha1.cena)  # vytisknu obsah atributu

"""
Zname i staticke atributy. Promenne na urovni tridy.
Lze je pouzit napric vsemi objekty.
Jsou definovane v konkretni tride.
"""
kniha1 = Kniha("Honzik a Marenka", 7)
kniha2 = Kniha("Ferda mravenec", 5)

kniha1.zobraz_info()
kniha2.zobraz_info()

"""
Staticke atributy mohou byt definovane i v metode __init__, v jine metode teto tridy, a dokonce mimo tridu.
Musi se ale pouzit v syntaxi "Nazev_tridy.atribut".
"""
print(kniha2.oddelovac) # oddelovac je tedy dostupny vsem instancim tridy

