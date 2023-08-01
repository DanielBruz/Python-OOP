"""
Magické metody:

Magické metódy pomáhajú vašim objektom získať známe a prívetivé rozhranie pre prácu s nimi.
Operátory ako plus, väčší než, menší než, reprezentácia, či len metóda sú vám k dispozícii pomocou týchto metód.
Ich použitie prezentuje polymorfizmus v akcii.

Jde o předdefinované metody, kterými můžeme obohatit své třídy. Jsou často používané pro emulování vestavěných typů.
Také jde o prezentaci matematických funkcí jako součet, větší než, menší než atp.

Mají před a za sebou podtržítka, jako např. __add__

Známe také __init__ metodu, která nastavuje počáteční stav objektu.

Umožňují definovat známé rozhranní.

Např. chceme vrátit velikost knihy a ta bude reprezentována počtem stránek. Použijeme __len__ metodu, která
normálně slouží pro určení délky řetězce nebo seznamu.

"""


# definujeme rozhranní pro knihu:

class Kniha():
    def __init__(self, nazev, autor, pocet_stran):
        self.nazev = nazev
        self.autor = autor
        self.pocet_stran = pocet_stran

    # vytvoříme si reprezentaci pomocí metody __repr__:

    def __repr__(self):
        return "{} : {}".format(self.nazev, self.autor)

    # definujeme si metodu pro velikost knihy pomocí __len__:

    def __len__(self):
        return self.pocet_stran


kniha = Kniha("Ocelove mesto", "Jules Verne", 320)
len(kniha)
print(kniha)

dir(list)   # vypsání metod



