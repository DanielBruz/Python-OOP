"""
Meli bychom uprednostnovat Kompozici pred Dedicnosti. Dedicnost je dobra, ale v nekterych pripadech nam muze
komplikovat zivot.

Dědičnost:
(Dedičnosť umožňuje classam zdieľať ich atribúty a metódy. Jedna trida muze zdedit metody a atributy jinych.
"""


class Polozka():
    def __init__(self, nazev, autor, cena):
        self.nazev = nazev
        self.autor = autor
        self.cena = cena

    def zobraz(self):
        print(self.nazev, " od ", self.autor, " za ", self.cena, " EUR.")


polozka = Polozka("O Honzikovi a Marence", "Bratri Grimove", 5)
polozka.zobraz()


class Kniha(Polozka):
    pass


kniha = Kniha("O Honzikovi a Marence", "Bratri Grimove", 5)
kniha.zobraz()  # funguje, i kdyz trida Kniha(Polozka) obsahuje jen pass.


class Audiokniha(Polozka):  # atributy a metoda jsou zdedene z materske tridy Polozka.
    pass


audiokniha = Audiokniha("Ferda mravenec", "Ondrej Sekora", 7)
audiokniha.zobraz()


# Kompozice vs Dedicnost:
# Problem dedicnosti je, ze muzeme dedit atributy / metody, ktere nechceme, nebo jsou dokonce skodlive.
# Treba remove().

class Kosik(list):  # bude dedit ze seznamu (z listu)
    def vloz(self, polozka):
        if not isinstance(polozka, Polozka):
            raise TypeError("Jen polozky mohou byt pridavane do kosiku.")
        super().append(polozka)  # super() odkazuje na rodicovskou tridu "list" (vestavena).


kosik = Kosik()
kosik.vloz(polozka)
kosik.vloz(audiokniha)
kosik.vloz(5)  # vyhodi chybu TypeError s popisem, protoze mohou byt do kosiku vkladane jen objekty typu Polozka.

# pro vyjmuti z kosiku muzeme pouzit zdedenou metodu pop(). Vyjme polozku z kosiku a vrati nam jeji hodnotu.

kosik.pop(0)
kosik.remove(audiokniha)  # audiokniha bude odstranena z kosiku, ale nebude nadale k dispozici.


# Proto je lepší v tomto pripade zvolit misto dedicnosti Kompozici, abychom se vyhnuli dedeni např. remove().

# super () - umoznuje nam pouzit metody rodicovske tridy.

# dedeni __init__
# chceme zmenit inicializaci rodicovske funkce:
# vezmeme knihy, ktere se daji stahnout zadarmo. Tedy jejich cena po vlozeni do kosiku bude vzdy nulova:

class EbookZadarmo(Polozka):
    def __init__(self, nazev, autor):  # prepsali jsme inicializacni metodu tridy Polozka. Nevyzaduje atribut "cena".
        self.nazev = nazev
        self.autor = autor
        self.cena = 0


ebookzadarmo = EbookZadarmo("Temno", "Alois Jirasek ")
ebookzadarmo.zobraz()


class EbookZadarmo2(EbookZadarmo):  # s metodou super(). Podtrida tridy EbookZadarmo.
    def __init__(self, nazev, autor, promo):
        super().__init__(nazev, autor)  # nemusime vypisovat self.nazev = nazev atp.
        self.promo = promo


ebookzadarmo2 = EbookZadarmo2("Vona a mir", "Alexej Tolstoj", True)
ebookzadarmo2.zobraz()
