"""
Getter a setter metody a properties:

Ak atribúty v objektoch enkapsulujeme a užívatelia našich class s nimi budú môcť manipulovať len pomocou
metód rozhrania, budeme ich musieť volať vždy, keď sa budeme chcieť k takémuto atribútu dostať.
Takýto kód je však menej Pythonovský. Aby sme mohli s rozhraním narábať, ako so samotným atribútom,
na to nám slúžia properties.

Privátní atributy by neměly být dostupné přímo, ale pouze pomocí metod getter a setter.

"""


class Kniha():
    def __init__(self, cena):
        self.__cena = cena  # privátní atribut __cena

    def get_cena(self):
        return self.__cena

    def set_cena(self, cena):
        self.__cena = cena


kniha1 = Kniha(5)
kniha2 = Kniha(10)

kniha1.get_cena()
kniha2.get_cena()

kniha1.set_cena(50)
kniha1.get_cena()

suma = kniha1.get_cena() + kniha2.get_cena()


# problém je, že kód je takto méně čitelný, než kdyby byl atribut cena otevřený formou self.cena = cena.
# Pak bychom mohli sčítat standardně suma = kniha1.cena + kniha2.cena
# Kódu by tak bylo méně. Snížili bychom tak riziko výskytu chyb.
# Na druhou stranu bychom tak přišli o enkapsulaci. Kdyby si každý mohl dělat s atributem cena co chce,
# mohli bychom se dostat do vážných problémů.
# Třeba zadání záporné ceny: při privátních atributech to ošetřím třeba takto:

def set_cena(self, cena):
    if cena < 0:
        self.__cena = 0
    else:
        self.__cena = cena


# když nebude atribut cena privátní, může být cena i záporná. Kdyby někdo použil atribut cena přímo,
# obešel by podmínku viz. výše. Jak tento problém řešit? :
# Python používá tzv. Properties:
# Před metody použijeme speciální atributy:

class Kniha():
    def __init__(self, cena):
        self.__cena = cena  # privátní atribut __cena

    @property
    def cena(self):  # upravím get_cena na cena
        return self.__cena

    @cena.setter
    def cena(self, cena):
        if cena < 0:
            self.__cena = 0
        else:
            self.__cena = cena


kniha1 = Kniha(5)
kniha2 = Kniha(10)

suma = kniha1.cena + kniha2.cena    # vypadá to, že voláme otevřený atribut cena, ale voláme cena.setter metodu.

kniha1.cena = -10
kniha1.cena # hodnota kniha1.cena = 0 !!!

